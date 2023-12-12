import 'package:flutter/material.dart';
import 'package:flutter_blue/flutter_blue.dart';

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
  final String _targetDeviceName = "HC-05";
  final String _targetDevicePassword = "1234";

  BluetoothDevice? _device;
  BluetoothCharacteristic? _characteristic;
  bool _isConnected = false;

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
                ? Text('Conectado ao dispositivo: ${_device?.name}')
                : ElevatedButton(
                    onPressed: _connectToDevice,
                    child: Text('Conectar ao dispositivo'),
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
    FlutterBlue flutterBlue = FlutterBlue.instance;
    List<ScanResult> scanResults = await flutterBlue.scan(timeout: Duration(seconds: 5));

    for (var result in scanResults) {
      if (result.device.name == _targetDeviceName) {
        _device = result.device;
        await _device!.connect();
        List<BluetoothService> services = await _device!.discoverServices();
        for (var service in services) {
          for (var characteristic in service.characteristics) {
            if (characteristic.properties.write) {
              _characteristic = characteristic;
              break;
            }
          }
        }
        setState(() {
          _isConnected = true;
        });
        break;
      }
    }
  }

  Future<void> _sendSignals() async {
    if (_characteristic == null) return;

    await _characteristic!.write(utf8.encode('Sinal Verde'));
    await Future.delayed(Duration(seconds: 5));
    await _characteristic!.write(utf8.encode('Sinal Piscando'));
    await Future.delayed(Duration(seconds: 5));
    await _characteristic!.write(utf8.encode('Sinal Vermelho'));
  }

  @override
  void dispose() {
    _device?.disconnect();
    super.dispose();
  }
}
