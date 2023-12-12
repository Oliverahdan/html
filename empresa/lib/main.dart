import 'package:flutter/material.dart';
import 'dart:convert';
import 'dart:io';
import 'package:path_provider/path_provider.dart';

void main() {
  runApp(MyApp());
}

class UserInfo {
  String name = '';
  String birthDate = 'dd/mm/aaaa';
  String occupation = 'empreendedor';

  Map<String, dynamic> toJson() {
    return {
      'name': name,
      'birthDate': birthDate,
      'occupation': occupation,
    };
  }
}


class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'User Info Form',
      home: UserInfoForm(),
    );
  }
}

class UserInfoForm extends StatefulWidget {
  @override
  _UserInfoFormState createState() => _UserInfoFormState();
}

class _UserInfoFormState extends State<UserInfoForm> {
  final _formKey = GlobalKey<FormState>();
  final UserInfo userInfo = UserInfo();
  String _savedJson = '';

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('User Info Form'),
      ),
      body: Padding(
        padding: EdgeInsets.all(16.0),
        child: Form(
          key: _formKey,
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: <Widget>[
              TextFormField(
                decoration: InputDecoration(labelText: 'Nome'),
                validator: (value) {
                  if (value == null || value.isEmpty) {
                    return 'Insira um nome';
                  }
                  return null;
                },
                onSaved: (value) {
                  userInfo.name = value!;
                },
              ),
              TextFormField(
                decoration: InputDecoration(labelText: 'Data de Nascimento (dd/mm/aaaa)'),
                validator: (value) {
                  if (value == null || value.isEmpty) {
                    return 'Insira uma data de nascimento';
                  }
                  return null;
                },
                onSaved: (value) {
                  userInfo.birthDate = value!;
                },
              ),
              DropdownButtonFormField<String>(
                decoration: InputDecoration(labelText: 'Ocupação'),
                value: userInfo.occupation,
                onChanged: (value) {
                  setState(() {
                    userInfo.occupation = value!;
                  });
                },
                items: ['empreendedor', 'empregado', 'estagiario']
                    .map<DropdownMenuItem<String>>(
                      (String value) => DropdownMenuItem<String>(
                        value: value,
                        child: Text(value),
                      ),
                    )
                    .toList(),
              ),
              ElevatedButton(
                onPressed: () async {
                  if (_formKey.currentState!.validate()) {
                    _formKey.currentState!.save();

                    await _submitForm();

                    ScaffoldMessenger.of(context).showSnackBar(
                      SnackBar(content: Text('Informações salvas com sucesso!')),
                    );
                  }
                },
                child: Text('Salvar'),
              ),
              Text(_savedJson),
            ],
          ),
        ),
      ),
    );
  }

  Future<void> _submitForm() async {
  final directory = await getApplicationDocumentsDirectory();
  final file = File('${directory.path}/user_info.json');

  List<Map<String, dynamic>> existingData = [];
  if (file.existsSync()) {
    final existingJson = await file.readAsString();
    existingData = List<Map<String, dynamic>>.from(json.decode(existingJson));
  }

  final newUserInfo = userInfo.toJson();

  // Adicionar as novas informações ao final da lista
  existingData.add(newUserInfo);

  final updatedJson = jsonEncode(existingData);

  print('Caminho do arquivo JSON: ${file.path}');
  print('Conteúdo atualizado do arquivo JSON: $updatedJson');

  await file.writeAsString(updatedJson);

  setState(() {
    _savedJson = updatedJson;
  });
 }
}