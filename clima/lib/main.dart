import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';
import 'package:weather_icons/weather_icons.dart';

void main() {
  runApp(MyApp());
}

class WeatherData {
  final String cityName;
  final double temperature;
  String description;
  final String iconCode;

  WeatherData({
    required this.cityName,
    required this.temperature,
    required this.description,
    required this.iconCode,
  });

  factory WeatherData.fromJson(Map<String, dynamic> json) {
    String description = json['weather'][0]['description'];
    String iconCode = json['weather'][0]['icon'];
    return WeatherData(
      cityName: json['name'],
      temperature: json['main']['temp'].toDouble() - 273.15,
      description: description,
      iconCode: iconCode,
    );
  }
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Meteorologia',
      home: WeatherScreen(),
    );
  }
}

class WeatherScreen extends StatefulWidget {
  @override
  _WeatherScreenState createState() => _WeatherScreenState();
}

class _WeatherScreenState extends State<WeatherScreen> {
  WeatherData? weatherData;
  List<String> citiesInBrazil = []; // Lista de cidades brasileiras
  List<String> citiesInState = [];
  String selectedCity = '';
  
  List<String> states = [
    'UF', 'AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS',
    'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO',
  ];
  String selectedState = 'UF';

  Map<String, IconData> weatherIconMap = {
    "01d": WeatherIcons.day_sunny,
    "02d": WeatherIcons.day_cloudy,
    "03d": WeatherIcons.cloud,
    "04d": WeatherIcons.cloudy,
    "09d": WeatherIcons.showers,
    "10d": WeatherIcons.rain,
    "11d": WeatherIcons.thunderstorm,
    "13d": WeatherIcons.snow,
    "50d": WeatherIcons.fog,
    
    // Mapeamentos de ícones...
  };

  Map<String, Color> weatherColorMap = {
    "01d": Color.fromARGB(255, 255, 181, 71),
    "02d": Color.fromARGB(255, 190, 229, 248),
    "03d": Color.fromARGB(255, 137, 208, 240),
    "04d": Color.fromARGB(255, 174, 174, 174),
    "09d": const Color.fromARGB(255, 212, 212, 212),
    "10d": Color.fromARGB(255, 95, 95, 95),
    "11d": const Color.fromARGB(255, 81, 81, 81),
    "13d": const Color.fromARGB(255, 255, 255, 255),
    "50d": Color.fromARGB(255, 255, 255, 202),
    // Mapeamentos de cores...
  };

  Map<String, String> descriptionTranslations = {
     "01d": "Céu limpo",
    "02d": "Poucas nuvens",
    "03d": "Nuvens dispersas",
    "04d": "Nuvens quebradas",
    "09d": "Chuva isolada",
    "10d": "Chuva",
    "11d": "Tempestade",
    "13d": "Neve",
    "50d": "Nevoa",
    // Mapeamentos de descrições...
  };

  @override
  void initState() {
    super.initState();
    fetchCitiesInBrazil(); // Buscar cidades brasileiras ao iniciar
  }

  Future<void> fetchCitiesInBrazil() async {
    final response = await http.get(Uri.parse('https://servicodados.ibge.gov.br/api/v1/localidades/municipios'));

    if (response.statusCode == 200) {
      final List<dynamic> data = json.decode(response.body);
      setState(() {
        citiesInBrazil = data.map((item) => item['nome']).cast<String>().toList();
        selectedCity = citiesInBrazil.isNotEmpty ? citiesInBrazil[0] : '';
        fetchWeatherData(selectedCity); // Buscar dados climáticos da primeira cidade
      });
    } else {
      print('Falha ao buscar cidades. Código de status: ${response.statusCode}');
    }
  }
  
  Future<void> fetchCitiesInState(String state) async {
    final response = await http.get(Uri.parse('https://servicodados.ibge.gov.br/api/v1/localidades/estados/$state/municipios'));

    if (response.statusCode == 200) {
      final List<dynamic> data = json.decode(response.body);
      setState(() {
        citiesInState = data.map((item) => item['nome']).cast<String>().toList();
        selectedCity = citiesInState.isNotEmpty ? citiesInState[0] : '';
        fetchWeatherData(selectedCity); // Buscar dados climáticos da primeira cidade no estado
      });
    } else {
      print('Falha ao buscar cidades. Código de status: ${response.statusCode}');
    }
  }

  Future<void> fetchWeatherData(String cityName) async {
    final response = await http.get(
        Uri.parse('https://api.openweathermap.org/data/2.5/weather?q=$cityName&appid=808e2a076233f96cafbb5a45abac9f83'));

    if (response.statusCode == 200) {
      final Map<String, dynamic> data = json.decode(response.body);
      setState(() {
        weatherData = WeatherData.fromJson(data);

        String iconCode = weatherData!.iconCode;
        weatherData!.description = descriptionTranslations[iconCode] ?? 'Descrição não disponível';
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    Color? backgroundColor = Colors.white; // Cor de fundo padrão

    if (weatherData != null) {
      backgroundColor = weatherColorMap[weatherData!.iconCode] ?? Colors.white;
    }

    return Scaffold(
      appBar: AppBar(
        title: Text('Meteorologia'),
      ),
      backgroundColor: backgroundColor,
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            DropdownButton<String>(
              value: selectedState,
              onChanged: (newValue) {
                setState(() {
                  selectedState = newValue!;
                  // Atualize a lista de cidades com base no estado selecionado
                  citiesInState = [];
                  fetchCitiesInState(selectedState); // Buscar cidades para o estado selecionado
                });
              },
              items: states
                  .map<DropdownMenuItem<String>>((String value) {
                return DropdownMenuItem<String>(
                  value: value,
                  child: Text(value),
                );
              }).toList(),
            ),
            SizedBox(height: 16),
            DropdownButton<String>(
              value: selectedCity,
              onChanged: (newValue) {
                setState(() {
                  selectedCity = newValue!;
                  fetchWeatherData(selectedCity);
                });
              },
              items: citiesInState
                  .map<DropdownMenuItem<String>>((String value) {
                return DropdownMenuItem<String>(
                  value: value,
                  child: Text(value),
                );
              }).toList(),
            ),
            SizedBox(height: 16),
            weatherData != null
                ? Column(
                    children: [
                      Text(
                        weatherData!.cityName,
                        style: TextStyle(fontSize: 24),
                      ),
                      SizedBox(height: 16),
                      Icon(
                        weatherIconMap[weatherData!.iconCode] ?? WeatherIcons.na,
                        size: 48,
                      ),
                      SizedBox(height: 16),
                      Text(
                        '${weatherData!.temperature.toStringAsFixed(1)}°C',
                        style: TextStyle(fontSize: 48),
                      ),
                      SizedBox(height: 16),
                      Text(
                        weatherData!.description,
                        style: TextStyle(fontSize: 18),
                      ),
                    ],
                  )
                : CircularProgressIndicator(),
          ],
        ),
      ),
    );
  }
}