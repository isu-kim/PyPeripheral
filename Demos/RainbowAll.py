"""
@project : PyPeripheral
@author : Gooday2die
@date : 2022-02-13
@file : RainbowAll.py
"""
import threading
import time

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
        self.delay = 0

    def run(self, **kwargs):
        """
        An abstract method for running this demo.
        This method will have main features of the demo script.
        :return: returns None
        """
        self.thread = threading.Thread(target=self.__rainbow_all)
        self.is_running = True
        self.sdk_object = kwargs['sdk_object']
        self.delay = kwargs['delay']
        self.thread.start()

    def stop(self):
        """
        An abstract method for stopping this demo.
        This method will terminate the demo script and this object.
        :return: returns None
        """
        self.is_running = False
        self.thread.join()

    def __rainbow_all(self):
        """
        A function that does rainbow shifting
        :return: returns None
        """
        while True:
            for g in range(0, 255, 1):
                if not self.is_running:
                    return None
                self.sdk_object.set_rgb({"ALL": (255, g, 0)})
                time.sleep(self.delay)

            for r in range(255, 0, -1):
                if not self.is_running:
                    return None
                self.sdk_object.set_rgb({"ALL": (r, 255, 0)})
                time.sleep(self.delay)

            for b in range(0, 255, 1):
                if not self.is_running:
                    return None
                self.sdk_object.set_rgb({"ALL": (0, 255, b)})
                time.sleep(self.delay)

            for g in range(255, 0, -1):
                if not self.is_running:
                    return None
                self.sdk_object.set_rgb({"ALL": (0, g, 255)})
                time.sleep(self.delay)

            for r in range(0, 255, 1):
                if not self.is_running:
                    return None
                self.sdk_object.set_rgb({"ALL": (r, 0, 255)})
                time.sleep(self.delay)

            for b in range(255, 0, -1):
                if not self.is_running:
                    return None
                self.sdk_object.set_rgb({"ALL": (255, 0, b)})
                time.sleep(self.delay)


if __name__ == '__main__':
    sdk_object = All.SDK()
    sdk_object.connect()
    rainbow_all = Demo()
    rainbow_all.run(sdk_object=sdk_object, step=10)
