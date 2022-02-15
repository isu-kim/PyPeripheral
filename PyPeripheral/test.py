# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import re
import subprocess

from PyPeripheral import All


if __name__ == "__main__":
    a = All.SDK()
    a.connect()
    print(a.get_all_device_information())
    a.disable()
"""    r = Razer.SDK()
    r.connect()
    a = r.get_all_device_information()
    print(a)
    print(r.get_device_information(0))
    print(r.get_device_information(1))
    r.disable()"""
