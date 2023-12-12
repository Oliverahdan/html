import 'package:flutter/material.dart';
import 'package:flutter_bluetooth_serial/flutter_bluetooth_serial.dart';
import 'dart:convert';



void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Bluetooth Control',
      home: BluetoothControlScreen(),
    );
  }
}

class BluetoothControlScreen extends StatefulWidget {
  @override
  _BluetoothControlScreenState createState() => _BluetoothControlScreenState();
}

class _BluetoothControlScreenState extends State<BluetoothControlScreen> {
  BluetoothConnection? _connection;
  bool _isConnected = false;
  FlutterBluetoothSerial _bluetooth = FlutterBluetoothSerial.instance;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Bluetooth Control'),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            _isConnected
                ? Text('Conectado ao dispositivo Bluetooth')
                : ElevatedButton(
                    onPressed: _connectToDevice,
                    child: Text('Conectar ao dispositivo Bluetooth'),
                  ),
            SizedBox(height: 20),
            ElevatedButton(
              onPressed: _isConnected ? _sendSignals : null,
              child: Text('Enviar Sinais'),
            ),
          ],
        ),
      ),
    );
  }

  Future<void> _connectToDevice() async {
    BluetoothDevice selectedDevice;
    List<BluetoothDevice> devices = [];

    try {
      devices = await _bluetooth.getBondedDevices();
    } catch (e) {
      print(e);
    }

    if (devices.isEmpty) {
      return;
    }

    selectedDevice = devices.first;
    BluetoothConnection connection = await BluetoothConnection.toAddress(selectedDevice.address);
    setState(() {
      _connection = connection;
      _isConnected = true;
    });
  }

  Future<void> _sendSignals() async {
    if (_connection == null) return;

    try {
      await _connection!.output.add(utf8.encode('Sinal Verde'));
      await _connection!.output.allSent;

      await Future.delayed(Duration(seconds: 5));

      await _connection!.output.add(utf8.encode('Sinal Piscando'));
      await _connection!.output.allSent;

      await Future.delayed(Duration(seconds: 5));

      await _connection!.output.add(utf8.encode('Sinal Vermelho'));
      await _connection!.output.allSent;
    } catch (e) {
      print(e);
    }
  }

  @override
  void dispose() {
    _connection?.close();
    super.dispose();
  }
}
