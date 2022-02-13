# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import time

from PyPeripheral.Wrappers import Corsair
from PyPeripheral.Wrappers import Razer


if __name__ == "__main__":
    #c = Corsair.SDK()
    #c.connect()
    #c.use()
    #print(c.get_all_device_information())
    #c.set_rgb({"Mouse": (255, 255, 0)})
    #time.sleep(100)
    #c.disable()
    r = Razer.SDK()
    r.connect()
    r.disable()
    #r.get_device_information(1)
    r.set_rgb({"ALL": (255, 255, 0)})
    