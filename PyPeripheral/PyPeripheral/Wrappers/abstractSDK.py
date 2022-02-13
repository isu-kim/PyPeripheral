"""
@project : PyPeripheral
@author : Gooday2die
@file : abstractSDK.py
@date : 2022-02-13
"""

from abc import abstractmethod, ABCMeta


class SDK:
    """
    An abstract class for a single sdk
    This class is meant to be overridden and be implemented by other sdk codes.
    """
    @abstractmethod
    def __init__(metaclass=ABCMeta):
        """
        An abstract method for initializer method
        """
        pass

    @abstractmethod
    def connect(self):
        """
        An abstract method for connection.
        This method should perform connection to the SDK software.
        :return: returns None
        """
        pass

    @abstractmethod
    def disable(self):
        """
        An abstract method for disabling a specific SDK.
        This method should "release" control over RGB devices of a certain SDK.
        If the disable method is NOT called before exiting the program, SDKs would
        think this python script is still using SDKs features. Thus, call this method before quitting program.
        :return: returns None
        """
        pass

    @abstractmethod
    def get_all_device_information(self):
        """
        An abstract method for all device's information.
        This method should get all device information and store into a dictionary type.
        Example: {'MouseMat': ('MM800RGB', 0), 'Keyboard': ('K95 RGB PLATINUM', 1), 'Headset': ('VOID PRO USB', 2),
        'Motherboard': ('ASUS Motherboard', 3)}
        :return: returns the device information stored in dictionary type.
        """
        pass

    @abstractmethod
    def get_device_information(self, index):
        """
        An abstract method for getting a single device information from specific index.
        This method should retrieve information of a specific device by index
        Example: ('Keyboard', 'K95 RGB PLATINUM')
        :param index: the index of the device
        :return: returns information of the device.
        """
        pass

    @abstractmethod
    def set_rgb(self, rgb_info):
        """
        An abstract method for getting a single rgb.
        This method should set a rgb value by the rgb_info argument.
        :param rgb_info: dictionary type of object that contains key_id, and rgb values. Example: {Keyboard, (255,0,0)}
        :return: returns True if successful, and False if failure.
        """
        pass
