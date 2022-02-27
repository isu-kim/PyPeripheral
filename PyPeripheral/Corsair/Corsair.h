/**
 * @file: Corsair.h
 * @author: Gooday2die (Isu Kim), edina00@naver.com
 * @date: 2022-02-18
 * @brief: Codes that implements all member functions and attributes in class Corsair
 */


#ifndef PYPERIPHERAL_CORSAIR_H
#define PYPERIPHERAL_CORSAIR_H
#pragma once

#include <iostream>
#include <string>
#include <list>

#include "CUESDK.h"

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

class Corsair{
private:
    int deviceCount = 0;
    Device* deviceList = nullptr;

    std::list<int> MouseIndexList;
    std::list<int> KeyboardIndexList;
    std::list<int> HeadsetIndexList;
    std::list<int> MouseMatIndexList;
    std::list<int> HeadsetStandIndexList;
    std::list<int> CoolerIndexList;
    std::list<int> MemoryModuleIndexList;
    std::list<int> MotherBoardIndexList;
    std::list<int> GPUIndexList;
    std::list<int> ETCIndexList;

    static int getNthElementFromList(std::list<int>, int);

    int setMouseRgb(int, int, int);
    int setKeyboardRgb(int, int, int);
    int setHeadsetRgb(int, int, int);
    int setMouseMatRgb(int, int, int);
    int setHeadsetStandRgb(int, int, int);
    int setCoolerRgb(int, int, int);
    int setMemoryModuleRgb(int, int, int);
    int setMotherboardRgb(int, int, int);
    int setGPURgb(int, int, int);
    int setETCRgb(int, int, int);
    int setAllRgb(int, int, int);
    int getDeviceType(CorsairDeviceType, int);
    void getAllDeviceInfo();


public:
    ~Corsair () {};
    int connect();
    int disconnect();
    int setDeviceRgb(int, int, int, int);
    int getDeviceCount();
    Device getDeviceInfo(int);
};

#endif //PYPERIPHERAL_CORSAIR_H
