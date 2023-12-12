import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';
import 'package:country_list_pick/country_list_pick.dart';
import 'package:timezone/standalone.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: TripPlanner(),
    );
  }
}

class TripPlanner extends StatefulWidget {
  @override
  _TripPlannerState createState() => _TripPlannerState();
}

class _TripPlannerState extends State<TripPlanner> {
  final GlobalKey<FormState> _formKey = GlobalKey<FormState>();
  TextEditingController estimatedArrivalTimeController = TextEditingController();
  TextEditingController availableMoneyController = TextEditingController();

  String originCountryCode = ''; // Alterado para tipo String?
  String destinationCountryCode = ''; // Alterado para tipo String?
  double estimatedArrivalTime = 0.0;
  double availableMoney = 0.0;
  final String openCageApiKey = '09afbe586d2a44f9ac80f83d8da4f534';
  final String openExchangeRatesApiKey = 'ae8a61c69d9744a3b9577d1eb98b3a79';

  Map<String, String> countryToContinent = {
    'BR': 'America',
    'US': 'America',
    'EU': 'Europe',
    'JP': 'Asia',
    'GB': 'Europe',
    'CA': 'America',
    'AU': 'Australia',
    // Adicione mais países e continentes conforme necessário
  };

  Future<int> getTimezoneOffsetByContinent(String continent) async {
    final location = getLocation(continent);
    if (location == null) {
      return 0; // Retorna 0 como valor padrão se o continente não for encontrado
    }
    final now = DateTime.now();
    final timeZone = location.timeZone(now as int);
    final timeZoneOffset = timeZone.offset.inHours; // Obtém o offset em horas
    return timeZoneOffset;
  }

  Future<String> getCountryFromLocation(String? location) async {
    if (location == null || location.isEmpty) {
      return 'Campo vazio';
    }

    final String url =
        'https://api.opencagedata.com/geocode/v1/json?q=${Uri.encodeComponent(location)}&key=$openCageApiKey';

    try {
      final response = await http.get(Uri.parse(url));

      if (response.statusCode == 200) {
        final Map<String, dynamic> data = json.decode(response.body);
        if (data['results'] != null && data['results'].isNotEmpty) {
          final components = data['results'][0]['components'];
          final country = components['country'];
          return country;
        }
      }

      return 'País não encontrado';
    } catch (e) {
      print('Erro na pesquisa do país: $e');
      return 'Erro na pesquisa do país';
    }
  }

  Future<double> convertCurrency(double amount, String fromCurrency, String toCurrency) async {
    final String url =
        'https://openexchangerates.org/api/convert?from=$fromCurrency&to=$toCurrency&amount=$amount&app_id=$openExchangeRatesApiKey';

    try {
      final response = await http.get(Uri.parse(url));

      if (response.statusCode == 200) {
        final Map<String, dynamic> data = json.decode(response.body);
        final double convertedAmount = data['response'];
        return convertedAmount;
      }

      return 0.0; // Taxa de câmbio não encontrada
    } catch (e) {
      print('Erro na conversão de moeda: $e');
      return 0.0;
    }
  }

  void clearFields() {
    estimatedArrivalTimeController.clear();
    availableMoneyController.clear();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Viagem Inteligente'),
      ),
      body: SingleChildScrollView(
        child: Padding(
          padding: const EdgeInsets.all(16.0),
          child: Form(
            key: _formKey,
            child: Column(
              children: <Widget>[
                CountryListPick(
                  // Use a biblioteca CountryListPick para selecionar o país de origem
                  theme: CountryTheme(
                    isShowFlag: true,
                    isShowTitle: false,
                    isShowCode: true,
                    isDownIcon: true,
                    showEnglishName: true,
                  ),
                  initialSelection: '+1',
                  onChanged: (CountryCode? code) {
                    setState(() {
                      originCountryCode = code?.code ?? '';
                    });
                  },
                ),
                CountryListPick(
                  // Use a biblioteca CountryListPick para selecionar o país de destino
                  theme: CountryTheme(
                    isShowFlag: true,
                    isShowTitle: false,
                    isShowCode: true,
                    isDownIcon: true,
                    showEnglishName: true,
                  ),
                  initialSelection: '+1',
                  onChanged: (CountryCode? code) {
                    setState(() {
                      destinationCountryCode = code?.code ?? '';
                    });
                  },
                ),
                TextFormField(
                  controller: estimatedArrivalTimeController,
                  decoration: InputDecoration(labelText: 'Horário de Chegada Estimada (hh:mm)'),
                  onChanged: (value) {
                    // Implemente a lógica para analisar as horas e os minutos separadamente aqui
                    // Por exemplo, você pode usar expressões regulares para garantir o formato correto.
                  },
                  validator: (value) {
                    // Implemente a validação para garantir o formato correto (hh:mm)
                    if (value == null || !RegExp(r'^\d{2}:\d{2}$').hasMatch(value)) {
                      return 'Formato inválido (hh:mm)';
                    }
                    return null;
                  },
                ),
                TextFormField(
                  controller: availableMoneyController,
                  decoration: InputDecoration(
                    labelText: 'Quantidade de Dinheiro Disponível',
                    prefixText: getCurrencySymbol(originCountryCode), // Adiciona o símbolo da moeda
                  ),
                  onChanged: (value) {
                    availableMoney = double.tryParse(value) ?? 0.0;
                  },
                  validator: (value) {
                    if (value == null || value.isEmpty) {
                      return 'Campo obrigatório';
                    }
                    return null;
                  },
                ),

                SizedBox(height: 20),
                ElevatedButton(
                  onPressed: () async {
                    if (_formKey.currentState!.validate()) {
                      // Chame funções para calcular tempo de viagem, conversão de moeda, etc.

                      final originTimezoneOffset =
                          await getTimezoneOffsetByContinent(countryToContinent[originCountryCode]!);
                      final destinationTimezoneOffset =
                          await getTimezoneOffsetByContinent(countryToContinent[destinationCountryCode]!);

                      final timezoneDifference = originTimezoneOffset - destinationTimezoneOffset;

                      final convertedMoney = await convertCurrency(availableMoney, originCountryCode, destinationCountryCode);
                      print('Dinheiro convertido: $convertedMoney');
                      print('Diferença de fuso horário: $timezoneDifference horas');

                      // Exiba o pop-up "Viagem Planejada" com os resultados
                      showDialog(
                        context: context,
                        builder: (BuildContext context) {
                          return AlertDialog(
                            title: Text('Viagem Planejada'),
                            content: Column(
                              children: [
                                Text('Dinheiro convertido: $convertedMoney'),
                                Text('Diferença de fuso horário: $timezoneDifference horas'),
                              ],
                            ),
                            actions: <Widget>[
                              TextButton(
                                child: Text('Fechar'),
                                onPressed: () {
                                  Navigator.of(context).pop();
                                },
                              ),
                            ],
                          );
                        },
                      );

                      // Limpar os campos de entrada
                      clearFields();
                    }
                  },
                  child: Text('Planejar Viagem'),
                ),
              ],
            ),
          ),
        ),
      ),
      drawer: Drawer(
        child: ListView(
          padding: EdgeInsets.zero,
          children: <Widget>[
            DrawerHeader(
              child: Text('Histórico de Viagem'),
              decoration: BoxDecoration(
                color: Colors.blue,
              ),
            ),
            // Lista de viagens passadas do banco de dados
          ],
        ),
      ),
    );
  }
}
