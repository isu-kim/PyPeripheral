/**
 * @file: Corsair.cpp
 * @author: Gooday2die (Isu Kim), edina00@naver.com
 * @date: 2022-02-18
 * @brief: Codes that implements all member functions and attributes in class Corsair
 */

#include "Corsair.h"

/**
 * A connection method for class Corsair.
 * This performs Protocol handshake and requests control over sdk.
 * @return returns 1 if successful, else 0
 */
int Corsair::connect(){
    CorsairPerformProtocolHandshake();
    bool result = CorsairRequestControl(CAM_ExclusiveLightingControl);
    getAllDeviceInfo();
    return result;
}

/**
 * A disconnection method for class Corsair
 * This releases control over Corsair SDK
 * @return returns 1 if successful, else 0
 */
int Corsair::disconnect(){
    return CorsairReleaseControl(CAM_ExclusiveLightingControl);
}

/**
 * A private member function for translating CorsairDeviceType into DeviceType for our project
 * @param argType the CorsairDeviceType of original device
 * @return translated int for our project
 */
int Corsair::getDeviceType(CorsairDeviceType argType, int index){
    switch (argType) {
        case CDT_Keyboard:
            this->KeyboardIndexList.push_back(index);
            return 1;

        case CDT_Mouse:
            this->MouseIndexList.push_back(index);
            return 0;

        case CDT_Headset:
            this->HeadsetIndexList.push_back(index);
            return 2;

        case CDT_MouseMat:
            this->MouseMatIndexList.push_back(index);
            return 3;

        case CDT_CommanderPro:
            this->CoolerIndexList.push_back(index);
            return 5;

        case CDT_LightingNodePro:
            this->ETCIndexList.push_back(index);
            return 9;

        case CDT_MemoryModule:
            this->MemoryModuleIndexList.push_back(index);
            return 6;

        case CDT_Motherboard:
            this->MotherBoardIndexList.push_back(index);
            return 7;

        case CDT_GraphicsCard:
            this->GPUIndexList.push_back(index);
            return 8;

        case CDT_Cooler:
            this->CoolerIndexList.push_back(index);
            return 5;

        case CDT_Unknown:
            this->ETCIndexList.push_back(index);
            return 9;

        case CDT_HeadsetStand:
            this->HeadsetStandIndexList.push_back(index);
            return 4;
    }
    this->ETCIndexList.push_back(index);
    return 9;
}

/**
 * A method that saves all device information to attributes.
 * This returns nothing, so if there is need to retrieve information from devices, please use getDeviceInfo instead
 */
void Corsair::getAllDeviceInfo() {
    this->deviceCount = CorsairGetDeviceCount();
    this->deviceList = (Device*)malloc(sizeof(Device) * this->deviceCount);

    for(int i = 0 ; i < this->deviceCount ; i++){
        CorsairDeviceInfo* curDevice = CorsairGetDeviceInfo(i);
        this->deviceList[i].type = this->getDeviceType(curDevice->type, i);
        this->deviceList[i].index = i;
        this->deviceList[i].name = curDevice->model;
    }
}

/**
 * A method that gets device info and returns it as a struct that we use in our project
 * @param index the index of the device
 * @return the Device struct that represents a specific device
 */
Device Corsair::getDeviceInfo(int index){
    return this->deviceList[index];
}

/**
 * A member function that gets the total connected device count.
 * @return count of devices.
 */
int Corsair::getDeviceCount() {
    return this->deviceCount;
}

/**
 * A member function that sets device rgb by type.
 * @param type the type of device which is noted in Corsair.h
 * @param r the red value of rgb color to set
 * @param g the green value of rgb color to set
 * @param b the blue value of rgb color to set
 * @return returns int values depends on results
 * 0 : failed to set rgb colors
 * 1 : successfully set rgb color of a specific device
 * -1 : could not find device index
 * -2 : could not set all device type's colors. Example would be, 1/3 mouse is not set rgb.
 */
int Corsair::setDeviceRgb(int type, int r , int g,  int b){
    switch (type) {
        case 0:
            return Corsair::setMouseRgb(r, g, b);
        case 1:
            return Corsair::setKeyboardRgb(r, g, b);
        case 2:
            return Corsair::setHeadsetRgb(r, g, b);
        case 3:
            return Corsair::setMouseMatRgb(r, g, b);
        case 4:
            return Corsair::setHeadsetStandRgb(r, g, b);
        case 5:
            return Corsair::setCoolerRgb(r, g, b);
        case 6:
            return Corsair::setMemoryModuleRgb(r, g, b);
        case 7:
            return Corsair::setMotherboardRgb(r, g, b);
        case 8:
            return Corsair::setGPURgb(r, g, b);
        case 9:
            return Corsair::setETCRgb(r, g, b);
        case 10:
            return Corsair::setAllRgb(r, g, b);
        default:
            return -1;
    }
}

/**
 * A member function that gets nth element from list using advance
 * Code was from https://stackoverflow.com/questions/16747591/how-to-get-an-element-at-specified-index-from-c-list
 * @param list the list to find element from
 * @param index the index to retrieve
 * @return returns value of index
 */
int Corsair::getNthElementFromList(std::list<int> list, int index){
    auto l_front = list.begin();
    std::advance(l_front, index);
    return *l_front;
}

/**
 * A member function that sets Mouse rgb by type.
 * @param r the red value of rgb color to set
 * @param g the green value of rgb color to set
 * @param b the blue value of rgb color to set
 * @return returns int values depends on results
 * 0 : failed to set rgb colors
 * 1 : successfully set rgb color of a specific device
 * -2 : could not set all device type's colors. Example would be, 1/3 mouse is not set rgb.
 */

int Corsair::setMouseRgb(int r, int g, int b) {
    CorsairLedColor values[20];
    for (auto &value: values) {
        value.r = r;
        value.g = g;
        value.b = b;
    }

    int curValueIndex = 0;

    for (int i = 0; i < 4; i++)
        values[curValueIndex++].ledId = static_cast<CorsairLedId>(148 + i);
    for (int i = 0; i < 2; i++)
        values[curValueIndex++].ledId = static_cast<CorsairLedId>(189 + i);
    for (int i = 0; i < 14; i++)
        values[curValueIndex++].ledId = static_cast<CorsairLedId>(1694 + i);

    int resultSum = 0;
    for (int i = 0; i < this->MouseIndexList.size(); i++) // Iterate over all mouse indexes.
        resultSum += CorsairSetLedsColorsBufferByDeviceIndex(getNthElementFromList(this->MouseIndexList, i),
                                                curValueIndex, values);
    CorsairSetLedsColorsFlushBuffer();

    if (resultSum == 0) return resultSum;
    else return resultSum == this->MouseIndexList.size() ? 1 : -2;
}

/**
 * A member function that sets Keyboard rgb by type.
 * @param r the red value of rgb color to set
 * @param g the green value of rgb color to set
 * @param b the blue value of rgb color to set
 * @return returns int values depends on results
 * 0 : failed to set rgb colors
 * 1 : successfully set rgb color of a specific device
 * -2 : could not set all device type's colors. Example would be, 1/3 mouse is not set rgb.
 */

int Corsair::setKeyboardRgb(int r, int g, int b){
    CorsairLedColor values[199];
    for (auto & value : values){
        value.r = r;
        value.g = g;
        value.b = b;
    }

    int curValueIndex = 0;

    for(int i = 1 ; i < 148 ; i++)
        values[curValueIndex++].ledId = static_cast<CorsairLedId>(i);

    values[curValueIndex++].ledId = static_cast<CorsairLedId>(154);

    for(int i = 170 ; i < 18 ; i++)
        values[curValueIndex++].ledId = static_cast<CorsairLedId>(i);

    int resultSum = 0;
    for (int i = 0; i < this->KeyboardIndexList.size(); i++) // Iterate over all keyboard indexes.
        resultSum += CorsairSetLedsColorsBufferByDeviceIndex(getNthElementFromList(this->KeyboardIndexList, i),
                                                             curValueIndex, values);
    CorsairSetLedsColorsFlushBuffer();

    if (resultSum == 0) return resultSum;
    else return resultSum == this->KeyboardIndexList.size() ? 1 : -2;
}

/**
 * A member function that sets Headset rgb by type.
 * @param r the red value of rgb color to set
 * @param g the green value of rgb color to set
 * @param b the blue value of rgb color to set
 * @return returns int values depends on results
 * 0 : failed to set rgb colors
 * 1 : successfully set rgb color of a specific device
 * -2 : could not set all device type's colors. Example would be, 1/3 mouse is not set rgb.
 */
int Corsair::setHeadsetRgb(int r, int g, int b){
    CorsairLedColor values[2];
    for(auto & i : values){
        i.r = r;
        i.g = g;
        i.b = b;
    }

    values[0].ledId = CLH_LeftLogo;
    values[1].ledId = CLH_RightLogo;

    int resultSum = 0;
    for (int i = 0; i < this->HeadsetIndexList.size(); i++) // Iterate over all headset indexes.
        resultSum += CorsairSetLedsColorsBufferByDeviceIndex(getNthElementFromList(this->HeadsetIndexList, i),
                                                             2, values);
    CorsairSetLedsColorsFlushBuffer();

    if (resultSum == 0) return resultSum;
    else return resultSum == this->HeadsetIndexList.size() ? 1 : -2;
}

/**
 * A member function that sets MouseMat rgb by type.
 * @param r the red value of rgb color to set
 * @param g the green value of rgb color to set
 * @param b the blue value of rgb color to set
 * @return returns int values depends on results
 * 0 : failed to set rgb colors
 * 1 : successfully set rgb color of a specific device
 * -2 : could not set all device type's colors. Example would be, 1/3 mouse is not set rgb.
 */
int Corsair::setMouseMatRgb(int r, int g, int b){
    CorsairLedColor values[15];
    for(auto & i : values){
        i.r = r;
        i.g = g;
        i.b = b;
    }

    int curValueIndex = 0;

    for (int i = 0; i < 15; i++)
        values[curValueIndex++].ledId = static_cast<CorsairLedId>(155 + i);

    int resultSum = 0;
    for (int i = 0; i < this->MouseMatIndexList.size(); i++) // Iterate over all mousemat indexes.
        resultSum += CorsairSetLedsColorsBufferByDeviceIndex(getNthElementFromList(this->MouseMatIndexList, i),
                                                             curValueIndex, values);
    CorsairSetLedsColorsFlushBuffer();

    if (resultSum == 0) return resultSum;
    else return resultSum == this->MouseMatIndexList.size() ? 1 : -2;
}

/**
 * A member function that sets HeadsetStand rgb by type.
 * @param r the red value of rgb color to set
 * @param g the green value of rgb color to set
 * @param b the blue value of rgb color to set
 * @return returns int values depends on results
 * 0 : failed to set rgb colors
 * 1 : successfully set rgb color of a specific device
 * -2 : could not set all device type's colors. Example would be, 1/3 mouse is not set rgb.
 */
int Corsair::setHeadsetStandRgb(int r, int g, int b){
    CorsairLedColor values[9];
    for(auto & i : values){
        i.r = r;
        i.g = g;
        i.b = b;
    }

    int curValueIndex = 0;

    for (int i = 0; i < 9; i++)
        values[curValueIndex++].ledId = static_cast<CorsairLedId>(191 + i);

    int resultSum = 0;
    for (int i = 0; i < this->HeadsetStandIndexList.size(); i++) // Iterate over all headset stand indexes.
        resultSum += CorsairSetLedsColorsBufferByDeviceIndex(getNthElementFromList(this->HeadsetStandIndexList, i),
                                                             curValueIndex, values);
    CorsairSetLedsColorsFlushBuffer();

    if (resultSum == 0) return resultSum;
    else return resultSum == this->HeadsetStandIndexList.size() ? 1 : -2;
}

/**
 * A member function that sets Cooler rgb by type.
 * @param r the red value of rgb color to set
 * @param g the green value of rgb color to set
 * @param b the blue value of rgb color to set
 * @return returns int values depends on results
 * 0 : failed to set rgb colors
 * 1 : successfully set rgb color of a specific device
 * -2 : could not set all device type's colors. Example would be, 1/3 mouse is not set rgb.
 */
int Corsair::setCoolerRgb(int r, int g, int b){
    CorsairLedColor values[1050];
    for(auto & i : values){
        i.r = r;
        i.g = g;
        i.b = b;
    }

    int curValueIndex = 0;

    for (int i = 0; i < 300; i++)
        values[curValueIndex++].ledId = static_cast<CorsairLedId>(200 + i);

    for (int i = 0; i < 750; i++)
        values[curValueIndex++].ledId = static_cast<CorsairLedId>(612 + i);

    int resultSum = 0;
    for (int i = 0; i < this->CoolerIndexList.size(); i++) // Iterate over all cooler indexes.
        resultSum += CorsairSetLedsColorsBufferByDeviceIndex(getNthElementFromList(this->CoolerIndexList, i),
                                                             curValueIndex, values);
    CorsairSetLedsColorsFlushBuffer();

    if (resultSum == 0) return resultSum;
    else return resultSum == this->CoolerIndexList.size() ? 1 : -2;
}

/**
 * A member function that sets MemoryModule rgb by type.
 * @param r the red value of rgb color to set
 * @param g the green value of rgb color to set
 * @param b the blue value of rgb color to set
 * @return returns int values depends on results
 * 0 : failed to set rgb colors
 * 1 : successfully set rgb color of a specific device
 * -2 : could not set all device type's colors. Example would be, 1/3 mouse is not set rgb.
 */
int Corsair::setMemoryModuleRgb(int r, int g, int b){
    CorsairLedColor values[12];
    for(auto & i : values){
        i.r = r;
        i.g = g;
        i.b = b;
    }

    int curValueIndex = 0;

    for (int i = 0; i < 12; i++)
        values[curValueIndex++].ledId = static_cast<CorsairLedId>(600 + i);

    int resultSum = 0;
    for (int i = 0; i < this->MemoryModuleIndexList.size(); i++) // Iterate over all memory module indexes.
        resultSum += CorsairSetLedsColorsBufferByDeviceIndex(getNthElementFromList(this->MemoryModuleIndexList, i),
                                                             curValueIndex, values);
    CorsairSetLedsColorsFlushBuffer();

    if (resultSum == 0) return resultSum;
    else return resultSum == this->MemoryModuleIndexList.size() ? 1 : -2;
}

/**
 * A member function that sets Motherboard rgb by type.
 * @param r the red value of rgb color to set
 * @param g the green value of rgb color to set
 * @param b the blue value of rgb color to set
 * @return returns int values depends on results
 * 0 : failed to set rgb colors
 * 1 : successfully set rgb color of a specific device
 * -2 : could not set all device type's colors. Example would be, 1/3 mouse is not set rgb.
 */
int Corsair::setMotherboardRgb(int r, int g, int b){
    CorsairLedColor values[100];
    for(auto & i : values){
        i.r = r;
        i.g = g;
        i.b = b;
    }

    int curValueIndex = 0;

    for (int i = 0; i < 100; i++)
        values[curValueIndex++].ledId = static_cast<CorsairLedId>(1362 + i);

    int resultSum = 0;
    for (int i = 0; i < this->MotherBoardIndexList.size(); i++) // Iterate over all mother board indexes.
        // I guess there should be no two motherboards in one pc for normal users, however just in case.
        resultSum += CorsairSetLedsColorsBufferByDeviceIndex(getNthElementFromList(this->MotherBoardIndexList, i),
                                                             curValueIndex, values);
    CorsairSetLedsColorsFlushBuffer();

    if (resultSum == 0) return resultSum;
    else return resultSum == this->MotherBoardIndexList.size() ? 1 : -2;
}

/**
 * A member function that sets GPU rgb by type.
 * @param r the red value of rgb color to set
 * @param g the green value of rgb color to set
 * @param b the blue value of rgb color to set
 * @return returns int values depends on results
 * 0 : failed to set rgb colors
 * 1 : successfully set rgb color of a specific device
 * -2 : could not set all device type's colors. Example would be, 1/3 mouse is not set rgb.
 */
int Corsair::setGPURgb(int r, int g, int b){
    CorsairLedColor values[50];
    for(auto & i : values){
        i.r = r;
        i.g = g;
        i.b = b;
    }

    int curValueIndex = 0;

    for (int i = 0; i < 50; i++)
        values[curValueIndex++].ledId = static_cast<CorsairLedId>(1462 + i);

    int resultSum = 0;
    for (int i = 0; i < this->GPUIndexList.size(); i++) // Iterate over all GPU indexes.
        // I guess there should SLI or some users using multiple GPUS in one PC.
        resultSum += CorsairSetLedsColorsBufferByDeviceIndex(getNthElementFromList(this->GPUIndexList, i),
                                                             curValueIndex, values);
    CorsairSetLedsColorsFlushBuffer();

    if (resultSum == 0) return resultSum;
    else return resultSum == this->MotherBoardIndexList.size() ? 1 : -2;
}

/**
 * A member function that sets ETC rgb by type.
 * @param r the red value of rgb color to set
 * @param g the green value of rgb color to set
 * @param b the blue value of rgb color to set
 * @return returns int values depends on results
 * 0 : failed to set rgb colors
 * 1 : successfully set rgb color of a specific device
 * -2 : could not set all device type's colors. Example would be, 1/3 mouse is not set rgb.
 */
int Corsair::setETCRgb(int r, int g, int b){
    CorsairLedColor values[250];
    for(auto & i : values){
        i.r = r;
        i.g = g;
        i.b = b;
    }

    int curValueIndex = 0;

    for (int i = 0; i < 100; i++)
        values[curValueIndex++].ledId = static_cast<CorsairLedId>(500 + i);
    for (int i = 0; i < 150; i++)
        values[curValueIndex++].ledId = static_cast<CorsairLedId>(1544 + i);

    int resultSum = 0;
    for (int i = 0; i < this->ETCIndexList.size(); i++) // Iterate over all ETC indexes.
        // I guess there should SLI or some users using multiple GPUS in one PC.
        resultSum += CorsairSetLedsColorsBufferByDeviceIndex(getNthElementFromList(this->ETCIndexList, i),
                                                             curValueIndex, values);
    CorsairSetLedsColorsFlushBuffer();

    if (resultSum == 0) return resultSum;
    else return resultSum == this->ETCIndexList.size() ? 1 : -2;
}

/**
 * A member function that sets ALL rgb.
 * @param r the red value of rgb color to set
 * @param g the green value of rgb color to set
 * @param b the blue value of rgb color to set
 * @return returns int values depends on results
 * 1 : successfully set rgb color of a specific device
 */
int Corsair::setAllRgb(int r, int g, int b){
    this->setMouseRgb(r, g, b);
    this->setKeyboardRgb(r, g, b);
    this->setHeadsetRgb(r, g, b);
    this->setHeadsetStandRgb(r, g, b);
    this->setMemoryModuleRgb(r, g, b);
    this->setGPURgb(r, g, b);
    this->setETCRgb(r, g, b);
    this->setMouseMatRgb(r, g, b);
    this->setMotherboardRgb(r, g, b);

    return 1;
}
