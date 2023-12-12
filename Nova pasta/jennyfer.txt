import 'package:flutter/material.dart';
import 'package:path/path.dart';
import 'package:sqflite/sqflite.dart';

void main() {
  runApp(CadastroApp());
}

class Livro {
  final int id;
  final String titulo;
  final String autor;
  final String genero;

  Livro({
    required this.id,
    required this.titulo,
    required this.autor,
    required this.genero,
  });

  Map<String, dynamic> toMap() {
    return {
      'id': id,
      'titulo': titulo,
      'autor': autor,
      'genero': genero,
    };
  }

  factory Livro.fromMap(Map<String, dynamic> map) {
    return Livro(
      id: map['id'],
      titulo: map['titulo'],
      autor: map['autor'],
      genero: map['genero'],
    );
  }
}

class LivrosDatabase {
  late Database _database;

  Future<Database> open() async {
    String databasesPath = await getDatabasesPath();
    String path = join(databasesPath, 'livro.sdb');

    _database = await openDatabase(
      path,
      version: 1,
      onCreate: _createDB,
    );

    return _database;
  }

  Future<void> _createDB(Database db, int version) async {
    await db.execute('''
      CREATE TABLE IF NOT EXISTS livros (
        id INTEGER PRIMARY KEY,
        titulo TEXT NOT NULL,
        autor TEXT NOT NULL,
        genero TEXT
      )
    ''');
  }

  Future<int> insertLivro(Livro livro) async {
    return await _database.insert(
      'livros',
      livro.toMap(),
      conflictAlgorithm: ConflictAlgorithm.replace,
    );
  }

  Future<List<Livro>> livros() async {
    final List<Map<String, dynamic>> maps = await _database.query('livros');
    return List.generate(maps.length, (i) {
      return Livro.fromMap(maps[i]);
    });
  }
}

class CadastroApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Cadastro App',
      home: CadastroScreen(),
    );
  }
}

class CadastroScreen extends StatelessWidget {
  final LivrosDatabase livrosDatabase = LivrosDatabase();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Biblioteca', style: TextStyle(color: Colors.white)),
        backgroundColor: Color.fromARGB(255, 122, 81, 26),
      ),
      backgroundColor: Color.fromARGB(210, 231, 177, 107),
      body: Center(
        child: CadastroForm(livrosDatabase),
      ),
    );
  }
}

class CadastroForm extends StatefulWidget {
  final LivrosDatabase livrosDatabase;

  CadastroForm(this.livrosDatabase);

  @override
  _CadastroFormState createState() => _CadastroFormState();
}

class _CadastroFormState extends State<CadastroForm> {
  final _formKey = GlobalKey<FormState>();
  final _tituloController = TextEditingController();
  final _autorController = TextEditingController();
  final _generoController = TextEditingController();

  String _connectionMessage = ''; // Connection message placeholder

  @override
  Widget build(BuildContext context) {
    return Form(
      key: _formKey,
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Container(
            width: 300,
            decoration: BoxDecoration(
              color: const Color.fromARGB(255, 211, 194, 157),
              border: Border.all(color: const Color.fromARGB(255, 0, 0, 0)),
              borderRadius: BorderRadius.circular(8.0),
            ),
            child: TextFormField(
              controller: _tituloController,
              style: TextStyle(color: const Color.fromARGB(255, 0, 0, 0)),
              validator: (value) {
                if (value!.isEmpty) {
                  return 'Campo obrigatório';
                }
                return null;
              },
              decoration: InputDecoration(
                labelText: 'Título do Livro',
                labelStyle: TextStyle(color: const Color.fromARGB(255, 0, 0, 0)),
                border: InputBorder.none,
                contentPadding: EdgeInsets.all(12.0),
              ),
            ),
          ),
          SizedBox(height: 10),
          Container(
            width: 300,
            decoration: BoxDecoration(
              color: const Color.fromARGB(255, 211, 194, 157),
              border: Border.all(color: const Color.fromARGB(255, 0, 0, 0)),
              borderRadius: BorderRadius.circular(8.0),
            ),
            child: TextFormField(
              controller: _autorController,
              style: TextStyle(color: const Color.fromARGB(255, 0, 0, 0)),
              validator: (value) {
                if (value!.isEmpty) {
                  return 'Campo obrigatório';
                }
                return null;
              },
              decoration: InputDecoration(
                labelText: 'Nome do Autor(a)',
                labelStyle: TextStyle(color: const Color.fromARGB(255, 0, 0, 0)),
                border: InputBorder.none,
                contentPadding: EdgeInsets.all(12.0),
              ),
            ),
          ),
          SizedBox(height: 10),
          Container(
            width: 300,
            decoration: BoxDecoration(
              color: Color.fromARGB(255, 211, 194, 157),
              border: Border.all(color: const Color.fromARGB(255, 0, 0, 0)),
              borderRadius: BorderRadius.circular(8.0),
            ),
            child: TextFormField(
              controller: _generoController,
              style: TextStyle(color: const Color.fromARGB(255, 0, 0, 0)),
              validator: (value) {
                if (value!.isEmpty) {
                  return 'Campo obrigatório';
                }
                return null;
              },
              decoration: InputDecoration(
                labelText: 'Gênero do Livro',
                labelStyle: TextStyle(color: const Color.fromARGB(255, 0, 0, 0)),
                border: InputBorder.none,
                contentPadding: EdgeInsets.all(12.0),
              ),
            ),
          ),
          SizedBox(height: 20),
          ElevatedButton(
            onPressed: () async {
              if (_formKey.currentState!.validate()) {
                await _insertLivro();
                _tituloController.clear();
                _autorController.clear();
                _generoController.clear();
              }
            },
            style: ButtonStyle(
              backgroundColor: MaterialStateProperty.all<Color>(Color.fromARGB(255, 167, 125, 48)),
            ),
            child: Text('Cadastrar'),
          ),
          SizedBox(height: 20),
          ElevatedButton(
            onPressed: () {
              Navigator.of(context).push(
                MaterialPageRoute(builder: (ctx) => ListaLivrosScreen(widget.livrosDatabase)),
              );
            },
            style: ButtonStyle(
              backgroundColor: MaterialStateProperty.all<Color>(Color.fromARGB(255, 167, 125, 48)),
            ),
            child: Text('Ver Lista de Livros'),
          ),
          // Display connection message
          Padding(
            padding: const EdgeInsets.all(8.0),
            child: Text(
              _connectionMessage,
              style: TextStyle(color: Colors.green),
            ),
          ),
        ],
      ),
    );
  }

  Future<void> _insertLivro() async {
    final database = await widget.livrosDatabase.open();

    await database.insert(
      'livros',
      {
        'titulo': _tituloController.text,
        'autor': _autorController.text,
        'genero': _generoController.text,
      },
      conflictAlgorithm: ConflictAlgorithm.replace,
    );

    setState(() {
      _connectionMessage = 'Conexão com o banco de dados estabelecida com sucesso!';
    });
  }
}

class ListaLivrosScreen extends StatefulWidget {
  final LivrosDatabase livrosDatabase;

  ListaLivrosScreen(this.livrosDatabase);

  @override
  _ListaLivrosScreenState createState() => _ListaLivrosScreenState();
}

class _ListaLivrosScreenState extends State<ListaLivrosScreen> {
  List<Livro> _livrosCadastrados = [];

  @override
  void initState() {
    super.initState();
    _queryAll();
  }

  Future<void> _queryAll() async {

    final List<Livro> livros = await widget.livrosDatabase.livros();

    setState(() {
      _livrosCadastrados = livros;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Lista de Livros', style: TextStyle(color: Colors.white))),
      backgroundColor: Color.fromARGB(210, 231, 177, 107),
      body: ListaLivros(livrosCadastrados: _livrosCadastrados),
    );
  }
}

class ListaLivros extends StatelessWidget {
  final List<Livro> livrosCadastrados;

  ListaLivros({required this.livrosCadastrados});

  @override
  Widget build(BuildContext context) {
    return ListView.separated(
      itemCount: livrosCadastrados.length,
      separatorBuilder: (BuildContext context, int index) {
        return Divider(
          color: Colors.black,
          thickness: 1.0,
        );
      },
      itemBuilder: (ctx, index) {
        return ListTile(
          title: Text(livrosCadastrados[index].titulo),
          subtitle: Text(livrosCadastrados[index].autor),
          trailing: Text(livrosCadastrados[index].genero),
        );
      },
    );
  }
}
