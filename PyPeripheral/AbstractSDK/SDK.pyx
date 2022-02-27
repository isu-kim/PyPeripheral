# distutils: language = c++

"""
The upper #distutils part MUST to on top of this code
This script is a reference for wrapping abstraction of a SDK.
@project : PyPeripheral
@author : Gooday2die
@date : 2022-02-23
@file : SDK.pyx
"""

from PyPeripheral.AbstractSDK.abstractSDK cimport AbstractSDK
# There should be an error when you use Pycharm however, it is a little bug with cython.

class SDKInitFailError(Exception):
    """
    An error class for letting our library know that we failed to initialize SDK and cannot connect to SDK.
    Name this SDKInitFailError in a way that the SDK name can be represented. This is for module All to know
    when if a specific SDK failed to init, the module All is able to not use that sdk.
    Ex) CorsairSDKInitFailError
    """
    pass

class SDKNotConnectedError(Exception):
    """
    A Error class for when sdk is not connected and use is trying to perform actions which should be
    executed after sdk has been connected.
    """
    pass

class InvalidDeviceIndexError(Exception):
    """
    An Error class for Invalid Device index
    """
    pass

class InvalidRgbValueError(Exception):
    """
    An Error class for Invalid RGB Values.
    Example: ("AWD", 123, 123)
    Would raise this error
    """
    pass


"""
A reference class sdk for abstractions.
"""
cdef class sdk:
    cdef AbstractSDK* abstract_sdk_ptr  # declare a pointer object of AbstractSDK class.
    cdef object connected_devices  # declare an object which will store all connected devices in dictionary type
    cdef object is_connected  # declare an object which will store if sdk is connected or not

    def __cinit__(self):
        self.abstract_sdk_ptr = new AbstractSDK() # generate a object using new keyword to make object from cpp
        self.connected_devices = dict()  # make a dict that contains all connected devices
        self.is_connected = False  # make an attribute to save if the sdk was connected or not before

    def connect(self):
        """
        A method that connects and requests control over SDK.
        Also set self.is_connected to True if SDK successfully responded.
        :return: returns True if success, False if not.
        """
        # self.is_connected = True
        pass

    def disconnect(self):
        """
        A method that disconnects and requests control over SDK.
        Also set self.is_connected to False if SDK successfully responded.
        :return: returns True if success, False if not.
        """
        # self.is_connected = False
        pass

    def set_rgb(self, rgb_info):
        """
        A method that sets rgb values with dict type that was given as arguments.
        :param rgb_info: the dictionary type of led information.
        Example: {"Mouse": (255, 255, 0)} # this will make Mouse's color go (255, 255, 0)
        :return: each return values can be set freely.
        """
        if not self.is_connected:
            # Raise error if the SDK is not connected.
            # There might be some SDKs which works without being connected, however for safe operations and to minimize
            # unexpected behaviors, raise errors to stop this sdk from making future disasters.
            raise SDKNotConnectedError("SDK is not connected. Use connect() first.")

        for device_type in rgb_info: # Iterate over all elements in rgb_info
            values = rgb_info[device_type]
            try:
                if device_type == "MouseMat":
                    # set MouseMat RGB
                    pass

                elif device_type == "Mouse":
                    # set Mouse RGB
                    pass

                elif device_type == "Keyboard":
                    # set Keyboard RGB
                    pass

                elif device_type == "Headset":
                    # set Headset RGB
                    pass

                elif device_type == "HeadsetStand":
                    # set HeadsetStand RGB
                    pass

                elif device_type == "Cooler":
                    # set Cooler RGB
                    pass

                elif device_type == "MemoryModule":
                    # set MemoryModule RGB
                    pass

                elif device_type == "Motherboard":
                    # set Motherboard RGB
                    pass

                elif device_type == "GPU":
                    # set GPU RGB
                    pass

                elif device_type == "ETC":
                    # set ETC RGB
                    pass

                elif device_type == "ALL":
                    # set ALL RGB
                    pass

            except TypeError:
                # raise TypeError if the given type was not supported or is invalid.
                raise InvalidRgbValueError

    def get_device_information(self, index):
        """
        A method that gets device information from a specific index.
        This must return in a tuple type of following format
        (DeviceName, DeviceType)
        Example: ("GLAIVE RGB", "Mouse")
        :param index: the index to find device information from
        :return: returns tuple type object that contains connected deviec.
        """
        if not self.is_connected:
            raise SDKNotConnectedError("SDK is not Connected. Use connect() first.")
        pass

    def get_device_count(self):
        """
        A method that retrieves count of all connected devices
        :return: returns integer value of connected devices.
        """
        if not self.is_connected:
            raise SDKNotConnectedError("SDK is not Connected. Use connect() first.")
        pass

    def get_all_device_information(self):
        """
        A method for all device's information.
        This method should get all device information and store into a dictionary type.
        Example: {'MouseMat': ('MM800RGB', 0), 'Keyboard': ('K95 RGB PLATINUM', 1), 'Headset': ('VOID PRO USB', 2),
        'Motherboard': ('ASUS Motherboard', 3)}
        :return: returns the device information stored in dictionary type.
        """
        if not self.is_connected:
            raise SDKNotConnectedError("SDK is not Connected. Use connect() first.")

        pass