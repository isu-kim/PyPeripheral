from __future__ import print_function
from Wrappers import Corsair
from Wrappers import Razer
from main import mainInit
import main
import numpy as np
import scipy.cluster
import mss
from PIL import Image
import time

global debug
debug = None

def debugON():
    global debug
    debug = True

def debugOFF():
    global debug
    debug = False

def returnRGB():
    with mss.mss() as sct:
        # Get rid of the first, as it represents the "All in One" monitor:
        for num, monitor in enumerate(sct.monitors[1:], 1):
            # Get raw pixels from the screen
            sct_img = sct.grab(monitor)

            # Create the Image
            im = Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX")
        im = im.resize((150, 150))      # optional, to reduce time

        NUM_CLUSTERS = 1


        ar = np.asarray(im)
        shape = ar.shape
        ar = ar.reshape(scipy.product(shape[:2]), shape[2]).astype(float)

        codes, dist = scipy.cluster.vq.kmeans(ar, NUM_CLUSTERS)
        #Codes are stored as  a matrix
        # 0 : R , 1 : G , 2 : B

        for i in range(len(codes)):
            list = []
            #print(int(codes[i][0]))
            #print(int(codes[i][1]))
            #print(int(codes[i][2]))
            list.append(int(codes[i][0]))
            list.append(int(codes[i][1]))
            list.append(int(codes[i][2]))

            '''

            if debug:
                print(' #%02x%02x%02x' % (int(codes[i][0]), int(codes[i][1]), int(codes[i][2])), end=' / ')
            '''

        return list
'''
while True:
    returnRGB()
    time.sleep(0.1)
'''

def ask():
    global debug

    print("[INFO] Turn Debug ON ?")
    answer = (input("True/False : "))
    anslist = ["True", "False" , "true" , "false"]
    posit = ["True", "true"]
    negit = ["False" , "false"]

    if answer not in anslist:
        ask()

    else:
        if answer in posit:
            debugON()

        if answer in negit:
            debugOFF()

    #print(debug)

def screenreactive():
    global debug

    while True:
        newlist = returnRGB()
        main.SetAllColor(newlist[0], newlist[1], newlist[2], 0)
        if debug:
            print("[INFO] Dominant Color : ("+str(newlist[0])+"," +str(newlist[1])+","+str(newlist[2])+")")


if __name__ == '__main__':
    ask()
    #print(debug)
    if debug:
        print("[INFO] Debug Turned ON")
    else:
        print("[INFO] Debug Turned OFF")

    screenreactive()

