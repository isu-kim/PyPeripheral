from __future__ import print_function
from Wrappers import Corsair
from Wrappers import Razer
import main
import numpy as np
import scipy.cluster
import mss
from PIL import Image
import time



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
            print(int(codes[i][0]))
            print(int(codes[i][1]))
            print(int(codes[i][2]))
            list.append(int(codes[i][0]))
            list.append(int(codes[i][1]))
            list.append(int(codes[i][2]))


            print('#%02x%02x%02x' % (int(codes[i][0]), int(codes[i][1]), int(codes[i][2])))

        return list
'''
while True:
    returnRGB()
    time.sleep(0.1)
'''

while True:
    newlist = returnRGB()
    main.setEveryDeviceColor(newlist[0],newlist[1],newlist[2],0.0001)
    time.sleep(0.001)

