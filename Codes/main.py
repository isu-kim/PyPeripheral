from Wrappers import Corsair
from Wrappers import Razer
from Communications import ServerSide
from pathlib import Path
from time import sleep
from threading import Thread


import random
from Wrappers.cue_sdk import *

global RazerURI


global server
server = False



class DEVLIST:
#Device List in main function for init
    def __init__(self):
        self.keyboard = None
        self.mouse = None
        self.mousepad = None
        self.headset = None
        self.etc = None
        self.sdks = []


class SDKS:
    def __init__(self):
        self.Razer = None
        self.Corsair = None
        self.RazerMouse = None
        self.RazerKeybd = None
        self.RazerMousePD = None
        self.RazerHeadSet = None
        self.RazerETC = None
        self.CorsairMouse = None
        self.CorsairKeybd = None
        self.CorsairMousePD = None
        self.CorsairHeadSet = None
        self.CorsairETC = None


class TEST:
    '''
    This class includes some of simple testing scripts whether the program is successfully working
    White_Out will set all device color to white, and wait 3sec.
    RainBowAll will set all device color into rainbow shaped. this will loop forever.
    '''

    def White_Out(self):
        for i in range(300):
            SetAllColor(255, 255, 255, 0)
            sleep(0.001)

    def RainBowAll(self):
        RainBowAll(100)

    def randomColors(self):
        while True:
            color = setCOLOR()
            color.mouse(random.randrange(1, 256), random.randrange(1, 256), random.randrange(1, 256),RazerURI,0)
            color.keyboard(random.randrange(1, 256), random.randrange(1, 256), random.randrange(1, 256),RazerURI,0)
            color.mousepad(random.randrange(1, 256), random.randrange(1, 256), random.randrange(1, 256),RazerURI,0)
            color.headset(random.randrange(1, 256), random.randrange(1, 256), random.randrange(1, 256),RazerURI,0)
            color.etc(random.randrange(1, 256), random.randrange(1, 256), random.randrange(1, 256),RazerURI,0)



class setCOLOR:
    '''
    This class is for setting colors regardless of the sdks.
    for example, setCOLOR.mouse will set ALL connected mouse color into just one color.
    If you wish to control individually, please import files from Wrappers directory.
    Direct Control should be in this way : Corsair.ledOn(CLK.GLAV_1, 255, 255, 255, 0)

    Also, If you wish to set all the device color instantly with out any delay, please set duration as 0
    Otherwise, the lighting would be in wave shape. There would be at least delays between leds.
    '''
    def mouse(self, r, g, b, RazerURI, Duration):
        if SDKS.RazerMouse:
            EffectID = Razer.createMouseEffect("CHROMA_STATIC" ,r ,g ,b, RazerURI)
            Razer.setEffect(EffectID, RazerURI)

        if SDKS.CorsairMouse:
            Corsair.ledOn(CLK.GLAV_1, r, g, b, Duration)
            Corsair.ledOn(CLK.GLAV_2, r, g, b, Duration)
            Corsair.ledOn(CLK.GLAV_3, r, g, b, Duration)

    def keyboard(self, r, g, b, RazerURI, Duration):
        if SDKS.RazerKeybd:
            EffectID = Razer.createKeyboardEffect("CHROMA_STATIC", r, g, b, RazerURI)
            Razer.setEffect(EffectID, RazerURI)

        if SDKS.CorsairKeybd:

            exceptList = [148 , 149 , 150 , 151 , #Mouse
                          189 , 148 , 149 , #Mouse
                          155 , 156 , 157 , 158 , 159 , 160 , 161 , 162 , 163, 164, 165, 166 , 167 , 168 , 169, #mousepad
                          152 , 153 #HeadSet
                          ]

            for i in range(200):
                if i not in exceptList:
                    Corsair.ledOn(i , r, g, b, Duration)

    def mousepad(self, r, g, b, RazerURI, Duration):
        if SDKS.RazerMousePD:
            EffectID = Razer.createMousePadEffect("CHROMA_STATIC", r, g, b, RazerURI)
            Razer.setEffect(EffectID, RazerURI)

        if SDKS.CorsairMousePD:
            for i in range (155,170,1):
                Corsair.ledOn(i, r, g, b, Duration)

    def headset(self, r, g, b, RazerURI, Duration):
        if SDKS.CorsairHeadSet:
            Corsair.ledOn(CLK.VOIDPRO_R, r, g, b, Duration)
            Corsair.ledOn(CLK.VOIDPRO_L, r, g, b, Duration)

        if SDKS.RazerHeadSet:
            EffectID = Razer.createHeadsetEffect("CHROMA_STATIC", r, g, b, RazerURI)
            Razer.setEffect(EffectID, RazerURI)

    def etc(self, r, g, b, RazerURI, Duration):
        if SDKS.RazerETC:
            EffectID = Razer.createETCEffect("CHROMA_STATIC" , r, g, b, RazerURI)
            Razer.setEffect(EffectID, RazerURI)

        if SDKS.CorsairETC:
            for i in range(500): # I do not know the maximum number. So, this might not be a optimal one.
                Corsair.ledOn(i, r, g, b, Duration)

class Config:
    '''
    This class is for config files.
    config write would read the config files and store the information inside config to a class called DEVLIST.
    If you wish to use my program as it is, do not touch this part.
    '''
    def write(self):
        f = open("Config.txt", "w")
        f.write("#PyPheperial Config File\n")
        f.write("#Please DO NOT change anything from this file unless you know how it works.\n")
        f.write("#If you wish to change devices, delete this config. The software would generate a new one for you.\n")

        # This file would save the info with this type
        # Example
        # MOUSE=RAZER,CORSAIR
        # KEYBOARD=CORSAIR
        # MOUSEPAD=CORSAIR
        # HEADSET=CORSAIR
        # ETC=CORSAIR

        print("[INFO] Please tell us your spec")
        print("[INFO] If you have more than one devices per category, use it with comma")
        print("[INFO] Type in \"None\" for no Device")
        print("[INFO] ex) RAZER,CORSAIR")

        mouse = input("[INFO] Mouse : ")
        keyboard = input("[INFO] Keyboard : ")
        mousepad = input("[INFO] Mouse Pad : ")
        headset = input("[INFO] Headset : ")
        etc = input("[INFO] ETC : ")

        f.write("MOUSE=" + str(mouse) + "\n")
        f.write("KEYBOARD=" + str(keyboard) + "\n")
        f.write("MOUSEPAD=" + str(mousepad) + "\n")
        f.write("HEADSET=" + str(headset) + "\n")
        f.write("ETC=" + str(etc) + "\n")
        f.write("EOF\n")

        f.close()

        print("[INFO] Thank you! Configuration Done. Now setting up some things for real action.")

    def read(self):
        global mainDebug
        f = open("Config.txt", "r")
        lines = f.readlines()
        # Line 3 : Mouse / 4 : Keyboard / 5 : Mousepad / 6 : Headset / 7 : ETC

        MOUSE = [x.strip() for x in lines[3].replace("MOUSE=", "").split(',')]
        if mainDebug:
            print("[DEBUG] Mouse : ", end="")
            print(MOUSE)

        KEYBOARD = [x.strip() for x in lines[4].replace("KEYBOARD=", "").split(',')]
        if mainDebug:
            print("[DEBUG] Keyboard : ", end="")
            print(KEYBOARD)

        MOUSEPAD = [x.strip() for x in lines[5].replace("MOUSEPAD=", "").split(',')]
        if mainDebug:
            print("[DEBUG] Mouse Pad : ", end="")
            print(MOUSEPAD)

        HEADSET = [x.strip() for x in lines[6].replace("HEADSET=", "").split(',')]
        if mainDebug:
            print("[DEBUG] Head Set : ", end="")
            print(HEADSET)

        ETC = [x.strip() for x in lines[7].replace("ETC=", "").split(',')]
        if mainDebug:
            print("[DEBUG] ETC : ", end="")
            print(ETC)

        DEVLIST.mouse = MOUSE
        DEVLIST.keyboard = KEYBOARD
        DEVLIST.mousepad = MOUSEPAD
        DEVLIST.headset = HEADSET
        DEVLIST.etc = ETC

        return DEVLIST

class Debug:
    '''
    This class is for debugging. debug.ON and debug.OFF would just effect all the debugs just in main.py.
    If you wish to use all the debugs in all the SDKs, please use debug.AllON
    If you wish to use them individually, please refer to the individual SDK Wrapper files in the project. or use the function in this class.
    '''
    def __init__(self):
        global mainDebug
        mainDebug = False
        Corsair.debugOFF()
        Razer.debugOFF()

    def ON(self):
        global mainDebug
        mainDebug = True

    def OFF(self):
        global mainDebug
        mainDebug = False
        Corsair.debugOFF()
        Razer.debugOFF()

    def AllON(self):
        global mainDebug
        mainDebug = True
        Corsair.debugON()
        Razer.debugON()

    def Corsair(self):
        Corsair.debugON()

    def Razer(self):
        Razer.debugON()

class SDKops:
    '''
    This class is for SDK information.
    This class finds out all the information regarding your device written in Config file, and decide which one to use.
    All the functions in this class uses SDKS class which contains boolean values for each devices.
    '''
    def SDKtypes(self, DEVLIST):
        dump = []

        for i in range(len(DEVLIST.mouse)):
            dump.append(DEVLIST.mouse[i])

        for i in range(len(DEVLIST.keyboard)):
            dump.append(DEVLIST.keyboard[i])

        for i in range(len(DEVLIST.mousepad)):
            dump.append(DEVLIST.mousepad[i])

        for i in range(len(DEVLIST.etc)):
            dump.append(DEVLIST.etc[i])

        for i in range(len(DEVLIST.headset)):
            dump.append(DEVLIST.headset[i])

        if mainDebug:
            print(dump)
            print(len(list(dict.fromkeys(dump))))
            print(list(dict.fromkeys(dump)))

        DEVLIST.sdks = list(dict.fromkeys(dump))

    def clearSDK(self):
        SDKS.Razer = False
        SDKS.RazerMouse = False
        SDKS.RazerKeybd = False
        SDKS.RazerHeadSet = False
        SDKS.RazerMousePD = False
        SDKS.RazerETC = False

        SDKS.Corsair = False
        SDKS.CorsairMouse = False
        SDKS.CorsairKeybd = False
        SDKS.CorsairMousePD = False
        SDKS.CorsairHeadSet = False
        SDKS.CorsairETC = False

    def SDKInits(self, DEVLIST):
        global RazerURI
        ops = SDKops()

        ops.clearSDK()
        ops.SDKtypes(DEVLIST)

        if mainDebug:
            print(DEVLIST.sdks)

        if "RAZER" in DEVLIST.sdks:
            print("[INFO] RAZER Device Found. Initiating SDK")
            RazerURI = Razer.geturi()
            SDKS.Razer = True

            if "RAZER" in DEVLIST.mouse:
                SDKS.RazerMouse = True

            if "RAZER" in DEVLIST.headset:
                SDKS.RazerHeadSet = True

            if "RAZER" in DEVLIST.keyboard:
                SDKS.RazerKeybd = True

            if "RAZER" in DEVLIST.mousepad:
                SDKS.RazerMousePD = True

            if "RAZER" in DEVLIST.etc:
                SDKS.RazerETC = True

        if "CORSAIR" in DEVLIST.sdks:
            print("[INFO] CORSAIR Device Found. Requesting Control")
            Corsair.RequestControl()
            SDKS.Corsair = True

            if "CORSAIR" in DEVLIST.mouse:
                SDKS.CorsairMouse = True

            if "CORSAIR" in DEVLIST.headset:
                SDKS.CorsairHeadSet = True

            if "CORSAIR" in DEVLIST.keyboard:
                SDKS.CorsairKeybd = True

            if "CORSAIR" in DEVLIST.mousepad:
                SDKS.CorsairMousePD = True

            if "CORSAIR" in DEVLIST.etc:
                SDKS.CorsairETC = True

        else:
            print("[ERROR] Sorry, Only Razer and Corsair devices are supported right now. ")
            return

        if mainDebug:
            print(vars(SDKS))

'''
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
    
#DO NOT USE THIS FUNCTION AT ALL.
'''

class GlowKeys:
    '''
    This class is for "Glowing" keys. This would smoothly turn the keys on light.
    "step" parameter is for how rapidly the light should turn. The higher parameter is, the smoother keys will glow. However it will turn on slowly.
    "duration" parameter is for how much seconds shall it be stopped between those loops. The higher parameter is, the slower keys glow.
    '''
    def mouse(self,r,g,b,step,duration):
        etc = ETCfuncs()
        color = setCOLOR()

        for x in etc.range_float(0, 2, step):
            NRval = int((1 - abs(x - 1)) * r)
            NGval = int((1 - abs(x - 1)) * g)
            NBval = int((1 - abs(x - 1)) * b)
            color.mouse(NRval, NGval, NBval, RazerURI, 0)
            sleep(duration)

        if mainDebug:
            print("[INFO] Glow mouse set : " + str(r) + "," + str(g) + "," + str(b) + " ")

    def keyboard(self,r,g,b,step,duration):
        etc = ETCfuncs()
        color = setCOLOR()

        for x in etc.range_float(0, 2, step):
            NRval = int((1 - abs(x - 1)) * r)
            NGval = int((1 - abs(x - 1)) * g)
            NBval = int((1 - abs(x - 1)) * b)
            color.keyboard(NRval, NGval, NBval, RazerURI, 0)
            sleep(duration)

        if mainDebug:
            print("[INFO] Glow keyboard set : " + str(r) + "," + str(g) + "," + str(b) + " ")

    def mousepad(self,r,g,b,step,duration):
        etc = ETCfuncs()
        color = setCOLOR()

        for x in etc.range_float(0, 2, step):
            NRval = int((1 - abs(x - 1)) * r)
            NGval = int((1 - abs(x - 1)) * g)
            NBval = int((1 - abs(x - 1)) * b)
            color.mousepad(NRval, NGval, NBval, RazerURI, 0)
            sleep(duration)

        if mainDebug:
            print("[INFO] Glow mousepad set : " + str(r) + "," + str(g) + "," + str(b) + " ")

    def headset(self,r,g,b,step,duration):
        etc = ETCfuncs()
        color = setCOLOR()

        for x in etc.range_float(0, 2, step):
            NRval = int((1 - abs(x - 1)) * r)
            NGval = int((1 - abs(x - 1)) * g)
            NBval = int((1 - abs(x - 1)) * b)
            color.headset(NRval, NGval, NBval, RazerURI, 0)
            sleep(duration)

        if mainDebug:
            print("[INFO] Glow headset set : " + str(r) + "," + str(g) + "," + str(b) + " ")

    def etc(self,r,g,b,step,duration):
        etc = ETCfuncs()
        color = setCOLOR()

        for x in etc.range_float(0, 2, step):
            NRval = int((1 - abs(x - 1)) * r)
            NGval = int((1 - abs(x - 1)) * g)
            NBval = int((1 - abs(x - 1)) * b)
            color.etc(NRval, NGval, NBval, RazerURI, 0)
            sleep(duration)

        if mainDebug:
            print("[INFO] Glow etc set : " + str(r) + "," + str(g) + "," + str(b) + " ")

    def all(self,r,g,b,step,duration):
        global RazerURI
        etc = ETCfuncs()
        color = setCOLOR()

        for x in etc.range_float(0, 2, step):
            NRval = int((1 - abs(x - 1)) * r)
            NGval = int((1 - abs(x - 1)) * g)
            NBval = int((1 - abs(x - 1)) * b)

            color.keyboard(NRval, NGval, NBval, RazerURI, 0)
            color.mouse(NRval, NGval, NBval, RazerURI, 0)
            color.mousepad(NRval, NGval, NBval, RazerURI, 0)
            color.headset(NRval, NGval, NBval, RazerURI, 0)
            color.etc(NRval, NGval, NBval, RazerURI, 0)

            sleep(duration)

            if mainDebug:
                print("[INFO] Glow all set : " + str(r) + "," + str(g) + "," + str(b) + " ")



class ETCfuncs():
    def range_float(self, start, stop, step):
        while start < stop:
            yield start
            start += step



def RainBowAll(step): # how fast the rainbow should be changed.
    while True:
        for g in range(0,255,step):
            #Corsair.KeyboardSetdAll(255, g, 0, 0.001)
            SetAllColor(255,g,0,0)

        for r in range(255 , 0 , -step):
            #Corsair.KeyboardSetdAll(r,255,0,0.001)
            SetAllColor(r,255,0,0)

        for b in range(0,255,step):
            #Corsair.KeyboardSetdAll(0,255,b,0.001)
            SetAllColor(0,255,b,0)

        for g in range(255 , 0 , -step):
            #Corsair.KeyboardSetdAll(0,g,255,0.001)
            SetAllColor(0,g,255,0)

        for r in range(0,255,step):
            #Corsair.KeyboardSetdAll(r,0,255,0.001)
            SetAllColor(r,0,255,0)

        for b in range(255 , 0 , -step):
            #Corsair.KeyboardSetdAll(255,0,b,0.001)
            SetAllColor(255,0,b,0)



def serverON():
    global server
    server = True

def serverOFF():
    global server
    server = False

def setdevs():
    config_path = Path(str(__file__).replace("main.py", "Config.txt"))
    if config_path.is_file():
        print("[INFO] Config File Exists.")
        firstinit()
    else:
        print("[INFO] Config File Does Not Exist.")
        print("[]")


def firstinit():
    print("[INFO] Seems that you are using this program for the first time.")
    print("[INFO] This program will create a file called \"config.txt\"")
    config = Config()
    config.write()
    return config.read()

def isFirstRun():
    config_path = Path(str(__file__).replace("main.py", "Config.txt"))
    if mainDebug:
        print(config_path)

    if config_path.is_file():
        print("[INFO] Config File Exists.")
        return False
    else:
        print("[INFO] Config File Does Not Exist.")
        return True


def mainInit():
    print("██████╗ ██╗   ██╗██████╗ ██╗  ██╗███████╗██████╗ ███████╗██████╗ ██╗ █████╗ ██╗")
    print("██╔══██╗╚██╗ ██╔╝██╔══██╗██║  ██║██╔════╝██╔══██╗██╔════╝██╔══██╗██║██╔══██╗██║")
    print("██████╔╝ ╚████╔╝ ██████╔╝███████║█████╗  ██████╔╝█████╗  ██████╔╝██║███████║██║")
    print("██╔═══╝   ╚██╔╝  ██╔═══╝ ██╔══██║██╔══╝  ██╔═══╝ ██╔══╝  ██╔══██╗██║██╔══██║██║")
    print("██║        ██║   ██║     ██║  ██║███████╗██║     ███████╗██║  ██║██║██║  ██║███████╗")
    print("╚═╝        ╚═╝   ╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝     ╚══════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═╝╚══════╝")
    print("                                                                       By Gooday2die")
    print("                  Please Check My Github : https://github.com/gooday2die/pypheperial")
    print()

#    print("[INFO] Select Operating Mode : ")
#    print("(1) CLI  /  (2) GUI")

    if isFirstRun():
        firstinit()
        config = Config()
        config.read()

    else:
        print("[INFO] Welcome Back!")
        config = Config()
        config.read()

    ops = SDKops()
    ops.SDKInits(DEVLIST)


def SetAllColor(r,g,b,duration):
    global RazerURI
    '''
    Sync every color into just one color.
    If you want no delays between those, please set duraton to 0.
    However, this would not remove delay completely.
    I have tried multi-threading. However, it is not perfectly no delay.
    Would be fixed in the future.
    '''

    Color = setCOLOR()
    Color.keyboard(r,g,b,RazerURI,duration)
    Color.mouse(r,g,b,RazerURI,duration)
    Color.mousepad(r,g,b,RazerURI,duration)
    Color.headset(r,g,b,RazerURI,duration)
    Color.etc(r,g,b,RazerURI,duration)


if __name__ == '__main__':
    Debug = Debug()
    Debug.ON
    mainInit()
    glow = GlowKeys()
    test = TEST()

    color = setCOLOR()


    SetAllColor(255,0,255,0)

    sleep(3)

    glow.all(255,255,255,0.01,0.005)
    glow.all(255,0,0,0.01,0.005)
    glow.all(0,255,0,0.01,0.005)
    glow.all(0,0,255,0.01,0.005)
    glow.all(255,255,255,0.01,0.005)

    #test.randomColors()

    sleep(4)
