"""
@project : PyPeripheral
@author : Gooday2die
@date : 2022-02-13
@file : RainbowAll.py
"""

from PyPeripheral import All


def rainbow_all(step):
    sdk_object = All.SDK()
    sdk_object.connect()
    """
    Function for Setting all the keys rainbow shift.
    step is the parameter for how fast the rainbow should shift.
    """
    while True:
        for g in range(0, 255, step):
            sdk_object.set_rgb({"ALL": (255, g, 0)})

        for r in range(255, 0, -step):
            sdk_object.set_rgb({"ALL": (r, 255, 0)})

        for b in range(0, 255, step):
            sdk_object.set_rgb({"ALL": (0, 255, b)})

        for g in range(255, 0, -step):
            sdk_object.set_rgb({"ALL": (0, g, 255)})

        for r in range(0, 255, step):
            sdk_object.set_rgb({"ALL": (r, 255, 0)})

        for b in range(255, 0, -step):
            sdk_object.set_rgb({"ALL": (255, 0, b)})


if __name__ == '__main__':
    rainbow_all(10)
