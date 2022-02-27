/**
 * @file: Razer.h
 * @author: Gooday2die (Isu Kim), edina00@naver.com
 * @date: 2022-02-23
 * @brief: Codes that implements all member functions and attributes in class Razer
 */


#ifndef PYPERIPHERAL_RAZER_H
#define PYPERIPHERAL_RAZER_H

#pragma once

#include <iostream>
#include <tchar.h>
#include <windows.h>
#include <assert.h>
#include <wtypes.h>
#include <list>


#include "./includes/RzChromaSDKDefines.h"
#include "./includes/RzChromaSDKTypes.h"
#include "./includes/RzErrors.h"


#ifdef _WIN64
#define CHROMASDKDLL        _T("RzChromaSDK64.dll")
#else
#define CHROMASDKDLL        _T("RzChromaSDK.dll")
#endif


typedef struct Device{
    const char* name; // The name of this current device
    int type; // The device type of this device
    int index;
}Device;

class Razer{
private:
    int deviceCount = 0;
    Device* deviceList = nullptr;
    std::list<RZDEVICEID> deviceNames;

    typedef RZRESULT(*INIT)(void);
    typedef RZRESULT(*UNINIT)(void);
    typedef RZRESULT(*CREATEEFFECT)(RZDEVICEID DeviceId, ChromaSDK::EFFECT_TYPE Effect, PRZPARAM pParam, RZEFFECTID* pEffectId);
    typedef RZRESULT(*CREATEKEYBOARDEFFECT)(ChromaSDK::Keyboard::EFFECT_TYPE Effect, PRZPARAM pParam, RZEFFECTID* pEffectId);
    typedef RZRESULT(*CREATEHEADSETEFFECT)(ChromaSDK::Headset::EFFECT_TYPE Effect, PRZPARAM pParam, RZEFFECTID* pEffectId);
    typedef RZRESULT(*CREATEMOUSEPADEFFECT)(ChromaSDK::Mousepad::EFFECT_TYPE Effect, PRZPARAM pParam, RZEFFECTID* pEffectId);
    typedef RZRESULT(*CREATEMOUSEEFFECT)(ChromaSDK::Mouse::EFFECT_TYPE Effect, PRZPARAM pParam, RZEFFECTID* pEffectId);
    typedef RZRESULT(*CREATEKEYPADEFFECT)(ChromaSDK::Keypad::EFFECT_TYPE Effect, PRZPARAM pParam, RZEFFECTID* pEffectId);
    typedef RZRESULT(*CREATECHROMALINKEFFECT)(ChromaSDK::ChromaLink::EFFECT_TYPE Effect, PRZPARAM pParam, RZEFFECTID* pEffectId);
    typedef RZRESULT(*SETEFFECT)(RZEFFECTID EffectId);
    typedef RZRESULT(*DELETEEFFECT)(RZEFFECTID EffectId);
    typedef RZRESULT(*REGISTEREVENTNOTIFICATION)(HWND hWnd);
    typedef RZRESULT(*UNREGISTEREVENTNOTIFICATION)(void);
    typedef RZRESULT(*QUERYDEVICE)(RZDEVICEID DeviceId, ChromaSDK::DEVICE_INFO_TYPE& DeviceInfo);

    INIT Init = nullptr;
    UNINIT UnInit = nullptr;
    CREATEEFFECT CreateEffect = nullptr;
    CREATEKEYBOARDEFFECT CreateKeyboardEffect = nullptr;
    CREATEMOUSEEFFECT CreateMouseEffect = nullptr;
    CREATEHEADSETEFFECT CreateHeadsetEffect = nullptr;
    CREATEMOUSEPADEFFECT CreateMousepadEffect = nullptr;
    CREATEKEYPADEFFECT CreateKeypadEffect = nullptr;
    CREATECHROMALINKEFFECT CreateChromaLinkEffect = nullptr;
    SETEFFECT SetEffect = nullptr;
    DELETEEFFECT DeleteEffect = nullptr;
    QUERYDEVICE QueryDevice = nullptr;
    HMODULE m_ChromaSDKModule = NULL;

    int setMouseRgb(int, int, int);
    int setKeyboardRgb(int, int, int);
    int setHeadsetRgb(int, int, int);
    int setMouseMatRgb(int, int, int);
    int setETCRgb(int, int, int);
    int setAllRgb(int, int, int);
    void getAllDeviceInfo();
    bool isConnectedDevice(RZDEVICEID);
    static RZDEVICEID getNthElementFromList(std::list<RZDEVICEID>, int);
    static int translateDeviceType(int);
    static const char* getDeviceName(RZDEVICEID);

public:
    Razer();
    int connect();
    int disconnect();
    int setDeviceRgb(int, int, int, int);
    int getDeviceCount();
    Device getDeviceInfo(int);
};

#endif //PYPERIPHERAL_RAZER_H

