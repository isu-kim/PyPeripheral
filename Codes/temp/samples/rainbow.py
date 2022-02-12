from Wrappers import Corsair
from Wrappers import Razer
import time
from Wrappers.cue_sdk import *


Corsair.RequestControl()
Corsair.debugON()

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


def prints():
    for i in range(200):
        print("Thread(target = Corsair.ledOn(" + str(i) + ", r , g , b ,duration)).start()")


def setEveryDeviceColor(r,g,b,duration):
    Corsair.KeyboardSetdAll(r, g, b, duration)
    Corsair.MM800SetAll(r, g, b, duration)
    Razer.setEffect(Razer.createMouseEffect("CHROMA_STATIC", r, g, b, RazerURI), RazerURI)
    Corsair.ledOn(CLK.GLAV_2, r, g, b, duration)
    Corsair.ledOn(CLK.GLAV_1, r, g, b, duration)
    Corsair.ledOn(CLK.GLAV_3, r, g, b, duration)
    Corsair.ledOn(CLK.VOIDPRO_R, r, g, b, duration)
    Corsair.ledOn(CLK.VOIDPRO_L, r, g, b, duration)
    # duration == 0.001 is ideal


def RainBowAll(step): # how fast the rainbow should be changed.
    for g in range(0,255,step):
        #Corsair.KeyboardSetdAll(255, g, 0, 0.001)
        setEveryDeviceColor(255,g,0,0.001)

    for r in range(255 , 0 , -step):
        #Corsair.KeyboardSetdAll(r,255,0,0.001)
        setEveryDeviceColor(r,255,0,0.001)

    for b in range(0,255,step):
        #Corsair.KeyboardSetdAll(0,255,b,0.001)
        setEveryDeviceColor(0,255,b,0.001)

    for g in range(255 , 0 , -step):
        #Corsair.KeyboardSetdAll(0,g,255,0.001)
        setEveryDeviceColor(0,g,255,0.001)

    for r in range(0,255,step):
        #Corsair.KeyboardSetdAll(r,0,255,0.001)
        setEveryDeviceColor(r,0,255,0.001)

    for b in range(255 , 0 , -step):
        #Corsair.KeyboardSetdAll(255,0,b,0.001)
        setEveryDeviceColor(255,0,b,0.001)



RainBowAll(30)
