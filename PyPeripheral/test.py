# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random

from PyPeripheral import Razer



if __name__ == "__main__":
    r = Razer.SDK()
    r.connect()
    r.get_all_device_information()
    r.disable()
