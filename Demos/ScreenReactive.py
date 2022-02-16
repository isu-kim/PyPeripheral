"""
@project : PyPeripheral
@author : Gooday2die
@date : 2022-02-13
@file : ScreenReactive.py
"""

from __future__ import print_function

import threading
import numpy as np
import scipy.cluster
import mss
from PIL import Image

from PyPeripheral import All
from abstractDemo import AbstractDemo


class Demo(AbstractDemo):
    def __init__(self):
        """
        An initializer method for class Demo in RainbowAll
        """
        self.thread = None
        self.is_running = False
        self.sdk_object = None
        self.r = 0
        self.g = 0
        self.b = 0

    def run(self, **kwargs):
        """
        An abstract method for running this demo.
        This method will have main features of the demo script.
        :return: returns None
        """
        self.thread = threading.Thread(target=self.__screen_reactive)
        self.sdk_object = kwargs['sdk_object']
        self.is_running = True
        self.thread.start()

    def stop(self):
        """
        An abstract method for stopping this demo.
        This method will terminate the demo script and this object.
        :return: returns None
        """
        self.is_running = False
        self.thread.join()

    def __return_rgb(self):
        """
        A method that returns the most dominant color of current screen
        This code is from https://stackoverflow.com/questions/3241929/python-find-dominant-most-common-color-in-an-image
        Edited a bit of code in order to work in our demo script
        :return: returns None
        """
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

            self.r = int(codes[0][0])
            self.g = int(codes[0][1])
            self.b = int(codes[0][2])

    def __screen_reactive(self):
        """
        A method that does screen reactive lightning
        :return: returns None
        """
        while self.is_running:
            self.sdk_object.set_rgb({"ALL": (self.r, self.g, self.b)})
        return


if __name__ == '__main__':
    sdk_object = All.SDK()
    sdk_object.connect()
    static_color = Demo()
    static_color.run(sdk_object=sdk_object)
