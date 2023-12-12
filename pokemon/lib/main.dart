import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';
import 'dart:math';
import 'package:cached_network_image/cached_network_image.dart';

void main() {
  runApp(MyApp());
}

class Pokemon {
  final String name;
  int hp;
  final int attack;
  final int defense;
  final String type;
  final String spriteUrl;

  Pokemon({
    required this.name,
    required this.hp,
    required this.attack,
    required this.defense,
    required this.type,
    required this.spriteUrl,
  });
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: PokemonSelectionScreen(),
    );
  }
}

class PokemonSelectionScreen extends StatefulWidget {
  @override
  _PokemonSelectionScreenState createState() => _PokemonSelectionScreenState();
}

class _PokemonSelectionScreenState extends State<PokemonSelectionScreen> {
  Future<List<Pokemon>> _fetchPokemons() async {
    final List<int> randomIds = List.generate(3, (index) => Random().nextInt(898) + 1);

    final List<Pokemon> pokemons = [];

    for (final id in randomIds) {
      final response = await http.get(Uri.parse('https://pokeapi.co/api/v2/pokemon/$id'));
      if (response.statusCode == 200) {
        final data = jsonDecode(response.body);
        final name = data['name'];
        final hp = data['stats'][0]['base_stat'];
        final attack = data['stats'][1]['base_stat'];
        final defense = data['stats'][2]['base_stat'];
        final type = data['types'][0]['type']['name'];
        final spriteUrl = 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/$id.png';

        final pokemon = Pokemon(
          name: name,
          hp: hp,
          attack: attack,
          defense: defense,
          type: type,
          spriteUrl: spriteUrl,
        );

        pokemons.add(pokemon);
      }
    }

    return pokemons;
  }

  Future<Pokemon> _fetchRandomPokemon() async {
    final int randomId = Random().nextInt(898) + 1;
    final response = await http.get(Uri.parse('https://pokeapi.co/api/v2/pokemon/$randomId'));
    if (response.statusCode == 200) {
      final data = jsonDecode(response.body);
      final name = data['name'];
      final hp = data['stats'][0]['base_stat'];
      final attack = data['stats'][1]['base_stat'];
      final defense = data['stats'][2]['base_stat'];
      final type = data['types'][0]['type']['name'];
      final spriteUrl = 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/$randomId.png';

      return Pokemon(
        name: name,
        hp: hp,
        attack: attack,
        defense: defense,
        type: type,
        spriteUrl: spriteUrl,
      );
    } else {
      throw Exception('Falha ao carregar o Pokémon oponente');
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('TCG Pokémon Battle'),
      ),
      body: Center(
        child: FutureBuilder<List<Pokemon>>(
          future: _fetchPokemons(),
          builder: (context, snapshot) {
            if (snapshot.connectionState == ConnectionState.waiting) {
              return CircularProgressIndicator();
            } else if (snapshot.hasError) {
              return Text('Erro ao carregar os Pokémon: ${snapshot.error}');
            } else if (!snapshot.hasData) {
              return Text('Nenhum dado encontrado');
            } else {
              final pokemons = snapshot.data!;
              return Column(
                children: [
                  Text('Escolha um Pokémon para batalhar:'),
                  for (final pokemon in pokemons)
                    Card(
                      child: ListTile(
                        title: Text(pokemon.name),
                        subtitle: Column(
                          crossAxisAlignment: CrossAxisAlignment.start,
                          children: [
                            Text(
                              'HP: ${pokemon.hp}\nAtaque: ${pokemon.attack}\nDefesa: ${pokemon.defense}\nTipo: ${pokemon.type}',
                            ),
                            LinearProgressIndicator(
                              value: pokemon.hp / 100,
                              color: Colors.green,
                              backgroundColor: Colors.grey,
                            ),
                          ],
                        ),
                        leading: CachedNetworkImage(
                          imageUrl: pokemon.spriteUrl,
                          placeholder: (context, url) => CircularProgressIndicator(),
                          errorWidget: (context, url, error) => Icon(Icons.error),
                        ),
                        trailing: ElevatedButton(
                          onPressed: () async {
                            final randomOpponent = await _fetchRandomPokemon();

                            Navigator.of(context).push(
                              MaterialPageRoute(
                                builder: (context) => BattleScreen(
                                  userPokemon: pokemon,
                                  opponentPokemon: randomOpponent,
                                ),
                              ),
                            );
                          },
                          child: Text('Escolher'),
                        ),
                      ),
                    ),
                ],
              );
            }
          },
        ),
      ),
    );
  }
}

class BattleScreen extends StatefulWidget {
  final Pokemon userPokemon;
  final Pokemon opponentPokemon;

  BattleScreen({
    required this.userPokemon,
    required this.opponentPokemon,
  });

  @override
  _BattleScreenState createState() => _BattleScreenState();
}

class _BattleScreenState extends State<BattleScreen> {
  bool battleInProgress = false;
  String battleResult = '';

  Future<void> attack() async {
    setState(() {
      battleInProgress = true;
    });

    await Future.delayed(Duration(seconds: 2));

    final userAttack = widget.userPokemon.attack;
    final opponentDefense = widget.opponentPokemon.defense;
    final randomFactor = Random().nextDouble() * 0.2 + 0.9;

    final damage = (userAttack / opponentDefense * 10 * randomFactor).round();

    setState(() {
      widget.opponentPokemon.hp -= damage;
      battleInProgress = false;

      if (widget.opponentPokemon.hp <= 0) {
        battleResult = 'Você venceu!';
      } else {
        final opponentAttack = widget.opponentPokemon.attack;
        final userDefense = widget.userPokemon.defense;
        final opponentDamage = (opponentAttack / userDefense * 10 * randomFactor).round();
        final newUserHp = widget.userPokemon.hp - opponentDamage;

        if (newUserHp <= 0) {
          battleResult = 'Você perdeu!';
        } else {
          widget.userPokemon.hp = newUserHp;

          final userDefense = widget.userPokemon.defense;
          final opponentAttack = widget.opponentPokemon.attack;
          final userDamage = (opponentAttack / userDefense * 10 * randomFactor).round();
          final newOpponentHp = widget.opponentPokemon.hp - userDamage;

          if (newOpponentHp <= 0) {
            battleResult = 'Você venceu!';
          } else {
            widget.opponentPokemon.hp = newOpponentHp;
          }
        }
      }
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Batalha Pokémon'),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Text('Seu Pokémon: ${widget.userPokemon.name}'),
            CachedNetworkImage(
              imageUrl: widget.userPokemon.spriteUrl,
              placeholder: (context, url) => CircularProgressIndicator(),
              errorWidget: (context, url, error) => Icon(Icons.error),
            ),
            Text(
              'HP: ${widget.userPokemon.hp}\nAtaque: ${widget.userPokemon.attack}\nDefesa: ${widget.userPokemon.defense}\nTipo: ${widget.userPokemon.type}',
            ),
            LinearProgressIndicator(
              value: widget.userPokemon.hp / 100,
              color: Colors.green,
              backgroundColor: Colors.grey,
              minHeight: 10, // Ajuste a altura desejada da barra de vida
            ),
            SizedBox(height: 20),
            if (widget.opponentPokemon.hp > 0)
              Column(
                children: [
                  Text('Pokémon Oponente: ${widget.opponentPokemon.name}'),
                  CachedNetworkImage(
                    imageUrl: widget.opponentPokemon.spriteUrl,
                    placeholder: (context, url) => CircularProgressIndicator(),
                    errorWidget: (context, url, error) => Icon(Icons.error),
                  ),
                  Text(
                    'HP: ${widget.opponentPokemon.hp}\nAtaque: ${widget.opponentPokemon.attack}\nDefesa: ${widget.opponentPokemon.defense}\nTipo: ${widget.opponentPokemon.type}',
                  ),
                  LinearProgressIndicator(
                    value: widget.opponentPokemon.hp / 100,
                    color: Colors.green,
                    backgroundColor: Colors.grey,
                    minHeight: 10, // Ajuste a altura desejada da barra de vida
                  ),
                ],
              ),
            SizedBox(height: 20),
            if (battleInProgress)
              CircularProgressIndicator()
            else if (battleResult.isNotEmpty)
              Text(
                battleResult,
                style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold),
              )
            else
              ElevatedButton(
                onPressed: () {
                  attack();
                },
                child: Text('Atacar'),
              ),
          ],
        ),
      ),
    );
  }
}
