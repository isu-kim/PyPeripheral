# distutils: language = c++
# distutils: sources = Corsair.cpp

"""
The upper #distutils part MUST to on top of this code
This script is for declaring that Razer SDK's methods and its functions.
@project : PyPeripheral
@author : Gooday2die
@date : 2022-02-23
@file : Razer.pxd
"""

cdef extern from "Razer.cpp":
    pass

# Decalre the class with cdef
cdef extern from "Razer.h":
    cdef cppclass Razer:
        int connect()
        int disconnect()
        int setDeviceRgb(int type, int r, int g, int b)
        int getDeviceCount();
        Device getDeviceInfo(int index)

    ctypedef struct Device:
        const char * name  # I had to change it from std::string to const char * in due to wierd bugs.
        int type
        int index
