import 'dart:math' as math;
import 'package:flutter/material.dart';
import 'package:flutter_compass/flutter_compass.dart';
import 'package:geolocator/geolocator.dart';
import 'package:permission_handler/permission_handler.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Compass and Proximity Example',
      home: CompassScreen(),
    );
  }
}

class CompassScreen extends StatefulWidget {
  @override
  _CompassScreenState createState() => _CompassScreenState();
}

class _CompassScreenState extends State<CompassScreen> {
  double _direction = 0.0;
  String _proximity = 'Desconhecida';

  String _getDirection(double heading) {
    if (heading >= 45 && heading < 135) {
      return 'Leste';
    } else if (heading >= 135 && heading < 225) {
      return 'Sul';
    } else if (heading >= 225 && heading < 315) {
      return 'Oeste';
    } else {
      return 'Norte';
    }
  }

  Future<void> _getProximity() async {
    // Verifique e solicite permissão de localização se necessário
    var status = await Permission.location.request();
    
    if (status.isGranted) {
      Position position = await Geolocator.getCurrentPosition(
        desiredAccuracy: LocationAccuracy.best,
      );

      // Coordenadas do ponto 1 (Rua)
      final double lat1 = -20.1461411809263;
      final double lon1 = -44.889972614422454;

      // Coordenadas do ponto 2 (Sua posição atual)
      final double lat2 = position.latitude;
      final double lon2 = position.longitude;

      // Fórmula Haversine para calcular a distância entre dois pontos
      final double radius = 6371; // Raio da Terra em quilômetros
      final double dLat = _degToRad(lat2 - lat1);
      final double dLon = _degToRad(lon2 - lon1);
      final double a = (math.sin(dLat / 2) * math.sin(dLat / 2)) +
          (math.cos(_degToRad(lat1)) * math.cos(_degToRad(lat2)) *
              math.sin(dLon / 2) *
              math.sin(dLon / 2));
      final double c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a));
      final double distance = radius * c;

      if (distance < 0.1) {
        // Você está a menos de 100 metros da rua (ajuste conforme necessário)
        setState(() {
          _proximity = 'Perto da rua';
        });
      } else {
        setState(() {
          _proximity = 'Longe da rua';
        });
      }
    } else {
      // O usuário negou a permissão, você pode mostrar uma mensagem ou pedir novamente.
      setState(() {
        _proximity = 'Permissão de localização negada';
      });
    }
  }

  double _degToRad(double deg) {
    return deg * (math.pi / 180);
  }

  @override
  void initState() {
    super.initState();
    FlutterCompass.events?.listen((event) {
      setState(() {
        _direction = event.heading ?? 0.0;
      });
    });

    _getProximity();
  }

  @override
  Widget build(BuildContext context) {
    String directionText = _getDirection(_direction);

    return Scaffold(
      appBar: AppBar(
        title: Text('Compass and Proximity Example'),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Text('Direção: $directionText'),
            Text('Proximidade: $_proximity'),
          ],
        ),
      ),
    );
  }
}
