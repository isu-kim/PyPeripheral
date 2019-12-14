from Wrappers import Corsair
from Wrappers import Razer
from pathlib import Path
from time import sleep
import random
from Wrappers.cue_sdk import *

'''
Now Re-editing for PEP8 Style and more class based.
Nicer Function, Class, Variable names.
'''


class DevList:
    # Device List in main function for init
    def __init__(self):
        self.keyboard = None
        self.mouse = None
        self.mouse_pad = None
        self.headset = None
        self.headset_stand = None
        self.etc = None
        self.Sdks = []


class Sdks:
    def __init__(self):
        self.Razer = None
        self.Corsair = None

        self.RazerMouse = None
        self.RazerKeyboard = None
        self.RazerMousePD = None
        self.RazerHeadSet = None
        self.RazerHeadsetStand = None
        self.RazerETC = None

        self.CorsairMouse = None
        self.CorsairKeyboard = None
        self.CorsairMousePD = None
        self.CorsairHeadSet = None
        self.CorsairHeadsetStand = None
        self.CorsairETC = None


class Tests:
    """
    This class includes some of simple testing scripts whether the program is successfully working
    White_Out will set all device color to white, and wait 3sec.
    rainbow_all will set all device color into rainbow shaped. this will loop forever.
    """
    def __init__(self, debug_object, test_sdk_object):
        self.debug = debug_object
        self.sdk = test_sdk_object

    def set_all_white(self):
        sw_set_color = SetColor(self.sdk)
        for i in range(300):
            sw_set_color.all(255, 255, 255, 0)
            sleep(0.001)

    def rainbow_all(self, step):
        """
        Function for Setting all the keys rainbow shift.
        step is the parameter for how fast the rainbow should shift.
        """
        ra_set_color = SetColor(self.sdk)
        while True:
            for g in range(0, 255, step):
                ra_set_color.all(255, g, 0, 0)

            for r in range(255, 0, -step):
                ra_set_color.all(r, 255, 0, 0)

            for b in range(0, 255, step):
                ra_set_color.all(0, 255, b, 0)

            for g in range(255, 0, -step):
                ra_set_color.all(0, g, 255, 0)

            for r in range(0, 255, step):
                ra_set_color.all(r, 0, 255, 0)

            for b in range(255, 0, -step):
                ra_set_color.all(255, 0, b, 0)

    def random_colors(self):
        while True:
            # All t_variables are for the Tests class only.
            t_color = SetColor(self.sdk)
            t_color.mouse(random.randrange(1, 256), random.randrange(1, 256), random.randrange(1, 256), 0)
            t_color.keyboard(random.randrange(1, 256), random.randrange(1, 256), random.randrange(1, 256), 0)
            t_color.mouse_pad(random.randrange(1, 256), random.randrange(1, 256), random.randrange(1, 256), 0)
            t_color.headset(random.randrange(1, 256), random.randrange(1, 256), random.randrange(1, 256), 0)
            t_color.etc(random.randrange(1, 256), random.randrange(1, 256), random.randrange(1, 256), 0)

    def glow_effect_test(self):
        # All t_variables are for the Tests class only.
        t_glow = GlowKeys(self.debug, self.sdk)
        t_glow.all(255, 255, 255, 0.01, 0.005)
        t_glow.all(255, 0, 0, 0.01, 0.005)
        t_glow.all(0, 255, 0, 0.01, 0.005)
        t_glow.all(0, 0, 255, 0.01, 0.005)
        t_glow.all(255, 255, 255, 0.01, 0.005)


class SetColor:
    """
    This class is for setting colors regardless of the Sdks.
    for example, SetColor.mouse will set ALL connected mouse color into just one color.
    If you wish to control individually, please import files from Wrappers directory.
    Direct Control should be in this way : Corsair.ledOn(CLK.GLAV_1, 255, 255, 255, 0)

    Also, If you wish to set all the device color instantly with out any delay, please set duration as 0
    Otherwise, the lighting would be in wave shape. There would be at least delays between leds.
    """

    def __init__(self, sc_sdk_object):
        self.razer_uri = Razer.get_uri()
        self.sdk = sc_sdk_object

    def mouse(self, r, g, b, duration):
        if self.sdk.RazerMouse:
            effect_id = Razer.create_mouse_effect("CHROMA_STATIC", r, g, b, self.razer_uri)
            Razer.set_effect(effect_id, self.razer_uri)

        if self.sdk.CorsairMouse:
            Corsair.led_on(CLM.Z1, r, g, b, duration)
            Corsair.led_on(CLM.Z2, r, g, b, duration)
            Corsair.led_on(CLM.Z3, r, g, b, duration)
            Corsair.led_on(CLM.Z4, r, g, b, duration)
            Corsair.led_on(CLM.Z5, r, g, b, duration)
            Corsair.led_on(CLM.Z6, r, g, b, duration)

    def keyboard(self, r, g, b, duration):
        if self.sdk.RazerKeyboard:
            effect_id = Razer.create_keyboard_effect("CHROMA_STATIC", r, g, b, self.razer_uri)
            Razer.set_effect(effect_id, self.razer_uri)

        if self.sdk.CorsairKeyboard:

            exception_list = [148, 149, 150, 151, 189, 190,  # Mouse
                              155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169,  # mouse_pad
                              152, 153,  # HeadSet
                              ]

            for i in range(191):
                if i not in exception_list:
                    Corsair.led_on(i, r, g, b, duration)

    def mouse_pad(self, r, g, b, duration):
        if self.sdk.RazerMousePD:
            effect_id = Razer.create_mousepad_effect("CHROMA_STATIC", r, g, b, self.razer_uri)
            Razer.set_effect(effect_id, self.razer_uri)

        if self.sdk.CorsairMousePD:
            Corsair.led_on(CLMM.Zone1, r, g, b, duration)
            Corsair.led_on(CLMM.Zone2, r, g, b, duration)
            Corsair.led_on(CLMM.Zone3, r, g, b, duration)
            Corsair.led_on(CLMM.Zone4, r, g, b, duration)
            Corsair.led_on(CLMM.Zone5, r, g, b, duration)
            Corsair.led_on(CLMM.Zone6, r, g, b, duration)
            Corsair.led_on(CLMM.Zone7, r, g, b, duration)
            Corsair.led_on(CLMM.Zone8, r, g, b, duration)
            Corsair.led_on(CLMM.Zone9, r, g, b, duration)
            Corsair.led_on(CLMM.Zone10, r, g, b, duration)
            Corsair.led_on(CLMM.Zone11, r, g, b, duration)
            Corsair.led_on(CLMM.Zone12, r, g, b, duration)
            Corsair.led_on(CLMM.Zone13, r, g, b, duration)
            Corsair.led_on(CLMM.Zone14, r, g, b, duration)
            Corsair.led_on(CLMM.Zone15, r, g, b, duration)

    def headset(self, r, g, b, duration):
        if self.sdk.CorsairHeadSet:
            Corsair.led_on(CLH.LeftLogo, r, g, b, duration)
            Corsair.led_on(CLH.RightLogo, r, g, b, duration)

        if self.sdk.RazerHeadSet:
            effect_id = Razer.create_headset_effect("CHROMA_STATIC", r, g, b, self.razer_uri)
            Razer.set_effect(effect_id, self.razer_uri)

    def headset_stand(self, r, g, b, duration):
        if self.sdk.CorsairHeadsetStand:
            Corsair.led_on(CLHSS.Zone1, r, g, b, duration)
            Corsair.led_on(CLHSS.Zone2, r, g, b, duration)
            Corsair.led_on(CLHSS.Zone3, r, g, b, duration)
            Corsair.led_on(CLHSS.Zone4, r, g, b, duration)
            Corsair.led_on(CLHSS.Zone5, r, g, b, duration)
            Corsair.led_on(CLHSS.Zone6, r, g, b, duration)
            Corsair.led_on(CLHSS.Zone7, r, g, b, duration)
            Corsair.led_on(CLHSS.Zone8, r, g, b, duration)
            Corsair.led_on(CLHSS.Zone9, r, g, b, duration)

        if self.sdk.RazerHeadsetStand:
            effect_id = Razer.create_etc_effect("CHROMA_STATIC", r, g, b, self.razer_uri)
            Razer.set_effect(effect_id, self.razer_uri)

    def etc(self, r, g, b, duration):
        if self.sdk.RazerETC:
            effect_id = Razer.create_etc_effect("CHROMA_STATIC", r, g, b, self.razer_uri)
            Razer.set_effect(effect_id, self.razer_uri)

        if self.sdk.CorsairETC:
            for i in range(191, 500, 1):  # Check Wrappers/Corsair/cue_sdk/enumerations.py for more information.
                Corsair.led_on(i, r, g, b, duration)

    def all(self, r, g, b, duration):
        self.headset(r, g, b, duration)
        self.mouse(r, g, b, duration)
        self.mouse_pad(r, g, b, duration)
        self.keyboard(r, g, b, duration)
        self.headset_stand(r, g, b, duration)
        self.etc(r, g, b, duration)


class Config:
    def __init__(self, debug_object, dev_list_object):
        self.debug = debug_object
        self.dev_list = dev_list_object
    """
    This class is for config files.
    config write would read the config files and store the information inside config to a class called DevList.
    If you wish to use my program as it is, do not touch this part.
    """

    def write(self):
        f = open("Config.txt", "w")
        f.write("#PyPheperial Config File\n")
        f.write("#Please DO NOT change anything from this file unless you know how it works.\n")
        f.write("#If you wish to change devices, delete this config. The software would generate a new one for you.\n")

        # This file would save the info with this type
        # Example
        # MOUSE=RAZER,CORSAIR
        # KEYBOARD=CORSAIR
        # mouse_pad=CORSAIR
        # HEADSET=CORSAIR
        # ETC=CORSAIR

        print("[INFO] Please tell us your spec")
        print("[INFO] If you have more than one devices per category, use it with comma")
        print("[INFO] Type in \"None\" for no Device")
        print("[INFO] ex) RAZER,CORSAIR")

        mouse = input("[INFO] Mouse : ")
        keyboard = input("[INFO] Keyboard : ")
        mouse_pad = input("[INFO] Mouse Pad : ")
        headset = input("[INFO] Headset : ")
        headset_stand = input("[INFO] Headset Stand : ")
        etc = input("[INFO] ETC : ")

        f.write("MOUSE=" + str(mouse) + "\n")
        f.write("KEYBOARD=" + str(keyboard) + "\n")
        f.write("MOUSEPAD=" + str(mouse_pad) + "\n")
        f.write("HEADSET=" + str(headset) + "\n")
        f.write("HEADSETSTAND="+str(headset_stand)+"\n")
        f.write("ETC=" + str(etc) + "\n")
        f.write("EOF\n")

        f.close()

        print("[INFO] Thank you! Configuration Done. Now setting up some things for real action.")

    def read(self):
        f = open("Config.txt", "r")
        lines = f.readlines()
        # Line 3 : Mouse / 4 : Keyboard / 5 : mouse_pad / 6 : Headset / 7 : Headset Stand / 8 : Etc

        mouse = [x.strip() for x in lines[3].replace("MOUSE=", "").split(',')]
        if self.debug.return_state():
            print("[DEBUG] Mouse : ", end="")
            print(mouse)

        keyboard = [x.strip() for x in lines[4].replace("KEYBOARD=", "").split(',')]
        if self.debug.return_state():
            print("[DEBUG] Keyboard : ", end="")
            print(keyboard)

        mouse_pad = [x.strip() for x in lines[5].replace("MOUSEPAD=", "").split(',')]
        if self.debug.return_state():
            print("[DEBUG] Mouse Pad : ", end="")
            print(mouse_pad)

        headset = [x.strip() for x in lines[6].replace("HEADSET=", "").split(',')]
        if self.debug.return_state():
            print("[DEBUG] Head Set : ", end="")
            print(headset)

        headset_stand = [x.strip() for x in lines[6].replace("HEADSETSTAND=", "").split(',')]
        if self.debug.return_state():
            print("[DEBUG] Head Set Stand : ", end="")
            print(headset_stand)

        etc = [x.strip() for x in lines[8].replace("ETC=", "").split(',')]
        if self.debug.return_state():
            print("[DEBUG] ETC : ", end="")
            print(etc)

        self.dev_list.mouse = mouse
        self.dev_list.keyboard = keyboard
        self.dev_list.mouse_pad = mouse_pad
        self.dev_list.headset = headset
        self.dev_list.headset_stand = headset_stand
        self.dev_list.etc = etc


class Debug:
    """
    This class is for debugging. debug.ON and debug.OFF would just effect all the debugs just in main.py.
    If you wish to use all the debugs in all the Sdks, please use debug.AllON
    If you wish to use them individually, please refer to the individual SDK Wrapper files in the project. or use the
    function in this class.
    """

    def __init__(self):
        self.debug = False
        Corsair.debug_off()
        Razer.debug_off()

    def on(self):
        self.debug = True

    def off(self):
        self.debug = True
        Corsair.debug_off()
        Razer.debug_off()

    def all_on(self):
        self.debug = True
        Corsair.debug_on()
        Razer.debug_on()

    def corsair(self):
        Corsair.debug_on()

    def razer(self):
        Razer.debug_on()

    def return_state(self):
        return self.debug


class SDKOperations:
    """
     This class is for SDK information.
     This class finds out all the information regarding your device written in Config file, and decide which one to use.
     All the functions in this class uses Sdks class which contains boolean values for each devices.
     """

    def __init__(self, debug_object, dev_list_object, ops_sdk_object):
        self.dev_list = dev_list_object
        self.debug = debug_object
        self.sdk = ops_sdk_object

    def sdk_types(self):
        dump = []

        for i in range(len(self.dev_list.mouse)):
            dump.append(self.dev_list.mouse[i])

        for i in range(len(self.dev_list.keyboard)):
            dump.append(self.dev_list.keyboard[i])

        for i in range(len(self.dev_list.mouse_pad)):
            dump.append(self.dev_list.mouse_pad[i])

        for i in range(len(self.dev_list.etc)):
            dump.append(self.dev_list.etc[i])

        for i in range(len(self.dev_list.headset)):
            dump.append(self.dev_list.headset[i])

        for i in range(len(self.dev_list.headset_stand)):
            dump.append(self.dev_list.headset_stand[i])

        if self.debug.return_state():
            print(dump)
            print(len(list(dict.fromkeys(dump))))
            print(list(dict.fromkeys(dump)))

        self.dev_list.Sdks = list(dict.fromkeys(dump))

    def clear_sdk(self):
        self.sdk.Razer = False
        self.sdk.RazerMouse = False
        self.sdk.RazerKeyboard = False
        self.sdk.RazerHeadSet = False
        self.sdk.RazerMousePD = False
        self.sdk.RazerHeadsetStand = False
        self.sdk.RazerETC = False

        self.sdk.Corsair = False
        self.sdk.CorsairMouse = False
        self.sdk.CorsairKeyboard = False
        self.sdk.CorsairMousePD = False
        self.sdk.CorsairHeadSet = False
        self.sdk.CorsairHeadsetStand = False
        self.sdk.CorsairETC = False

    def sdk_inits(self):
        global RazerURI

        self.clear_sdk()
        self.sdk_types()

        if self.debug.return_state():
            print(self.dev_list.Sdks)

        if "RAZER" in self.dev_list.Sdks:
            print("[INFO] RAZER Device Found. Initiating SDK")
            RazerURI = Razer.get_uri()
            self.sdk.Razer = True

            if "RAZER" in self.dev_list.mouse:
                self.sdk.RazerMouse = True

            if "RAZER" in self.dev_list.headset:
                self.sdk.RazerHeadSet = True

            if "RAZER" in self.dev_list.keyboard:
                self.sdk.RazerKeyboard = True

            if "RAZER" in self.dev_list.mouse_pad:
                self.sdk.RazerMousePD = True

            if "RAZER" in self.dev_list.headset_stand:
                self.sdk.RazerHeadsetStand = True

            if "RAZER" in self.dev_list.etc:
                self.sdk.RazerETC = True

        if "CORSAIR" in self.dev_list.Sdks:
            print("[INFO] CORSAIR Device Found. Requesting Control")
            Corsair.request_control()
            self.sdk.Corsair = True

            if "CORSAIR" in self.dev_list.mouse:
                self.sdk.CorsairMouse = True

            if "CORSAIR" in self.dev_list.headset:
                self.sdk.CorsairHeadSet = True

            if "CORSAIR" in self.dev_list.keyboard:
                self.sdk.CorsairKeyboard = True

            if "CORSAIR" in self.dev_list.mouse_pad:
                self.sdk.CorsairMousePD = True

            if "CORSAIR" in self.dev_list.headset_stand:
                self.sdk.CorsairHeadsetStand = True

            if "CORSAIR" in self.dev_list.etc:
                self.sdk.CorsairETC = True

        if ("CORSAIR" not in self.dev_list.Sdks) and ("RAZER" not in self.dev_list.Sdks):
            print("[INFO] No Supported Sdks found. Only Razer and Corsair are supported right now.")
            print("[INFO] Exiting Program ...")
            exit(0)

        if self.debug.return_state():
            print(vars(self.sdk))


class GlowKeys:
    def __init__(self, debug_object, glow_sdk_object):
        self.debug = debug_object
        self.sdk = glow_sdk_object
        self.set_color = SetColor(self.sdk)
        self.etc = EtcFuncs()
    """
    This class is for "Glowing" keys. This would smoothly turn the keys on light.
    "step" parameter is for how rapidly the light should turn. The higher parameter is, the smoother keys will glow.
    However it will turn on slowly. "duration" parameter is for how much seconds shall it be stopped between those
    loops. The higher parameter is, the slower keys glow.
    """

    def mouse(self, r, g, b, step, duration):
        for x in self.etc.range_float(0, 2, step):
            n_rval = int((1 - abs(x - 1)) * r)
            n_gval = int((1 - abs(x - 1)) * g)
            n_bval = int((1 - abs(x - 1)) * b)
            self.set_color.mouse(n_rval, n_gval, n_bval, 0)
            sleep(duration)

        if debug.return_state():
            print("[INFO] Glow mouse set : " + str(r) + "," + str(g) + "," + str(b) + " ")

    def keyboard(self, r, g, b, step, duration):
        for x in self.etc.range_float(0, 2, step):
            n_rval = int((1 - abs(x - 1)) * r)
            n_gval = int((1 - abs(x - 1)) * g)
            n_bval = int((1 - abs(x - 1)) * b)
            self.set_color.keyboard(n_rval, n_gval, n_bval, 0)
            sleep(duration)

        if debug.return_state():
            print("[INFO] Glow keyboard set : " + str(r) + "," + str(g) + "," + str(b) + " ")

    def mouse_pad(self, r, g, b, step, duration):
        for x in self.etc.range_float(0, 2, step):
            n_rval = int((1 - abs(x - 1)) * r)
            n_gval = int((1 - abs(x - 1)) * g)
            n_bval = int((1 - abs(x - 1)) * b)
            self.set_color.mouse_pad(n_rval, n_gval, n_bval, 0)
            sleep(duration)

        if debug.return_state():
            print("[INFO] Glow mouse_pad set : " + str(r) + "," + str(g) + "," + str(b) + " ")

    def headset(self, r, g, b, step, duration):
        for x in self.etc.range_float(0, 2, step):
            n_rval = int((1 - abs(x - 1)) * r)
            n_gval = int((1 - abs(x - 1)) * g)
            n_bval = int((1 - abs(x - 1)) * b)
            self.set_color.headset(n_rval, n_gval, n_bval, 0)
            sleep(duration)

        if debug.return_state():
            print("[INFO] Glow headset set : " + str(r) + "," + str(g) + "," + str(b) + " ")

    def etc(self, r, g, b, step, duration):
        for x in self.etc.range_float(0, 2, step):
            n_rval = int((1 - abs(x - 1)) * r)
            n_gval = int((1 - abs(x - 1)) * g)
            n_bval = int((1 - abs(x - 1)) * b)
            self.set_color.etc(n_rval, n_gval, n_bval, 0)
            sleep(duration)

        if debug.return_state():
            print("[INFO] Glow etc set : " + str(r) + "," + str(g) + "," + str(b) + " ")

    def all(self, r, g, b, step, duration):
        global RazerURI
        for x in self.etc.range_float(0, 2, step):
            n_rval = int((1 - abs(x - 1)) * r)
            n_gval = int((1 - abs(x - 1)) * g)
            n_bval = int((1 - abs(x - 1)) * b)

            self.set_color.keyboard(n_rval, n_gval, n_bval, 0)
            self.set_color.mouse(n_rval, n_gval, n_bval, 0)
            self.set_color.mouse_pad(n_rval, n_gval, n_bval, 0)
            self.set_color.headset(n_rval, n_gval, n_bval, 0)
            self.set_color.headset_stand(n_rval, n_gval, n_bval, 0)
            self.set_color.etc(n_rval, n_gval, n_bval, 0)

            sleep(duration)

            if debug.return_state():
                print("[INFO] Glow all set : " + str(r) + "," + str(g) + "," + str(b) + " ")


class EtcFuncs:
    """
    This Class is for Etc Functions such as range_float function.
    range_float function : this function is for the same python range function
    for float numbers.
    """
    def range_float(self, start, stop, step):
        while start < stop:
            yield start
            start += step


class InitTools:
    def __init__(self, debug_object, dev_list_object, init_sdk_object):
        self.dev_list = dev_list_object
        self.debug = debug_object
        self.sdks = init_sdk_object

    def first_init(self):
        print("[INFO] Seems that you are using this program for the first time.")
        print("[INFO] This program will create a file called \"config.txt\"")
        config = Config(self.debug, self.dev_list)
        config.write()
        return config.read()

    def is_first_run(self):
        config_path = Path(str(__file__).replace("main.py", "Config.txt"))
        if self.debug.return_state():
            print(config_path)

        if config_path.is_file():
            print("[INFO] Config File Exists.")
            return False
        else:
            print("[INFO] Config File Does Not Exist.")
            return True

    def main_init(self):

        print("██████╗ ██╗   ██╗██████╗ ██╗  ██╗███████╗██████╗ ███████╗██████╗ ██╗ █████╗ ██╗")
        print("██╔══██╗╚██╗ ██╔╝██╔══██╗██║  ██║██╔════╝██╔══██╗██╔════╝██╔══██╗██║██╔══██╗██║")
        print("██████╔╝ ╚████╔╝ ██████╔╝███████║█████╗  ██████╔╝█████╗  ██████╔╝██║███████║██║")
        print("██╔═══╝   ╚██╔╝  ██╔═══╝ ██╔══██║██╔══╝  ██╔═══╝ ██╔══╝  ██╔══██╗██║██╔══██║██║")
        print("██║        ██║   ██║     ██║  ██║███████╗██║     ███████╗██║  ██║██║██║  ██║███████╗")
        print("╚═╝        ╚═╝   ╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝     ╚══════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═╝╚══════╝")
        print("                                                                         Version 0.1")
        print("                                                                       By Gooday2die")
        print("                  Please Check My Github : https://github.com/gooday2die/pypheperial")
        print()

        if self.is_first_run():
            self.first_init()
            config = Config(self.debug, self.dev_list)
            config.read()

        else:
            print("[INFO] Welcome Back!")
            config = Config(self.debug, self.dev_list)
            config.read()

        ops = SDKOperations(self.debug, self.dev_list, self.sdks)
        ops.sdk_inits()


"""
if __name__ == "__main__":
    RazerURI = None
    Debug = Debug()
    Debug.on()
    Init = InitTools()
    Init.main_init()
    glow = GlowKeys()
    glow.mouse(255, 255, 255, 0.1, 0.1)
    test = Tests()
    color = SetColor()
    Test = Tests()
    # Test.random_colors()
    # Test.glow_effect_test()
    Test.set_all_white()
    Test.rainbow_all(10)
"""

"""
dev_list = DevList()
debug = Debug()
sdk_object = Sdks()

init = InitTools(debug, dev_list, sdk_object)
init.main_init()
set_color = SetColor(sdk_object)

#set_color.mouse(255, 255, 255, 0)
#test = Tests(debug, sdk_object)
#test.rainbow_all(20)
"""