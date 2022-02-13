"""
@project : PyPeripheral
@author : Gooday2die
@date : 2022-02-13
@file : $NAME.py
"""

from PyPeripheral.PyPeripheral.Wrappers import All


def static_color(r, g, b):
    """
    Function for Setting all the keys rainbow shift.
    step is the parameter for how fast the rainbow should shift.
    """
    sdk_object = All.SDK()
    sdk_object.connect()
    while True:
        sdk_object.set_rgb({"ALL": (r, g, b)})


if __name__ == '__main__':
    static_color(255, 0, 0)
