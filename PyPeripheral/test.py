# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random
import multiprocessing

from PyPeripheral.Wrappers import Corsair
from PyPeripheral.Wrappers import Razer
from PyPeripheral.Wrappers import All

if __name__ == "__main__":
    a = All.SDK()
    a.connect()

    """
    while True:
        for i in range(1, 255, 3):
            c.set_rgb({"ALL": (i, 0, 0)})
            r.set_rgb({"ALL": (i, 0, 0)})

        for i in range(1, 255, 3):
            c.set_rgb({"ALL": (255 - i, i, 0)})
            r.set_rgb({"ALL": (255 - i, i, 0)})

        for i in range(1, 255, 3):
            c.set_rgb({"ALL": (0, 255 - i, i)})
            r.set_rgb({"ALL": (0, 255 - i, i)})

        for i in range(1, 255, 3):
            c.set_rgb({"ALL": (i, 0, 255 - i)})
            r.set_rgb({"ALL": (i, 0, 255 - i )})
    """
    while True:
        red = random.randrange(0, 255, 1)
        g = random.randrange(0, 255, 1)
        b = random.randrange(0, 255, 1)
        a.set_rgb({"ALL": (red, g, b)})
