"""
@project : PyPeripheral
@author : Gooday2die
@date : 2022-02-13
@file : ScreenReactive.py
"""

from __future__ import print_function
import numpy as np
import scipy.cluster
import mss
from PIL import Image
import asyncio

from PyPeripheral import All


def return_rgb():
    with mss.mss() as sct:
        # Get rid of the first, as it represents the "All in One" monitor:
        for num, monitor in enumerate(sct.monitors[1:], 1):
            # Get raw pixels from the screen
            sct_img = sct.grab(monitor)

            # Create the Image
            im = Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX")
        im = im.resize((150, 150))  # optional, to reduce time

        num_clusters = 1

        ar = np.asarray(im)
        shape = ar.shape
        ar = ar.reshape(np.product(shape[:2]), shape[2]).astype(float)

        codes, dist = scipy.cluster.vq.kmeans(ar, num_clusters)
        # Codes are stored as a matrix
        # 0 : R , 1 : G , 2 : B

        for i in range(len(codes)):
            lst = list()
            lst.append(int(codes[i][0]))
            lst.append(int(codes[i][1]))
            lst.append(int(codes[i][2]))

        return lst


async def screen_reactive(sdk_object):
    while True:
        new_list = return_rgb()
        sdk_object.set_rgb({"ALL": (new_list[0], new_list[1], new_list[2])})


if __name__ == '__main__':
    sdk_object = All.SDK()
    sdk_object.connect()
    asyncio.run(screen_reactive(sdk_object))
