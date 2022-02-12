class InvalidRgbValue(Exception):
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
