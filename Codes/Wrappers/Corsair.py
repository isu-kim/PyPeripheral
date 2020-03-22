import time
from cue_sdk import *

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


def debug_on():
    print("[Info] Corsair ICUE Debug Mode ON")
    global debug
    debug = True


def debug_off():
    print("[Info] Corsair ICUE Debug Mode OFF")
    global debug
    debug = False


def dev_count():
    return cue.get_device_count()


def device_info():
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


def request_control():
    cue.RequestControl(CAM.ExclusiveLightingControl)
    print("[INFO] Successfully Requested Corsair ICUE Control")


def release_control():
    cue.ReleaseControl(CAM.ExclusiveLightingControl)
    print("[INFO] Successfully Released Corsair ICUE Control")


def black_led(led_id):
    led_color = CorsairLedColor(led_id, 0, 0, 0)
    cue.set_led_colors(led_color)


def led_on(led_id, r_val, g_val, b_val, duration):
    global debug

    if debug:
        print("[DEBUG] LED_ID :", str(led_id), "R :", str(r_val), "G :", str(g_val), " B :", str(b_val), "Duration :",
              str(duration))

    led_color = CorsairLedColor(led_id, r_val, g_val, b_val)
    cue.set_led_colors(led_color)
    time.sleep(duration)  # for immediate action, set duration to 0 , think duration as delay


def led_smooth_on(led_id, r_val, g_val, b_val, duration):
    global debug
    for x in range_float(0, 2, 0.1):
        n_rval = int((1 - abs(x - 1)) * r_val)
        n_gval = int((1 - abs(x - 1)) * g_val)
        n_bval = int((1 - abs(x - 1)) * b_val)
        if debug:
            print("[DEBUG] LED_ID :", str(led_id), "R :", str(n_rval), "G :", str(n_gval), " B :", str(n_bval),
                  "Duration :", str(duration))
        led_color = CorsairLedColor(led_id, n_rval, n_gval, n_bval)
        cue.set_led_colors(led_color)
        time.sleep(duration)


def device_id(device_list):
    global NewDeviceID
    global debug

    for i in range(len(device_list)):
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


def keyboard_check():
    global NewDeviceID
    global DeviceType

    for i in range(len(NewDeviceID)):
        if NewDeviceID[i][0] == '2':
            keyboard_id = i
            NewDeviceID[keyboard_id] = NewDeviceID[keyboard_id].replace("2", "").replace("_CDT", "")
            if NewDeviceID[keyboard_id] == "K95 RGB PLATINUM":
                led_on(CLK.G1, 0, 255, 0, 0.1)
                led_on(CLK.G2, 0, 255, 0, 0.1)
                led_on(CLK.G3, 0, 255, 0, 0.1)
                led_on(CLK.G4, 0, 255, 0, 0.1)
                led_on(CLK.G5, 0, 255, 0, 0.1)
                led_on(CLK.G6, 0, 255, 0, 0.1)

                led_on(CLK.G1, 0, 0, 0, 0.1)
                led_on(CLK.G2, 0, 0, 0, 0.1)
                led_on(CLK.G3, 0, 0, 0, 0.1)
                led_on(CLK.G4, 0, 0, 0, 0.1)
                led_on(CLK.G5, 0, 0, 0, 0.1)
                led_on(CLK.G6, 0, 0, 0, 0.1)

                '''
                I do know that using for or while loop would be more effective way to do this.
                However, this process is to check all the dependencies were correctly installed. 

                If the importing cue_sdk module was not complete nor successful, CLK.G keys would be showing errors on 
                the CLK is not defined.
                '''

                for j in range(170, 188, 1):
                    led_on(j, 0, 255, 0, 0.01)
                    led_on(j + 1, 0, 255, 0, 0.01)

                for j in range(170, 188, 1):
                    led_on(j, 0, 0, 0, 0.01)
                    led_on(j + 1, 0, 0, 0, 0.01)

                for j in range(188, 170, -1):
                    led_on(j, 0, 255, 0, 0.01)
                    led_on(j + 1, 0, 255, 0, 0.01)

                for j in range(188, 170, -1):
                    led_on(j, 0, 0, 0, 0.01)
                    led_on(j + 1, 0, 0, 0, 0.01)

                '''
                If this function was correctly executed, it means that there would be no issues when controlling Corsair
                ICUE SDK. At least for me, my pheperials (K95 RGB , Glaive , Void , MM800) were ready for me to control 
                LEDs.

                If this crashes, The key LED mapping would be mismatched.  

                '''

            else:
                for j in range(2):
                    led_smooth_on(CLK.Space, 0, 255, 0, 0.01)

                for j in range(1, 12, 1):
                    led_on(j, 0, 255, 0, 0.1)

                for j in range(1, 12, 1):
                    led_on(j, 0, 0, 0, 0.1)
                    
                led_on(CLK.F12, 0, 0, 0, 0.1)

            print("[INFO]", str(NewDeviceID[keyboard_id]), "Connected")
            return

    print("[INFO] No Corsair Keyboard Found")


def mouse_pad_check():
    global NewDeviceID
    global DeviceType

    for i in range(len(NewDeviceID)):
        if NewDeviceID[i][0] == '4':
            mouse_pad_id = i
            NewDeviceID[mouse_pad_id] = NewDeviceID[mouse_pad_id].replace("4", "").replace("_CDT", "")

            if "MM800RGB" in NewDeviceID:
                for j in range(2):
                    led_smooth_on(CLK.MM800_1, 0, 255, 0, 0.01)

                for j in range(155, 169, 1):
                    led_on(j, 0, 255, 0, 0.1)

                for j in range(155, 169, 1):
                    led_on(j, 0, 0, 0, 0.1)

                print("[INFO]", str(NewDeviceID[mouse_pad_id]), "Connected")
                return

    print("[INFO] No Corsair Mouse Pad Found")


def mouse_check():
    global NewDeviceID
    global DeviceType

    for i in range(len(NewDeviceID)):
        if NewDeviceID[i][0] == '1':
            mouse_id = i
            NewDeviceID[mouse_id] = NewDeviceID[mouse_id].replace("1", "").replace("_CDT", "")

        if "GLAIVE RGB" in NewDeviceID:
            for j in range(2):
                led_smooth_on(CLK.GLAV_2, 0, 255, 0, 0.01)

            for j in [CLK.GLAV_1, CLK.GLAV_2, CLK.GLAV_3]:
                led_on(j, 0, 255, 0, 0.1)

            for j in [CLK.GLAV_1, CLK.GLAV_2, CLK.GLAV_3]:
                led_on(j, 0, 0, 0, 0.1)

                print("[INFO]", str(NewDeviceID[mouse_id]), "Connected")
                return

    print("[INFO] No Corsair Mouse Found")


def headphone_check():
    global NewDeviceID
    global DeviceType

    for i in range(len(NewDeviceID)):
        if NewDeviceID[i][0] == '3':
            headphone_id = i
            NewDeviceID[headphone_id] = NewDeviceID[headphone_id].replace("3", "").replace("_CDT", "")

        if "VOID PRO USB" in NewDeviceID:
            for j in range(2):
                led_smooth_on(CLK.VOIDPRO_L, 0, 255, 0, 0.01)

            for j in [CLK.VOIDPRO_L, CLK.VOIDPRO_R]:
                led_on(j, 0, 255, 0, 0.1)

            for j in [CLK.VOIDPRO_L, CLK.VOIDPRO_R]:
                led_on(j, 0, 0, 0, 0.1)

                print("[INFO]", str(NewDeviceID[headphone_id]), "Connected")
                return

    print("[INFO] No Corsair HeadPhone Found")


def first_init():
    request_control()

    device_info()
    device_id(DeviceList)

    keyboard_check()
    mouse_pad_check()
    mouse_check()
    headphone_check()

    print("[INFO] Corsair ICUE Init Complete")


def keyboard_col_1(r, g, b, duration):
    led_on(CLK.UpperLedBar1, r, g, b, duration)
    led_on(CLK.G1, r, g, b, duration)
    led_on(CLK.G2, r, g, b, duration)
    led_on(CLK.G3, r, g, b, duration)
    led_on(CLK.G4, r, g, b, duration)
    led_on(CLK.G5, r, g, b, duration)
    led_on(CLK.G6, r, g, b, duration)


def keyboard_col_2(r, g, b, duration):
    led_on(CLK.UpperLedBar2, r, g, b, duration)
    led_on(CLK.Escape, r, g, b, duration)
    led_on(CLK.GraveAccentAndTilde, r, g, b, duration)
    led_on(CLK.Tab, r, g, b, duration)
    led_on(CLK.CapsLock, r, g, b, duration)
    led_on(CLK.LeftShift, r, g, b, duration)
    led_on(CLK.LeftCtrl, r, g, b, duration)


def keyboard_col_3(r, g, b, duration):
    led_on(CLK.UpperLedBar3, r, g, b, duration)
    led_on(CLK.F1, r, g, b, duration)
    led_on(CLK._1, r, g, b, duration)
    led_on(CLK.Q, r, g, b, duration)
    led_on(CLK.A, r, g, b, duration)
    led_on(CLK.LeftGui, r, g, b, duration)


def keyboard_col4(r, g, b, duration):
    led_on(CLK.UpperLedBar4, r, g, b, duration)
    led_on(CLK.Brightness, r, g, b, duration)
    led_on(CLK.F2, r, g, b, duration)
    led_on(CLK._2, r, g, b, duration)
    led_on(CLK.W, r, g, b, duration)
    led_on(CLK.S, r, g, b, duration)
    led_on(CLK.Z, r, g, b, duration)
    led_on(CLK.LeftAlt, r, g, b, duration)


def keyboard_col5(r, g, b, duration):
    led_on(CLK.UpperLedBar5, r, g, b, duration)
    led_on(CLK.WinLock, r, g, b, duration)
    led_on(CLK.F3, r, g, b, duration)
    led_on(CLK._3, r, g, b, duration)
    led_on(CLK.E, r, g, b, duration)
    led_on(CLK.D, r, g, b, duration)
    led_on(CLK.X, r, g, b, duration)


def keyboard_col6(r, g, b, duration):
    led_on(CLK.UpperLedBar6, r, g, b, duration)
    led_on(CLK.F4, r, g, b, duration)
    led_on(CLK._4, r, g, b, duration)
    led_on(CLK._5, r, g, b, duration)
    led_on(CLK.R, r, g, b, duration)
    led_on(CLK.F, r, g, b, duration)
    led_on(CLK.C, r, g, b, duration)


def keyboard_col7(r, g, b, duration):
    led_on(CLK.UpperLedBar7, r, g, b, duration)
    led_on(CLK.F5, r, g, b, duration)
    led_on(CLK._6, r, g, b, duration)
    led_on(CLK.T, r, g, b, duration)
    led_on(CLK.G, r, g, b, duration)
    led_on(CLK.V, r, g, b, duration)


def keyboard_col8(r, g, b, duration):
    led_on(CLK.UpperLedBar8, r, g, b, duration)
    led_on(CLK.F6, r, g, b, duration)
    led_on(CLK._7, r, g, b, duration)
    led_on(CLK.Y, r, g, b, duration)
    led_on(CLK.H, r, g, b, duration)
    led_on(CLK.B, r, g, b, duration)
    led_on(CLK.Space, r, g, b, duration)


def keyboard_col9(r, g, b, duration):
    led_on(CLK. UpperLedBar9, r, g, b, duration)
    led_on(CLK.F7, r, g, b, duration)
    led_on(CLK._8, r, g, b, duration)
    led_on(CLK.U, r, g, b, duration)
    led_on(CLK.J, r, g, b, duration)
    led_on(CLK.N, r, g, b, duration)


def keyboard_col10(r, g, b, duration):
    led_on(CLK.F8, r, g, b, duration)
    led_on(CLK._9, r, g, b, duration)
    led_on(CLK.I, r, g, b, duration)
    led_on(CLK.K, r, g, b, duration)
    led_on(CLK.M, r, g, b, duration)


def keyboard_col11(r, g, b, duration):
    led_on(CLK._0, r, g, b, duration)
    led_on(CLK.O, r, g, b, duration)
    led_on(CLK.L, r, g, b, duration)
    led_on(CLK.CommaAndLessThan, r, g, b, duration)


def keyboard_col12(r, g, b, duration):
    led_on(CLK. UpperLedBar10, r, g, b, duration)
    led_on(CLK.F9, r, g, b, duration)
    led_on(CLK.MinusAndUnderscore, r, g, b, duration)
    led_on(CLK.P, r, g, b, duration)
    led_on(CLK.SemicolonAndColon, r, g, b, duration)
    led_on(CLK.PeriodAndBiggerThan, r, g, b, duration)
    led_on(CLK.RightAlt, r, g, b, duration)


def keyboard_col13(r, g, b, duration):
    led_on(CLK.UpperLedBar11, r, g, b, duration)
    led_on(CLK.F10, r, g, b, duration)
    led_on(CLK.EqualsAndPlus, r, g, b, duration)
    led_on(CLK.BracketLeft, r, g, b, duration)
    led_on(CLK.ApostropheAndDoubleQuote, r, g, b, duration)
    led_on(CLK.SlashAndQuestionMark, r, g, b, duration)
    led_on(CLK.RightGui, r, g, b, duration)


def keyboard_col14(r, g, b, duration):
    led_on(CLK.UpperLedBar12, r, g, b, duration)
    led_on(CLK.F11, r, g, b, duration)
    led_on(CLK.BracketRight, r, g, b, duration)
    led_on(CLK.Application, r, g, b, duration)


def keyboard_col15(r, g, b, duration):
    led_on(CLK.F12, r, g, b, duration)
    led_on(CLK.Backspace, r, g, b, duration)
    led_on(CLK.Backslash, r, g, b, duration)
    led_on(CLK.Enter, r, g, b, duration)
    led_on(CLK.RightShift, r, g, b, duration)
    led_on(CLK.RightCtrl, r, g, b, duration)


def keyboard_col16(r, g, b, duration):
    led_on(CLK.UpperLedBar13, r, g, b, duration)
    led_on(CLK.PrintScreen, r, g, b, duration)
    led_on(CLK.Insert, r, g, b, duration)
    led_on(CLK.Delete, r, g, b, duration)
    led_on(CLK.LeftArrow, r, g, b, duration)


def keyboard_col17(r, g, b, duration):
    led_on(CLK.UpperLedBar14, r, g, b, duration)
    led_on(CLK.ScrollLock, r, g, b, duration)
    led_on(CLK.Home, r, g, b, duration)
    led_on(CLK.End, r, g, b, duration)
    led_on(CLK.UpArrow, r, g, b, duration)
    led_on(CLK.DownArrow, r, g, b, duration)


def keyboard_col18(r, g, b, duration):
    led_on(CLK.UpperLedBar15, r, g, b, duration)
    led_on(CLK.PauseBreak, r, g, b, duration)
    led_on(CLK.PageUp, r, g, b, duration)
    led_on(CLK.PageDown, r, g, b, duration)
    led_on(CLK.RightArrow, r, g, b, duration)


def keyboard_col19(r, g, b, duration):
    led_on(CLK.UpperLedBar16, r, g, b, duration)
    led_on(CLK.Mute, r, g, b, duration)
    led_on(CLK.Stop, r, g, b, duration)
    led_on(CLK.NumLock, r, g, b, duration)
    led_on(CLK.Keypad7, r, g, b, duration)
    led_on(CLK.Keypad4, r, g, b, duration)
    led_on(CLK.Keypad1, r, g, b, duration)
    led_on(CLK.Keypad0, r, g, b, duration)


def keyboard_col20(r, g, b, duration):
    led_on(CLK.ScanPreviousTrack, r, g, b, duration)
    led_on(CLK.KeypadSlash, r, g, b, duration)
    led_on(CLK.Keypad8, r, g, b, duration)
    led_on(CLK.Keypad5, r, g, b, duration)
    led_on(CLK.Keypad2, r, g, b, duration)


def keyboard_col21(r, g, b, duration):
    led_on(CLK.UpperLedBar17, r, g, b, duration)
    led_on(CLK.PlayPause, r, g, b, duration)
    led_on(CLK.KeypadAsterisk, r, g, b, duration)
    led_on(CLK.Keypad9, r, g, b, duration)
    led_on(CLK.Keypad6, r, g, b, duration)
    led_on(CLK.Keypad3, r, g, b, duration)
    led_on(CLK.KeypadPeriodAndDelete, r, g, b, duration)


def keyboard_col22(r, g, b, duration):
    led_on(CLK.UpperLedBar18, r, g, b, duration)
    led_on(CLK.UpperLedBar19, r, g, b, duration)
    led_on(CLK.ScanNextTrack, r, g, b, duration)
    led_on(CLK.KeypadMinus, r, g, b, duration)
    led_on(CLK.KeypadPlus, r, g, b, duration)
    led_on(CLK.KeypadEnter, r, g, b, duration)


def keyboard_col(index, r, g, b, duration):
    if debug:
        print("keyboard_col"+str(index)+"("+str(r)+","+str(g)+","+str(b)+","+str(duration)+")")
    exec("keyboard_col"+str(index)+"("+str(r)+","+str(g)+","+str(b)+","+str(duration)+")")


def keyboard_set_all(r, g, b, duration):
    for i in range(1, 23, 1):
        keyboard_col(i, r, g, b, duration)


def mm800_col_1(r, g, b, duration):
    led_on(CLK.MM800_1, r, g, b, duration)
    led_on(CLK.MM800_2, r, g, b, duration)
    led_on(CLK.MM800_3, r, g, b, duration)
    led_on(CLK.MM800_4, r, g, b, duration)
    led_on(CLK.MM800_5, r, g, b, duration)


def mm800_col_2(r, g, b, duration):
    led_on(CLK.MM800_6, r, g, b, duration)


def mm800_col_3(r, g, b, duration):
    led_on(CLK.MM800_7, r, g, b, duration)


def mm800_col_4(r, g, b, duration):
    led_on(CLK.MM800_8, r, g, b, duration)


def mm800_col_5(r, g, b, duration):
    led_on(CLK.MM800_9, r, g, b, duration)
    

def mm800_col_6(r, g, b, duration):
    led_on(CLK.MM800_10, r, g, b, duration)


def mm800_col_7(r, g, b, duration):
    led_on(CLK.MM800_11, r, g, b, duration)
    led_on(CLK.MM800_12, r, g, b, duration)
    led_on(CLK.MM800_13, r, g, b, duration)
    led_on(CLK.MM800_14, r, g, b, duration)
    led_on(CLK.MM800_15, r, g, b, duration)


def mm800_col(index, r, g, b, duration):
    if debug:
        print("mm800_col_"+str(index)+"("+str(r)+","+str(g)+","+str(b)+","+str(duration)+")")
    exec("mm800_col_"+str(index)+"("+str(r)+","+str(g)+","+str(b)+","+str(duration)+")")


def mm800_set_all(r, g, b, duration):
    for i in range(1, 8, 1):
        mm800_col(i, r, g, b, duration)
