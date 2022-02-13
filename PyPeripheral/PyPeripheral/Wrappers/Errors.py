"""
@project : PyPeripheral
@author : Gooday2die
@date : 2022-02-13
@file : Errors.py
"""


class InvalidRgbValueError(Exception):
    """
    An Error class for Invalid RGB Values.
    Example: ("AWD", 123, 123)
    Would raise this error
    """
    pass


class CorsairRGBSetError(Exception):
    """
    An Error class for Setting RGB values with Corsair ICUE SDK
    """
    pass


class RazerRGBSetError(Exception):
    """
    An Error class for generating RGB effects with Razer SDK
    """
    pass


class CorsairSDKInitFailError(Exception):
    """
    An Error class for SDK not installed.
    """
    pass


class RazerSDKInitFailError(Exception):
    """
    An Error class for SDK not installed.
    """
    pass


class InvalidDeviceIndexError(Exception):
    """
    An Error class for Invalid Device index
    """
    pass


class InvalidDeviceTypeError(Exception):
    """
    An Error class for invalid device type error
    Current device types:

    1. Mouse
    2. Keyboard
    3. Headset
    4. MouseMat
    5. HeadsetStand
    6. Cooler
    7. MemoryModule
    8. Motherboard
    9. GPU
    10. ETC
    11. ALL

    If the requested device was other than these, raise Invalid Device Type Error
    """
    pass
