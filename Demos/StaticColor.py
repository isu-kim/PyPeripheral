"""
@project : PyPeripheral
@author : Gooday2die
@date : 2022-02-13
@file : StaticColor.py
"""

import threading

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
        self.thread = threading.Thread(target=self.__static_color)
        self.r = kwargs['r']
        self.g = kwargs['g']
        self.b = kwargs['b']
        self.sdk_object = kwargs['sdk_object']
        self.is_running = True
        self.thread.start()

    def stop(self):
        """
        An abstract method for stopping this demo.
        This method will terminate the demo script and this object.
        :return:
        """
        self.is_running = False
        self.thread.join()

    def __static_color(self):
        """
        A function that sets a single color over all devices
        :return: returns None
        """
        while True:
            self.sdk_object.set_rgb({"ALL": (self.r, self.g, self.b)})


if __name__ == '__main__':
    sdk_object = All.SDK()
    sdk_object.connect()
    static_color = Demo()
    static_color.run(sdk_object=sdk_object, r=255, g=255, b=255)
