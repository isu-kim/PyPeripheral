/**
 * @file: abstractSDK.h
 * @author: Gooday2die (Isu Kim), edina00@naver.com
 * @date: 2022-02-18
 * @brief: Codes that implements all member functions and attributes in class abstractSDK. Check documentation for more
 *         information about classes and its implementation.
 */

#ifndef PYPERIPHERAL_ABSTRACTSDK_H
#define PYPERIPHERAL_ABSTRACTSDK_H
#pragma once

/**
 * A struct for device information.
 * There were types that we could have used enums instead of using those int values as the results.
 * However I am trying not to use enums with cython since it is bit complicated.
 * This I will be representing all those values which enums as int values.
 * Device Type are as it follows:
 * Mouse = 0,
 * Keyboard = 1,
 * Headset = 2,
 * MouseMat = 3,
 * HeadsetStand = 4,
 * Cooler = 5,
 * MemoryModule = 6,
 * Motherboard = 7,
 * GPU = 8,
 * ETC = 9,
 * ALL = 10
 *
 * The SDK brand is as it follows:
 * Razer = 0,
 * CorsairSDK = 1
 */
typedef struct Device{
    const char* name; // The name of this current device
    int type; // The device type of this device
    int index;
}Device;

class abstractSDK {
private:
public:
    int deviceCount = 0;
    Device* deviceList = nullptr;

    int connect();
    int disconnect();
    int setDeviceRgb(int, int, int, int);
    int getDeviceCount();
    Device getDeviceInfo(int);
};



#endif //PYPERIPHERAL_ABSTRACTSDK_H
