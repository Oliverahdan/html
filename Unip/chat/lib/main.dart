import 'package:flutter/material.dart';
import 'package:flutter_local_notifications/flutter_local_notifications.dart';
import 'package:timezone/data/latest.dart' as tz;
import 'package:timezone/timezone.dart' as tz;

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  tz.initializeTimeZones();

  await initLocalNotifications();
  runApp(MyApp());
}

Future<void> initLocalNotifications() async {
  final FlutterLocalNotificationsPlugin flutterLocalNotificationsPlugin = FlutterLocalNotificationsPlugin();
  const AndroidInitializationSettings initializationSettingsAndroid = AndroidInitializationSettings('app_icon');
  final InitializationSettings initializationSettings = InitializationSettings(
    android: initializationSettingsAndroid,
  );
  await flutterLocalNotificationsPlugin.initialize(initializationSettings);
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Lembretes',
      home: ReminderScreen(),
    );
  }
}

class ReminderScreen extends StatefulWidget {
  @override
  _ReminderScreenState createState() => _ReminderScreenState();
}

class _ReminderScreenState extends State<ReminderScreen> {
  final TextEditingController _nameController = TextEditingController();
  final TextEditingController _messageController = TextEditingController();
  int _selectedHour = 0;
  int _selectedMinute = 0;

  late tz.Location _local; // Declare _local como late

  @override
  void initState() {
    super.initState();
    _local = tz.local; // Inicialize _local no initState
  }

  Future<void> _scheduleNotification() async {
    final FlutterLocalNotificationsPlugin flutterLocalNotificationsPlugin = FlutterLocalNotificationsPlugin();

    final int notificationId = DateTime.now().millisecondsSinceEpoch ~/ 1000;

    // Calcular a data e hora de agendamento
    final now = DateTime.now();
    final scheduledTime = tz.TZDateTime(
      _local,
      now.year,
      now.month,
      now.day,
      _selectedHour,
      _selectedMinute,
    );

    // Certifique-se de que a data e hora agendadas estão no futuro
    if (scheduledTime.isBefore(tz.TZDateTime.now(_local))) {
      showDialog(
        context: context,
        builder: (BuildContext context) {
          return AlertDialog(
            title: Text('Erro'),
            content: Text('Selecione uma hora futura para o lembrete.'),
            actions: [
              TextButton(
                onPressed: () => Navigator.of(context).pop(),
                child: Text('Ok'),
              ),
            ],
          );
        },
      );
      return;
    }

    // ignore: prefer_const_constructors
    final AndroidNotificationDetails androidPlatformChannelSpecifics = AndroidNotificationDetails(
      'channel_id',
      'Lembrete',
      importance: Importance.max,
      priority: Priority.high,
      icon: 'app_icon',
      largeIcon: DrawableResourceAndroidBitmap('app_icon'),
    );

    final NotificationDetails platformChannelSpecifics = NotificationDetails(
      android: androidPlatformChannelSpecifics,
    );

    await flutterLocalNotificationsPlugin.zonedSchedule(
      notificationId,
      'Lembrete: ${_nameController.text}',
      _messageController.text,
      scheduledTime,
      platformChannelSpecifics,
      androidAllowWhileIdle: true,
      uiLocalNotificationDateInterpretation: UILocalNotificationDateInterpretation.absoluteTime,
    );

    _nameController.clear();
    _messageController.clear();

    showDialog(
      context: context,
      builder: (BuildContext context) {
        return AlertDialog(
          title: Text('Lembrete Agendado'),
          content: Text('Seu lembrete foi agendado com sucesso.'),
          actions: [
            TextButton(
              onPressed: () => Navigator.of(context).pop(),
              child: Text('Ok'),
            ),
          ],
        );
      },
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Lembrete'),
      ),
      body: Padding(
        padding: EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: <Widget>[
            TextField(
              controller: _nameController,
              decoration: InputDecoration(labelText: 'Nome do Lembrete'),
            ),
            TextField(
              controller: _messageController,
              decoration: InputDecoration(labelText: 'Mensagem'),
            ),
            Row(
              children: <Widget>[
                Text('Horário do Lembrete:'),
                SizedBox(width: 16.0),
                DropdownButton<int>(
                  value: _selectedHour,
                  onChanged: (int? value) {
                    setState(() {
                      _selectedHour = value!;
                    });
                  },
                  items: List<int>.generate(24, (int index) => index)
                      .map<DropdownMenuItem<int>>(
                        (int value) => DropdownMenuItem<int>(
                          value: value,
                          child: Text(value.toString().padLeft(2, '0')),
                        ),
                      )
                      .toList(),
                ),
                Text(':'),
                DropdownButton<int>(
                  value: _selectedMinute,
                  onChanged: (int? value) {
                    setState(() {
                      _selectedMinute = value!;
                    });
                  },
                  items: List<int>.generate(60, (int index) => index)
                      .map<DropdownMenuItem<int>>(
                        (int value) => DropdownMenuItem<int>(
                          value: value,
                          child: Text(value.toString().padLeft(2, '0')),
                        ),
                      )
                      .toList(),
                ),
              ],
            ),
            ElevatedButton(
              onPressed: _scheduleNotification,
              child: Text('Agendar Lembrete'),
            ),
          ],
        ),
      ),
    );
  }

  @override
  void dispose() {
    _nameController.dispose();
    _messageController.dispose();
    super.dispose();
  }
}
