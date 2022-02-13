"""
@project : PyPeripheral
@author : Gooday2die
@date : 2022-02-13
@file : Corsair.py
"""

import ctypes

import cuesdk

from PyPeripheral.Wrappers import abstractSDK
from PyPeripheral.Wrappers import Errors


class SDK(abstractSDK.SDK):
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
        try:
            self.corsair_object.connect()
            self.corsair_object.request_control()
        except:
            raise Errors.CorsairSDKInitFailError

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
            device_type = self.__get_enum_values(cur_device_info.type.value)
            device_name = cur_device_info.model
            self.all_devices[device_type] = (device_name, i)

        return self.all_devices

    def get_device_information(self, index):
        """
        A get_device_information method for Corsair ICUE SDK
        :param index: the index of device to get information
        :return: returns Device Information object.
        """
        try:
            cur_device_info = self.corsair_object.get_device_info(index)
            return self.__get_enum_values(cur_device_info.type.value), cur_device_info.model
        except ValueError:
            raise Errors.InvalidDeviceIndexError("Invalid device index : " + str(index))

    @staticmethod
    def __get_enum_values(enum_value):
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

            elif device_type == "Mouse":
                self.__set_rgb_mouse(values)

            elif device_type == "Keyboard":
                self.__set_rgb_keyboard(values)

            elif device_type == "Headset":
                self.__set_rgb_headset(values)

            elif device_type == "HeadsetStand":
                self.__set_rgb_headset_stand(values)

            elif device_type == "Cooler":
                self.__set_rgb_cooler(values)

            elif device_type == "MemoryModule":
                self.__set_rgb_memory_module(values)

            elif device_type == "Motherboard":
                self.__set_rgb_motherboard(values)

            elif device_type == "GPU":
                self.__set_rgb_gpu(values)

            elif device_type == "ETC":
                self.__set_rgb_etc(values)

            elif device_type == "ALL":
                self.__set_rgb_all(values)

            else:
                raise Errors.InvalidDeviceTypeError("Invalid device type name : " + device_type)

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
        Following enums are for MouseMat LEDs

        MM_Zone1 ~ MM_Zone15 = 155 ~ 169

        Checked with MM800RGB
        :param values: tuple type of rgb values
        :return: returns None
        """
        device_index = self.all_devices["MouseMat"][1]
        try:  # try setting values using for loop
            for i in range(155, 170):
                self.corsair_object.set_led_colors_buffer_by_device_index(device_index, {i: values})
                # using original enum values instead of enum itself for loops
        except TypeError:  # when the value had some wrong values. raise InvalidRgbValue Error.
            raise Errors.InvalidRgbValueError("RGB Value : " + str(values) + " is invalid RGB Value")

    def __set_rgb_mouse(self, values):
        """
        A method that sets all rgb values of a mouse.
        Following enums are for Mouse LEDs

        M_1 ~ M_4 = 148 ~ 151
        M_5 ~ M_6 = 189 ~ 190
        M_7 ~ M_20 = 1694 ~ 1707

        Checked with GLAIVE RGB

        :param values: tuple type of rgb values
        :return: returns None

        """
        device_index = self.all_devices["Mouse"][1]
        try:  # try setting values using for loop
            for i in range(148, 152):
                self.corsair_object.set_led_colors_buffer_by_device_index(device_index, {i: values})

            self.corsair_object.set_led_colors_buffer_by_device_index(device_index, {189: values})
            self.corsair_object.set_led_colors_buffer_by_device_index(device_index, {190: values})

            for i in range(1694, 1708):
                self.corsair_object.set_led_colors_buffer_by_device_index(device_index, {i: values})

        except TypeError:  # when the value had some wrong values. raise InvalidRgbValue Error.
            raise Errors.InvalidRgbValueError("RGB Value : " + str(values) + " is invalid RGB Value")

    def __set_rgb_keyboard(self, values):
        """
        A method that sets all rgb values of keyboard.
        Following enums are for Keyboard LEDs

        Keyboard Values : 1 ~ 147
        K_Logo = 154
        K_Profile = 1543
        KLP_Zone1 ~ KLP_Zone19 = 170 ~ 188
        KLP_Zone20 ~ KLP_Zone50 = 1512 ~ 1542

        Could not check with keyboards yet.
        :param values: tuple type of rgb values
        :return: returns None
        """
        device_index = self.all_devices["Keyboard"][1]
        try:  # try setting values using for loop
            for i in range(1, 148):
                self.corsair_object.set_led_colors_buffer_by_device_index(device_index, {i: values})
                # using original enum values instead of enum itself for loops
            self.corsair_object.set_led_colors_buffer_by_device_index(device_index, {154: values})
            self.corsair_object.set_led_colors_buffer_by_device_index(device_index, {1543: values})
            for i in range(170, 189):
                self.corsair_object.set_led_colors_buffer_by_device_index(device_index, {i: values})
            for i in range(1512, 1543):
                self.corsair_object.set_led_colors_buffer_by_device_index(device_index, {i: values})
        except TypeError:  # when the value had some wrong values. raise InvalidRgbValue Error.
            raise Errors.InvalidRgbValueError("RGB Value : " + str(values) + " is invalid RGB Value")

    def __set_rgb_headset(self, values):
        """
        A method that sets all rgb values of headset.
        Following enums are for Headset LEDs

        H_LeftLogo = 152
        H_RightLogo = 153

        Could not check with Headset yet.
        :param values: tuple type of rgb values
        :return: returns None
        """
        device_index = self.all_devices["Headset"][1]
        try:  # try setting values using for loop
            self.corsair_object.set_led_colors_buffer_by_device_index(device_index, {152: values})
            self.corsair_object.set_led_colors_buffer_by_device_index(device_index, {153: values})
        except TypeError:  # when the value had some wrong values. raise InvalidRgbValue Error.
            raise Errors.InvalidRgbValueError("RGB Value : " + str(values) + " is invalid RGB Value")

    def __set_rgb_headset_stand(self, values):
        """
        A method that sets all rgb values of headset stand.
        Following enums are for Headset Stand LEDs

        HSS_Zone1 ~ HSS_Zone9 = 191 ~ 199

        Could not check with keyboards yet.
        :param values: tuple type of rgb values
        :return: returns None
        """
        device_index = self.all_devices["HeadsetStand"][1]
        try:  # try setting values using for loop
            for i in range(191, 200):
                self.corsair_object.set_led_colors_buffer_by_device_index(device_index, {i: values})
        except TypeError:  # when the value had some wrong values. raise InvalidRgbValue Error.
            raise Errors.InvalidRgbValueError("RGB Value : " + str(values) + " is invalid RGB Value")

    def __set_rgb_memory_module(self, values):
        """
        A method that sets all rgb values of MemoryModule led.
        Following enums are for MemoryModule LEDs

        DRAM_1 ~ DRAM_12 = 600 ~ 611

        Could not check with keyboards yet.
        :param values: tuple type of rgb values
        :return: returns None
        """

        device_index = self.all_devices["MemoryModule"][1]
        try:  # try setting values using for loop
            for i in range(600, 612):
                self.corsair_object.set_led_colors_buffer_by_device_index(device_index, {i: values})
        except TypeError:  # when the value had some wrong values. raise InvalidRgbValue Error.
            raise Errors.InvalidRgbValueError("RGB Value : " + str(values) + " is invalid RGB Value")

    def __set_rgb_cooler(self, values):
        """
        A method that sets all rgb values of Cooler led.
        Following enums are for Cooler LEDs
        I am not 100% sure about all the enums, but I am guessing
        D_C1_1 and those looking like in the same format would be coolers.
        If I get updates on which enums are coolers, I will update the code.

        D_C1_1 ~ D_C2_150 = 200 ~ 499
        D_C3_1 ~ D_C3_300 = 612 ~ 1361

        Could not check with Cooler yet.
        :param values: tuple type of rgb values
        :return: returns None
        """

        device_index = self.all_devices["Cooler"][1]
        try:  # try setting values using for loop
            for i in range(200, 500):
                self.corsair_object.set_led_colors_buffer_by_device_index(device_index, {i: values})
            for i in range(612, 1362):
                self.corsair_object.set_led_colors_buffer_by_device_index(device_index, {i: values})
        except TypeError:  # when the value had some wrong values. raise InvalidRgbValue Error.
            raise Errors.InvalidRgbValueError("RGB Value : " + str(values) + " is invalid RGB Value")

    def __set_rgb_motherboard(self, values):
        """
        A method that sets all rgb values of Motherboard led.
        Following enums are for Motherboard LEDs

        MB_Zone1 ~ MB_Zone100 = 1362 ~ 1461

        Could not check with Motherboard yet.
        :param values: tuple type of rgb values
        :return: returns None
        """

        device_index = self.all_devices["Motherboard"][1]
        try:  # try setting values using for loop
            for i in range(1362, 1462):
                self.corsair_object.set_led_colors_buffer_by_device_index(device_index, {i: values})
        except TypeError:  # when the value had some wrong values. raise InvalidRgbValue Error.
            raise Errors.InvalidRgbValueError("RGB Value : " + str(values) + " is invalid RGB Value")

    def __set_rgb_gpu(self, values):
        """
        A method that sets all rgb values of GPU led.
        Following enums are for GPU LEDs

        GPU_Zone1 ~ GPU_Zone50 = 1462 ~ 1511

        Could not check with GPU yet.
        :param values: tuple type of rgb values
        :return: returns None
        """

        device_index = self.all_devices["GPU"][1]
        try:  # try setting values using for loop
            for i in range(1462, 1512):
                self.corsair_object.set_led_colors_buffer_by_device_index(device_index, {i: values})
        except TypeError:  # when the value had some wrong values. raise InvalidRgbValue Error.
            raise Errors.InvalidRgbValueError("RGB Value : " + str(values) + " is invalid RGB Value")

    def __set_rgb_etc(self, values):
        """
        A method that sets all rgb values of etc led.
        Following enums are for etc LEDs

        Oem1 ~ Oem100 = 500 ~ 599
        Oem101 ~ Oem250 = 1544 ~ 1693

        Could not check with GPU yet.
        :param values: tuple type of rgb values
        :return: returns None
        """

        device_index = self.all_devices["GPU"][1]
        try:  # try setting values using for loop
            for i in range(500, 600):
                self.corsair_object.set_led_colors_buffer_by_device_index(device_index, {i: values})
            for i in range(1544, 1694):
                self.corsair_object.set_led_colors_buffer_by_device_index(device_index, {i: values})
        except TypeError:  # when the value had some wrong values. raise InvalidRgbValue Error.
            raise Errors.InvalidRgbValueError("RGB Value : " + str(values) + " is invalid RGB Value")

    def __set_rgb_all(self, values):
        """
        A method that sets all rgb values of all Corsair led.

        The enums of Corsair LEDs start from 1 to 1707

        :param values: tuple type of rgb values
        :return: returns None
        """

        device_index = 0
        try:  # try setting values using for loop
            for i in range(1, 1707):
                self.corsair_object.set_led_colors_buffer_by_device_index(device_index, {i: values})
            for i in range(1544, 1694):
                self.corsair_object.set_led_colors_buffer_by_device_index(device_index, {i: values})
        except TypeError:  # when the value had some wrong values. raise InvalidRgbValue Error.
            raise Errors.InvalidRgbValueError("RGB Value : " + str(values) + " is invalid RGB Value")
