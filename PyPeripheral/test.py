# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import time

from PyPeripheral.Wrappers import Corsair


if __name__ == "__main__":
    c = Corsair.SDK()
    c.connect()
    c.use()
    print(c.get_all_device_information())
    c.set_rgb({"Mouse": (255, 255, 0)})
    time.sleep(100)
    c.disable()
