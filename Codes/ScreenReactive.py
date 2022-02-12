from __future__ import print_function
import main
import numpy as np
import scipy.cluster
import mss
from PIL import Image


global debug
debug = False


def debug_on():
    global debug
    debug = True


def debug_off():
    global debug
    debug = False


def return_rgb():
    with mss.mss() as sct:
        # Get rid of the first, as it represents the "All in One" monitor:
        for num, monitor in enumerate(sct.monitors[1:], 1):
            # Get raw pixels from the screen
            sct_img = sct.grab(monitor)

            # Create the Image
            im = Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX")
        im = im.resize((150, 150))      # optional, to reduce time

        num_clusters = 1

        ar = np.asarray(im)
        shape = ar.shape
        ar = ar.reshape(scipy.product(shape[:2]), shape[2]).astype(float)

        codes, dist = scipy.cluster.vq.kmeans(ar, num_clusters)
        # Codes are stored as a matrix
        # 0 : R , 1 : G , 2 : B

        for i in range(len(codes)):
            lst = list()
            lst.append(int(codes[i][0]))
            lst.append(int(codes[i][1]))
            lst.append(int(codes[i][2]))

        return lst


def ask():
    global debug

    print("[INFO] Turn Debug ON ?")
    answer = (input("True/False : "))
    ans_list = ["True", "False", "true", "false"]
    positive = ["True", "true"]
    negative = ["False", "false"]

    if answer not in ans_list:
        ask()

    else:
        if answer in positive:
            debug_on()

        if answer in negative:
            debug_off()


def screen_reactive(obj_set_color):
    global debug

    while True:
        new_list = return_rgb()
        obj_set_color.all(new_list[0], new_list[1], new_list[2], 0)

        if debug:
            print("[INFO] Dominant Color : ("+str(new_list[0])+"," + str(new_list[1])+","+str(new_list[2])+")")


if __name__ == '__main__':
    ask()
    main_debug = main.Debug()

    if debug:
        print("[INFO] Debug Turned ON")
        main_debug.all_on()
        
    else:
        print("[INFO] Debug Turned OFF")
        main_debug.all_off()

    dev_list = main.DevList()
    sdk_object = main.Sdks()
    init = main.InitTools(main_debug, dev_list, sdk_object)
    init.main_init()

    set_color = main.SetColor(sdk_object)

    screen_reactive(set_color)
