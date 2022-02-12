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
    print(c.get_device_information(1))
    c.set_rgb({"MouseMat": (255, 255, 0)})
    time.sleep(100)
    c.disable()
