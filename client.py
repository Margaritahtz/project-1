from http.client import REQUESTED_RANGE_NOT_SATISFIABLE
import json
#import requests
#import redis
import websocket
import asyncio
import serial
from serial import Serial
import random, time

ws= websocket.WebSocket()


ws.connect('ws://localhost:8000/ws/polData/')


#count=0
#x=[]
#y=[]
#ser = serial.Serial('COM7',115200)
#ser.close()
#ser.open()
#while True:

    #data = ser.readline()
    #data.decode('utf-8')
    #value=str(data.decode('utf-8'))
    #print(value)

    #time.sleep(3)

    #ws.send(json.dumps({'value':value}))










for i in range(1000):
    time.sleep(3)

    ws.send(json.dumps({'value': random.randint(1,1000)}))

