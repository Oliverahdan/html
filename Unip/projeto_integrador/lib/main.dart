import 'dart:async';
import 'package:flutter/material.dart';

void main() {
  runApp(LoadingScreen());
}

class LoadingScreen extends StatefulWidget {
  @override
  _LoadingScreenState createState() => _LoadingScreenState();
}

class _LoadingScreenState extends State<LoadingScreen> {
  bool _showImage = true;
  late Timer _blinkTimer;

  @override
  void initState() {
    super.initState();
    _startBlinking();
  }

  void _startBlinking() {
    _blinkTimer = Timer.periodic(Duration(seconds: 1), (timer) {
      if (!mounted) {
        _blinkTimer.cancel(); // Cancela o temporizador se o widget não estiver mais no widget tree
        return;
      }
      setState(() {
        _showImage = !_showImage;
      });
    });

    Timer(Duration(seconds: 3), () {
      if (!mounted) {
        return; // Evita chamar runApp se o widget não estiver mais no widget tree
      }
      runApp(MyApp());
    });
  }

  @override
  void dispose() {
    _blinkTimer.cancel(); // Cancela o temporizador ao descartar o widget
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        backgroundColor: Color(0xFFFCD167),
        body: Center(
          child: AnimatedOpacity(
            opacity: _showImage ? 1.0 : 0.0,
            duration: Duration(milliseconds: 500),
            child: Image.asset(
              'assets/2.png', // Altere para o caminho da imagem no seu projeto
              width: 400, // Altere o tamanho da imagem conforme necessário
              height: 400,
            ),
          ),
        ),
      ),
    );
  }
}


class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Welcome Page',
      home: WelcomePage(),
    );
  }
}

class WelcomePage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Color.fromARGB(255, 255, 255, 255),
      appBar: AppBar(
        backgroundColor: Color(0xFFFCD167),
        toolbarHeight: 60, // Altura do cabeçalho
        title: Text('Bem Vindo(a)', style: TextStyle(color: Colors.black)),
        actions: [
          Padding(
            padding: EdgeInsets.only(right: 16.0),
            child: Image.asset(
              'assets/2.png', // Caminho da imagem
              width: 60, // Ajuste o tamanho da imagem conforme necessário
              height: 60,
            ),
          ),
        ],
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            CustomContainer(title: 'Estudos', imageAsset: 'assets/estudos.png'),
            SizedBox(height: 20),
            CustomContainer(title: 'Reuniões', imageAsset: 'assets/reunioes.png'),
            SizedBox(height: 20),
            CustomContainer(title: 'Alarmes', imageAsset: 'assets/alarmes.png'),
          ],
        ),
      ),
    );
  }
}

class CustomContainer extends StatelessWidget {
  final String title;
  final String imageAsset;

  CustomContainer({required this.title, required this.imageAsset});

  @override
  Widget build(BuildContext context) {
    return Container(
      width: 200,
      height: 100,
      decoration: BoxDecoration(
        color: Color(0xFFEA86BF),
        borderRadius: BorderRadius.circular(20),
      ),
      child: Row(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Image.asset(
            imageAsset,
            width: 40, // Ajuste o tamanho da imagem conforme necessário
            height: 40,
          ),
          SizedBox(width: 10),
          Text(
            title,
            style: TextStyle(
              color: Colors.white,
              fontSize: 20,
              fontWeight: FontWeight.bold,
            ),
          ),
        ],
      ),
    );
  }
}
