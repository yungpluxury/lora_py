import serial;
import requests;
import json;
serialPort=serial.Serial(port='COM4',baudrate=115200);
while True:
    print("");
    data=serialPort.readline().decode('CP866');
    jsonPart=json.dumps({"data": data});
    req = requests.post('http://172.16.117.193:80/gettingData', headers={'Content-Type': 'application/json'}, data=jsonPart);
    print(data);
    print (req.text);
serialPort.close();