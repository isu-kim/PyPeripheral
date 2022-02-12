import ctypes

import cuesdk

from PyPeripheral.Wrappers import abstractSDK
from PyPeripheral.Wrappers import Errors


class SDK (abstractSDK.SDK):
    """
    A class for implementing wrapper class for Corsair ICUE
    """
    def __init__(self):
        """
        An initializer method for Corsair ICUE SDK
        """
        self.corsair_object = cuesdk.CueSdk()
        self.all_devices = None

    def connect(self):
        """
        A connect method for Corsair ICUE SDK
        :return: returns None
        """
        self.corsair_object.connect()

    def use(self):
        """
        A use method for Corsair ICUE SDK
        :return: returns None
        """
        self.corsair_object.request_control()

    def disable(self):
        """
        A disable method for Corsair ICUE SDK
        :return: returns None
        """
        self.corsair_object.release_control()

    def get_all_device_information(self):
        """
        A get_all_device_information method for Corsair ICUE SDK
        :return: returns dictionary object of all device information
        """
        self.all_devices = dict()

        device_count = self.corsair_object.get_device_count()

        for i in range(device_count):
            cur_device_info = self.corsair_object.get_device_info(i)
            device_type = self.get_enum_values(cur_device_info.type.value)
            device_name = cur_device_info.model
            self.all_devices[device_type] = (device_name, i)

        return self.all_devices

    def get_device_information(self, index):
        """
        A get_device_information method for Corsair ICUE SDK
        :param index: the index of device to get information
        :return: returns Device Information object.
        """
        cur_device_info = self.corsair_object.get_device_info(index)
        return self.get_enum_values(cur_device_info.type.value), cur_device_info.model

    @staticmethod
    def get_enum_values(enum_value):
        """
        A method for getting names of device type by enum values.
        The enums are located at enums.py from cuesdk
        :param enum_value: the enum value to convert into names
        :return: returns device type in string
        """

        if enum_value == 0:
            return "Unknown"
        elif enum_value == 1:
            return "Mouse"
        elif enum_value == 2:
            return "Keyboard"
        elif enum_value == 3:
            return "Headset"
        elif enum_value == 4:
            return "MouseMat"
        elif enum_value == 5:
            return "HeadsetStand"
        elif enum_value == 6:
            return "CommanderPro"
        elif enum_value == 7:
            return "LightingNodePro"
        elif enum_value == 8:
            return "MemoryModule"
        elif enum_value == 9:
            return "Cooler"
        elif enum_value == 10:
            return "Motherboard"
        elif enum_value == 11:
            return "GraphicsCard"

    def set_rgb(self, rgb_info):
        """
        A set_rgb method for Corsair ICUE SDK
        :param rgb_info: the rgb_information to set
        :return: returns True if successful, False if failure.
        """

        for device_type in rgb_info:
            values = rgb_info[device_type]

            if device_type == "MouseMat":
                self.__set_rgb_mouse_mat(values)

        # Using set_led_colors_flush_buffer_async raises an error which is Argument Error.
        # ctypes.ArgumentError: argument 1: <class 'TypeError'>: expected CFunctionType instance instead of NoneType
        # So in this script, we are using set_led_colors_flush_buffer instead.
        try:
            self.corsair_object.set_led_colors_flush_buffer()
            # self.corsair_object.set_led_colors_flush_buffer_async()
        except ctypes.ArgumentError:
            raise Errors.CorsairRGBSetError("Cannot set RGB values: " + str(self.corsair_object.get_last_error()))

    def __set_rgb_mouse_mat(self, values):
        """
        A method that sets all rgb values of mouse mat.
        :param values: tuple type of rgb values
        :return: returns None
        """
        try:  # try setting values using for loop
            for i in range(155, 170):  # from 155 ~ 169 is mouse_mat values
                self.corsair_object.set_led_colors_buffer_by_device_index(0, {i: values})
                # using original enum values instead of enum itself for loops
        except TypeError:  # when the value had some wrong values. raise InvalidRgbValue Error.
            raise Errors.InvalidRgbValue("RGB Value : " + str(values) + " is invalid RGB Value")
