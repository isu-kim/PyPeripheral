# distutils: language = c++
# distutils: sources = Corsair.cpp

"""
The upper #distutils part MUST to on top of this code
This script is for declaring that Corsair SDK's methods and its functions.
@project : PyPeripheral
@author : Gooday2die
@date : 2022-02-20
@file : Corsair.pxd
"""

cdef extern from "Corsair.cpp":
    pass

# Decalre the class with cdef
cdef extern from "Corsair.h":
    cdef cppclass Corsair:
        int connect()
        int disconnect()
        int setDeviceRgb(int type, int r, int g, int b)
        int getDeviceCount();
        Device getDeviceInfo(int index)

    ctypedef struct Device:
        const char * name  # I had to change it from std::string to const char * in due to wierd bugs.
        int type
        int index
