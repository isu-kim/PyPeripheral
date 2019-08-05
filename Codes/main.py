from Wrappers import Corsair
from Wrappers import Razer
import time
import random
from Wrappers.cue_sdk import *


Corsair.RequestControl()
Corsair.debugOFF()

RazerURI = Razer.geturi()
Razer.debugOFF()




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
    while True:
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


def randomColors():
    while True:
        for i in range(200):
            Corsair.ledOn(i , random.randrange(1,256) , random.randrange(1,256) , random.randrange(1,256) , 0.0001)
            Razer.setEffect(Razer.createMouseEffect("CHROMA_STATIC" , random.randrange(1,256) ,random.randrange(1,256) ,random.randrange(1,256) , RazerURI),RazerURI)

RainBowAll(10)
