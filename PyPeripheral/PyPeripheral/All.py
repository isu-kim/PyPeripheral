"""
@project : PyPeripheral
@author : Gooday2die
@date : 2022-02-13
@file : All.py
"""


from PyPeripheral import abstractSDK
from PyPeripheral import Errors

from PyPeripheral import Corsair
from PyPeripheral import Razer


class SDK(abstractSDK.SDK):
    """
    A class for implementing wrapper class for All SDKs
    """

    def __init__(self):
        """
        An initializer method for All SDKs
        """
        self.sdk_list = list()
        self.all_devices = None

        self.sdk_list.append(Corsair.SDK())  # 0 -> Corsair
        self.sdk_list.append(Razer.SDK())  # 1 -> Razer

    def connect(self):
        for sdk in self.sdk_list:
            try:
                sdk.connect()
            except Errors.CorsairSDKInitFailError:  # When corsair failed to initialize, remove from list
                self.sdk_list.remove(self.sdk_list[0])
            except Errors.RazerSDKInitFailError:  # When Razer failed to initialize, remove from list
                self.sdk_list.remove(self.sdk_list[1])

    def disable(self):
        for sdk in self.sdk_list:
            sdk.disable()

    def get_all_device_information(self):
        """
        A get_all_device_information method for Razer SDK.
        Razer SDK does not provide any way of getting connected devices.
        Thus this method is invalid in this SDK.
        :return: returns dictionary object of all device information
        """
        all_devices = dict()
        for sdk in self.sdk_list:
            all_devices[str(sdk)] = sdk.get_all_device_information()

        return all_devices

    def get_device_information(self, index):
        """
        A get_device_information method for Razer SDK
        Razer SDK does not provide any way of getting connected devices.
        Thus this method is invalid in this SDK.
        :param index: the index of device to get information
        :return: returns Device Information object.
        """
        for sdk in self.sdk_list:
            sdk.get_device_information(index)

    def set_rgb(self, rgb_info):
        """
        A set_rgb method for Razer SDK.

        Since I do not have any Razer devices besides my Deathadders, I could NOT check if other devices work or not.
        Please PR or report issues if you got any problems with your devices.

        :param rgb_info: the rgb_information to set
        :return: returns True if successful, False if failure.
        """
        for sdk in self.sdk_list:
            sdk.set_rgb(rgb_info)

    def __repr__(self):
        """
        A __repr__ method for this class
        """
        return "All SDK"
