from .cue_sdk import *
import time

dir_path = str(__file__).replace("Corsair.py", "DLLs/CUESDK.x64_2015.dll")
print("[INFO] Corsair ICUE DLL Path : " + str(dir_path))
cue = CUESDK(dir_path)
global debug
global DeviceList
global NewDeviceID
global DeviceType
debug = False
DeviceList = []
NewDeviceID = []
DeviceType = []


def range_float(start, stop, step):
    while start < stop:
        yield start
        start += step


def debugON():
    print("[DEBUG] Debug Enabled.")
    global debug
    debug = True


def debugOFF():
    print("[DEBUG] Debug Disabled.")
    global debug
    debug = False


def DeviceInfo():
    global DeviceList
    global DeviceType
    print(("[INFO] There are " + str(cue.get_device_count())) + " connected Corsair devices.")
    for i in range(cue.get_device_count()):
        # print("Device #" + str(i+1) , str(cue.get_device_info(i))) # For all details about the devices
        print("Device #" + str(i + 1), str(cue.get_device_info(i)[1]))  # For just names
        thing_to_append = (str(cue.get_device_info(i)[1]) + "_" + str(cue.get_device_info(i)[0]))
        DeviceList.append(thing_to_append)
        DeviceType.append(cue.get_device_info(i)[0])
    return DeviceList


def RequestControl():
    cue.RequestControl(CAM.ExclusiveLightingControl)
    print("[INFO] Successfully Requested Corsair ICUE Control")


def ReleaseControl():
    cue.ReleaseControl(CAM.ExclusiveLightingControl)
    print("[INFO] Successfully Released Corsair ICUE Control")


def BlackLED(LED_ID):
    led_color = CorsairLedColor(LED_ID, 0, 0, 0)
    cue.set_led_colors(led_color)


def ledOn(LED_ID, RVal, GVal, BVal, Duration):
    global debug
    if debug:
        print("[DEBUG] LED_ID :", str(LED_ID), "R :", str(RVal), "G :", str(GVal), " B :", str(BVal), "Duration :",
              str(Duration))
    led_color = CorsairLedColor(LED_ID, RVal, GVal, BVal)
    cue.set_led_colors(led_color)
    time.sleep(Duration)


def ledSmoothOn(LED_ID, RVal, GVal, BVal, Duration):
    global debug
    for x in range_float(0, 2, 0.1):
        NRval = int((1 - abs(x - 1)) * RVal)
        NGval = int((1 - abs(x - 1)) * GVal)
        NBval = int((1 - abs(x - 1)) * BVal)
        if debug:
            print("[DEBUG] LED_ID :", str(LED_ID), "R :", str(NRval), "G :", str(NGval), " B :", str(NBval),
                  "Duration :", str(Duration))
        led_color = CorsairLedColor(LED_ID, NRval, NGval, NBval)
        cue.set_led_colors(led_color)
        time.sleep(Duration)


def DeviceID(DeviceList):
    global NewDeviceID
    global debug

    for i in range(len(DeviceList)):
        if "pad" in DeviceList[i]:
            NewDeviceID.append(
                "4" + str(((DeviceList[i].replace(".Mousepad", "")).replace("_CDT", "")).replace("pad", "")))
            DeviceList[i] = "NULLCHAR"
    for i in range(len(DeviceList)):
        if ".Keyboard" in DeviceList[i]:
            NewDeviceID.append("2" + str(DeviceList[i].replace(".Keyboard", "").replace("_CDT", "")))
    for i in range(len(DeviceList)):
        if ".Headset" in DeviceList[i]:
            NewDeviceID.append("3" + str(DeviceList[i].replace(".Headset", "").replace("_CDT", "")))
    for i in range(len(DeviceList)):
        if ".Mouse" in DeviceList[i]:
            NewDeviceID.append("1" + str(DeviceList[i].replace(".Mouse", "").replace("_CDT", "")))
    return NewDeviceID


def KeyboardCheck():
    global NewDeviceID
    global DeviceType

    for i in range(len(NewDeviceID)):
        if NewDeviceID[i][0] == '2':
            KeyboardID = i
            NewDeviceID[KeyboardID] = NewDeviceID[KeyboardID].replace("2", "").replace("_CDT", "")
            if NewDeviceID[KeyboardID] == "K95 RGB PLATINUM":
                ledOn(CLK.G1, 0, 255, 0, 0.1)
                ledOn(CLK.G2, 0, 255, 0, 0.1)
                ledOn(CLK.G3, 0, 255, 0, 0.1)
                ledOn(CLK.G4, 0, 255, 0, 0.1)
                ledOn(CLK.G5, 0, 255, 0, 0.1)
                ledOn(CLK.G6, 0, 255, 0, 0.1)

                ledOn(CLK.G1, 0, 0, 0, 0.1)
                ledOn(CLK.G2, 0, 0, 0, 0.1)
                ledOn(CLK.G3, 0, 0, 0, 0.1)
                ledOn(CLK.G4, 0, 0, 0, 0.1)
                ledOn(CLK.G5, 0, 0, 0, 0.1)
                ledOn(CLK.G6, 0, 0, 0, 0.1)

                '''
                I do know that using for or while loop would be more effective way to do this.
                However, this process is to check all the dependencies were correctly installed. 

                If the importing cue_sdk module was not complete nor successful, CLK.G keys would be showing errors on the CLK is not defined.
                '''

                for i in range(170, 188, 1):
                    ledOn(i, 0, 255, 0, 0.01)
                    ledOn(i + 1, 0, 255, 0, 0.01)

                for i in range(170, 188, 1):
                    ledOn(i, 0, 0, 0, 0.01)
                    ledOn(i + 1, 0, 0, 0, 0.01)

                for i in range(188, 170, -1):
                    ledOn(i, 0, 255, 0, 0.01)
                    ledOn(i + 1, 0, 255, 0, 0.01)

                for i in range(188, 170, -1):
                    ledOn(i, 0, 0, 0, 0.01)
                    ledOn(i + 1, 0, 0, 0, 0.01)

                '''
                If this function was correctly executed, it means that there would be no issues when controlling Corsair ICUE SDK.
                At least for me, my pheperials (K95 RGB , Glaive , Void , MM800) were ready for me to control LEDs.

                If this crashes, The key LED mapping would be mismatched.  

                '''

            else:
                for i in range(2):
                    ledSmoothOn(CLK.Space, 0, 255, 0, 0.01)
                for i in range(1, 12, 1):
                    ledOn(i, 0, 255, 0, 0.1)
                for i in range(1, 12, 1):
                    ledOn(i, 0, 0, 0, 0.1)
                ledOn(CLK.F12, 0, 0, 0, 0.1)

            print("[INFO]", str(NewDeviceID[KeyboardID]), "Connected")
            return

    print("[INFO] No Corsair Keyboard Found")


def MousePadCheck():
    global NewDeviceID
    global DeviceType

    for i in range(len(NewDeviceID)):
        if NewDeviceID[i][0] == '4':
            MousePadID = i
            NewDeviceID[MousePadID] = NewDeviceID[MousePadID].replace("4", "").replace("_CDT", "")
            if "MM800RGB" in NewDeviceID:
                for i in range(2):
                    ledSmoothOn(CLK.MM800_1, 0, 255, 0, 0.01)

                for i in range(155, 169, 1):
                    ledOn(i, 0, 255, 0, 0.1)

                for i in range(155, 169, 1):
                    ledOn(i, 0, 0, 0, 0.1)

                print("[INFO]", str(NewDeviceID[MousePadID]), "Connected")
                return

    print("[INFO] No Corsair Mouse Pad Found")


def MouseCheck():
    global NewDeviceID
    global DeviceType

    for i in range(len(NewDeviceID)):
        if NewDeviceID[i][0] == '1':
            MouseID = i
            NewDeviceID[MouseID] = NewDeviceID[MouseID].replace("1", "").replace("_CDT", "")
        if "GLAIVE RGB" in NewDeviceID:
            for i in range(2):
                ledSmoothOn(CLK.GLAV_2, 0, 255, 0, 0.01)

            for i in [CLK.GLAV_1, CLK.GLAV_2, CLK.GLAV_3]:
                ledOn(i, 0, 255, 0, 0.1)

            for i in [CLK.GLAV_1, CLK.GLAV_2, CLK.GLAV_3]:
                ledOn(i, 0, 0, 0, 0.1)

            print("[INFO]", str(NewDeviceID[MouseID]), "Connected")
            return

    print("[INFO] No Corsair Mouse Found")


def HeadPhoneCheck():
    global NewDeviceID
    global DeviceType

    for i in range(len(NewDeviceID)):
        if NewDeviceID[i][0] == '3':
            HeadPhoneID = i
            NewDeviceID[HeadPhoneID] = NewDeviceID[HeadPhoneID].replace("3", "").replace("_CDT", "")

        if "VOID PRO USB" in NewDeviceID:
            for i in range(2):
                ledSmoothOn(CLK.VOIDPRO_L, 0, 255, 0, 0.01)

            for i in [CLK.VOIDPRO_L, CLK.VOIDPRO_R]:
                ledOn(i, 0, 255, 0, 0.1)

            for i in [CLK.VOIDPRO_L, CLK.VOIDPRO_R]:
                ledOn(i, 0, 0, 0, 0.1)

            print("[INFO]", str(NewDeviceID[HeadPhoneID]), "Connected")
            return

    print("[INFO] No Corsair HeadPhone Found")


def FirstInit():
    RequestControl()

    DeviceInfo()
    DeviceID(DeviceList)

    KeyboardCheck()
    MousePadCheck()
    MouseCheck()
    HeadPhoneCheck()

    print("[INFO] Corsair ICUE Init Complete")


def KeyboardCol1(r,g,b,duration):
    ledOn(CLK.UpperLedBar1 , r , g , b ,duration)
    ledOn(CLK.G1 , r, g ,b ,duration)
    ledOn(CLK.G2 , r , g , b ,duration)
    ledOn(CLK.G3 , r , g , b ,duration)
    ledOn(CLK.G4 , r , g , b ,duration)
    ledOn(CLK.G5 , r , g , b ,duration)
    ledOn(CLK.G6 , r , g , b ,duration)

def KeyboardCol2(r,g,b,duration):
    ledOn(CLK.UpperLedBar2 , r , g , b ,duration)
    ledOn(CLK.Escape , r , g , b ,duration)
    ledOn(CLK.GraveAccentAndTilde , r , g , b ,duration)
    ledOn(CLK.Tab , r , g , b ,duration)
    ledOn(CLK.CapsLock , r , g , b ,duration)
    ledOn(CLK.LeftShift , r , g , b ,duration)
    ledOn(CLK.LeftCtrl , r , g , b ,duration)

def KeyboardCol3(r,g,b,duration):
    ledOn(CLK.UpperLedBar3 , r , g , b ,duration)
    ledOn(CLK.F1, r, g, b , duration)
    ledOn(CLK._1 ,r, g, b , duration)
    ledOn(CLK.Q, r, g, b , duration)
    ledOn(CLK.A, r, g, b , duration)
    ledOn(CLK.LeftGui ,r, g, b , duration)

def KeyboardCol4(r,g,b,duration):
    ledOn(CLK.UpperLedBar4 , r , g ,b ,duration)
    ledOn(CLK.Brightness,r,g,b,duration)
    ledOn(CLK.F2 , r , g ,b ,duration)
    ledOn(CLK._2 , r , g ,b ,duration)
    ledOn(CLK.W , r , g ,b ,duration)
    ledOn(CLK.S , r , g ,b ,duration)
    ledOn(CLK.Z , r , g ,b ,  duration)
    ledOn(CLK.LeftAlt , r , g ,b ,duration)

def KeyboardCol5(r,g,b,duration):
    ledOn(CLK.UpperLedBar5 , r , g ,b ,duration)
    ledOn(CLK.WinLock,r,g,b,duration)
    ledOn(CLK.F3 , r, g ,b , duration)
    ledOn(CLK._3 , r , g ,b ,duration)
    ledOn(CLK.E , r , g ,b ,duration)
    ledOn(CLK.D , r , g ,b ,duration)
    ledOn(CLK.X , r , g ,b ,duration)

def KeyboardCol6(r,g,b,duration):
    ledOn(CLK.UpperLedBar6 , r ,g ,b ,duration)
    ledOn(CLK.F4 , r ,g , b , duration)
    ledOn(CLK._4  , r ,g , b , duration)
    ledOn(CLK._5  , r ,g , b , duration)
    ledOn(CLK.R , r ,g , b , duration)
    ledOn(CLK.F , r ,g , b , duration)
    ledOn(CLK.C , r ,g , b , duration)

def KeyboardCol7(r,g,b,duration):
    ledOn(CLK.UpperLedBar7 , r , g ,b ,duration)
    ledOn(CLK.F5  , r ,g , b , duration)
    ledOn(CLK._6  , r ,g , b , duration)
    ledOn(CLK.T  , r ,g , b , duration)
    ledOn(CLK.G  , r ,g , b , duration)
    ledOn(CLK.V  , r ,g , b , duration)

def KeyboardCol8(r,g,b,duration):
    ledOn(CLK.UpperLedBar8  , r ,g , b , duration)
    ledOn(CLK.F6  , r ,g , b , duration)
    ledOn(CLK._7  , r ,g , b , duration)
    ledOn(CLK.Y  , r ,g , b , duration)
    ledOn(CLK.H  , r ,g , b , duration)
    ledOn(CLK.B  , r ,g , b , duration)
    ledOn(CLK.Space  , r ,g , b , duration)

def KeyboardCol9(r,g,b,duration):
    ledOn(CLK. UpperLedBar9 , r ,g , b , duration)
    ledOn(CLK.F7  , r ,g , b , duration)
    ledOn(CLK._8  , r ,g , b , duration)
    ledOn(CLK.U  , r ,g , b , duration)
    ledOn(CLK.J  , r ,g , b , duration)
    ledOn(CLK.N  , r ,g , b , duration)

def KeyboardCol10(r,g,b,duration):
    ledOn(CLK.F8  , r ,g , b , duration)
    ledOn(CLK._9  , r ,g , b , duration)
    ledOn(CLK.I  , r ,g , b , duration)
    ledOn(CLK.K  , r ,g , b , duration)
    ledOn(CLK.M  , r ,g , b , duration)

def KeyboardCol11(r,g,b,duration):
    ledOn(CLK._0  , r ,g , b , duration)
    ledOn(CLK.O  , r ,g , b , duration)
    ledOn(CLK.L  , r ,g , b , duration)
    ledOn(CLK.CommaAndLessThan  , r ,g , b , duration)

def KeyboardCol12(r,g,b,duration):
    ledOn(CLK. UpperLedBar10 , r ,g , b , duration)
    ledOn(CLK.F9, r, g, b , duration)
    ledOn(CLK.MinusAndUnderscore, r, g, b , duration)
    ledOn(CLK.P, r, g, b , duration)
    ledOn(CLK.SemicolonAndColon, r, g, b , duration)
    ledOn(CLK.PeriodAndBiggerThan, r, g, b , duration)
    ledOn(CLK.RightAlt, r, g, b , duration)

def KeyboardCol13(r,g,b,duration):
    ledOn(CLK.UpperLedBar11, r, g, b , duration)
    ledOn(CLK.F10, r, g, b , duration)
    ledOn(CLK.EqualsAndPlus, r, g, b , duration)
    ledOn(CLK.BracketLeft, r, g, b , duration)
    ledOn(CLK.ApostropheAndDoubleQuote, r, g, b , duration)
    ledOn(CLK.SlashAndQuestionMark, r, g, b , duration)
    ledOn(CLK.RightGui, r, g, b , duration)

def KeyboardCol14(r,g,b,duration):
    ledOn(CLK.UpperLedBar12, r, g, b , duration)
    ledOn(CLK.F11, r, g, b , duration)
    ledOn(CLK.BracketRight, r, g, b , duration)
    ledOn(CLK.Application, r, g, b , duration)


def KeyboardCol15(r,g,b,duration):
    ledOn(CLK.F12, r, g, b , duration)
    ledOn(CLK.Backspace, r, g, b , duration)
    ledOn(CLK.Backslash, r, g, b , duration)
    ledOn(CLK.Enter, r, g, b , duration)
    ledOn(CLK.RightShift, r, g, b , duration)
    ledOn(CLK.RightCtrl, r, g, b , duration)

def KeyboardCol16(r,g,b,duration):
    ledOn(CLK.UpperLedBar13, r, g, b , duration)
    ledOn(CLK.PrintScreen, r, g, b , duration)
    ledOn(CLK.Insert, r, g, b , duration)
    ledOn(CLK.Delete, r, g, b , duration)
    ledOn(CLK.LeftArrow, r, g, b , duration)

def KeyboardCol17(r,g,b,duration):
    ledOn(CLK.UpperLedBar14, r, g, b , duration)
    ledOn(CLK.ScrollLock, r, g, b , duration)
    ledOn(CLK.Home, r, g, b , duration)
    ledOn(CLK.End, r, g, b , duration)
    ledOn(CLK.UpArrow, r, g, b , duration)
    ledOn(CLK.DownArrow, r, g, b , duration)

def KeyboardCol18(r,g,b,duration):
    ledOn(CLK.UpperLedBar15, r, g, b , duration)
    ledOn(CLK.PauseBreak, r, g, b , duration)
    ledOn(CLK.PageUp, r, g, b , duration)
    ledOn(CLK.PageDown, r, g, b , duration)
    ledOn(CLK.RightArrow, r, g, b , duration)

def KeyboardCol19(r,g,b,duration):
    ledOn(CLK.UpperLedBar16, r, g, b , duration)
    ledOn(CLK.Mute, r, g, b , duration)
    ledOn(CLK.Stop, r, g, b , duration)
    ledOn(CLK.NumLock, r, g, b , duration)
    ledOn(CLK.Keypad7, r, g, b , duration)
    ledOn(CLK.Keypad4, r, g, b , duration)
    ledOn(CLK.Keypad1, r, g, b , duration)
    ledOn(CLK.Keypad0, r, g, b , duration)

def KeyboardCol20(r,g,b,duration):
    ledOn(CLK.ScanPreviousTrack, r, g, b , duration)
    ledOn(CLK.KeypadSlash, r, g, b , duration)
    ledOn(CLK.Keypad8, r, g, b , duration)
    ledOn(CLK.Keypad5, r, g, b , duration)
    ledOn(CLK.Keypad2, r, g, b , duration)

def KeyboardCol21(r,g,b,duration):
    ledOn(CLK.UpperLedBar17, r, g, b , duration)
    ledOn(CLK.PlayPause, r, g, b , duration)
    ledOn(CLK.KeypadAsterisk, r, g, b , duration)
    ledOn(CLK.Keypad9, r, g, b , duration)
    ledOn(CLK.Keypad6, r, g, b , duration)
    ledOn(CLK.Keypad3, r, g, b , duration)
    ledOn(CLK.KeypadPeriodAndDelete, r, g, b , duration)

def KeyboardCol22(r,g,b,duration):
    ledOn(CLK.UpperLedBar18, r, g, b , duration)
    ledOn(CLK.UpperLedBar19, r, g, b , duration)
    ledOn(CLK.ScanNextTrack, r, g, b , duration)
    ledOn(CLK.KeypadMinus, r, g, b , duration)
    ledOn(CLK.KeypadPlus, r, g, b , duration)
    ledOn(CLK.KeypadEnter, r, g, b , duration)

def KeyboardSetdAll(r,g,b,duration):
    KeyboardCol1(r,g,b,duration)
    KeyboardCol2(r,g,b,duration)
    KeyboardCol3(r,g,b,duration)
    KeyboardCol4(r,g,b,duration)
    KeyboardCol5(r,g,b,duration)
    KeyboardCol6(r,g,b,duration)
    KeyboardCol7(r,g,b,duration)
    KeyboardCol8(r,g,b,duration)
    KeyboardCol9(r,g,b,duration)
    KeyboardCol10(r,g,b,duration)
    KeyboardCol11(r,g,b,duration)
    KeyboardCol12(r,g,b,duration)
    KeyboardCol13(r,g,b,duration)
    KeyboardCol14(r,g,b,duration)
    KeyboardCol15(r,g,b,duration)
    KeyboardCol16(r,g,b,duration)
    KeyboardCol17(r,g,b,duration)
    KeyboardCol18(r,g,b,duration)
    KeyboardCol19(r,g,b,duration)
    KeyboardCol20(r,g,b,duration)
    KeyboardCol21(r,g,b,duration)
    KeyboardCol22(r,g,b,duration)

def MM800Col1(r,g,b,duration):
    ledOn(CLK.MM800_1,r,g,b,duration)
    ledOn(CLK.MM800_2,r,g,b,duration)
    ledOn(CLK.MM800_3,r,g,b,duration)
    ledOn(CLK.MM800_4,r,g,b,duration)
    ledOn(CLK.MM800_5,r,g,b,duration)

def MM800Col2(r,g,b,duration):
    ledOn(CLK.MM800_6,r,g,b,duration)

def MM800Col3(r,g,b,duration):
    ledOn(CLK.MM800_7,r,g,b,duration)

def MM800Col4(r,g,b,duration):
    ledOn(CLK.MM800_8,r,g,b,duration)

def MM800Col5(r,g,b,duration):
    ledOn(CLK.MM800_9,r,g,b,duration)

def MM800Col6(r,g,b,duration):
    ledOn(CLK.MM800_10,r,g,b,duration)

def MM800Col7(r,g,b,duration):
    ledOn(CLK.MM800_11,r,g,b,duration)
    ledOn(CLK.MM800_12,r,g,b,duration)
    ledOn(CLK.MM800_13,r,g,b,duration)
    ledOn(CLK.MM800_14,r,g,b,duration)
    ledOn(CLK.MM800_15,r,g,b,duration)

def MM800SetAll(r,g,b,duration):
    MM800Col1(r,g,b,duration)
    MM800Col2(r,g,b,duration)
    MM800Col3(r,g,b,duration)
    MM800Col4(r,g,b,duration)
    MM800Col5(r,g,b,duration)
    MM800Col6(r,g,b,duration)
    MM800Col7(r,g,b,duration)

