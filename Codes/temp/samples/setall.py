from Wrappers import Corsair
from Wrappers import Razer
from threading import Thread
from Wrappers import requests
import time
from Wrappers.cue_sdk import *




#Corsair.debugON()
#Corsair.FirstInit()

#print(Corsair.DeviceInfo())
#print(Corsair.DeviceList)
#print(Corsair. DeviceID(Corsair.DeviceList))

#Corsair.FirstInit()

#print(Corsair.DeviceInfo())
#Corsair.FirstInit()

Corsair.debugON()
Corsair.FirstInit()

RazerURI = Razer.geturi()
Razer.debugON()

def p1():
    while True:
        for i in range(170, 188, 1):

            Corsair.ledOn(i, 0, 255, 0, 0.01)
            Corsair.ledOn(i + 1, 0, 255, 0, 0.01)

        for i in range(170, 188, 1):
            Corsair.ledOn(i, 0, 0, 0, 0.01)
            Corsair.ledOn(i + 1, 0, 0, 0, 0.01)

        for i in range(188, 170, -1):
            Corsair.ledOn(i, 0, 255, 0, 0.01)
            Corsair.ledOn(i + 1, 0, 255, 0, 0.01)

        for i in range(188, 170, -1):
            Corsair.ledOn(i, 0, 0, 0, 0.01)
            Corsair.ledOn(i + 1, 0, 0, 0, 0.01)



def p2():
    while True:
        Effectid = Razer.createMouseEffect("CHROMA_STATIC" , 255, 0 , 0 , RazerURI)
        Razer.setEffect(Effectid , RazerURI)
        time.sleep(1)
        Effectid = Razer.createMouseEffect("CHROMA_STATIC" , 0, 255 , 0 , RazerURI)
        time.sleep(1)
        Razer.setEffect(Effectid , RazerURI)
        Effectid = Razer.createMouseEffect("CHROMA_STATIC" , 0, 0 , 255 , RazerURI)
        time.sleep(1)
        Razer.setEffect(Effectid , RazerURI)

def setall(r,g,b):
    for i in range(200):
        Corsair.ledOn(i , r,g,b,0.00001)
    Effectid = Razer.createMouseEffect("CHROMA_STATIC", r, g, b, RazerURI)
    Razer.setEffect(Effectid, RazerURI)


while True:
    setall(255 , 0 , 0 )
    setall(0 , 255 , 0 )
    setall(0 , 0 , 255 )
