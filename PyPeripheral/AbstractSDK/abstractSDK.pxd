# distutils: language = c++

"""
@project : PyPeripheral
@author : Gooday2die
@file : abstractSDK.pxd
@date : 2022-02-13
"""


# Decalre the class with cdef
"""
This is an abstract class for a sdk wrapper.
"""
cdef extern from "abstractSDK.h":
    cdef cppclass AbstractSDK:
        int connect()
        int disconnect()
        int setDeviceRgb(int type, int r, int g, int b)
        int getDeviceCount();
        Device getDeviceInfo(int index)

    ctypedef struct Device:
        const char * name  # I had to change it from std::string to const char * in due to wierd bugs.
        int type
        int index