/**
 * @file: Razer.cpp
 * @author: Gooday2die (Isu Kim), edina00@naver.com
 * @date: 2022-02-23
 * @brief: Codes that implements all member functions and attributes in class Razer
 */

#include "./includes/RzChromaSDKDefines.h"
#include "./includes/RzChromaSDKTypes.h"
#include "./includes/RzErrors.h"

#include "Razer.h"


/**
 * A constructor member function that generates all deviceNames list.
 * This will make the list deviceNames filled with Razer devices which is listed in RzChromaSDKDefines.h.
 * This might be added or removed in the future due to Razer's support of each devices.
 */
Razer::Razer(){
    // Keyboards
    deviceNames.push_back(ChromaSDK::BLACKWIDOW_CHROMA);
    deviceNames.push_back(ChromaSDK::BLACKWIDOW_CHROMA_TE);
    deviceNames.push_back(ChromaSDK::DEATHSTALKER_CHROMA);
    deviceNames.push_back(ChromaSDK::OVERWATCH_KEYBOARD);
    deviceNames.push_back(ChromaSDK::BLACKWIDOW_X_CHROMA);
    deviceNames.push_back(ChromaSDK::BLACKWIDOW_X_TE_CHROMA);
    deviceNames.push_back(ChromaSDK::ORNATA_CHROMA);
    deviceNames.push_back(ChromaSDK::BLADE_STEALTH);
    deviceNames.push_back(ChromaSDK::BLADE);
    deviceNames.push_back(ChromaSDK::BLADE_PRO);
    deviceNames.push_back(ChromaSDK::BLACKWIDOW_CHROMA2);

    // Mice
    deviceNames.push_back(ChromaSDK::DEATHADDER_CHROMA);
    deviceNames.push_back(ChromaSDK::MAMBA_CHROMA_TE);
    deviceNames.push_back(ChromaSDK::DIAMONDBACK_CHROMA);
    deviceNames.push_back(ChromaSDK::MAMBA_CHROMA);
    deviceNames.push_back(ChromaSDK::NAGA_EPIC_CHROMA);
    deviceNames.push_back(ChromaSDK::NAGA_CHROMA);
    deviceNames.push_back(ChromaSDK::OROCHI_CHROMA);
    deviceNames.push_back(ChromaSDK::NAGA_HEX_CHROMA);
    deviceNames.push_back(ChromaSDK::DEATHADDER_ELITE_CHROMA);

    // Headsets
    deviceNames.push_back(ChromaSDK::KRAKEN71_CHROMA);
    deviceNames.push_back(ChromaSDK::MANOWAR_CHROMA);
    deviceNames.push_back(ChromaSDK::KRAKEN71_REFRESH_CHROMA);

    // MouseMats
    deviceNames.push_back(ChromaSDK::FIREFLY_CHROMA);

    // Keypads, this will be considered ETC
    deviceNames.push_back(ChromaSDK::TARTARUS_CHROMA);
    deviceNames.push_back(ChromaSDK::ORBWEAVER_CHROMA);


    // ChromaLinks, this will be considered ETC
    deviceNames.push_back(ChromaSDK::LENOVO_Y900);
    deviceNames.push_back(ChromaSDK::LENOVO_Y27);
    deviceNames.push_back(ChromaSDK::CORE_CHROMA);
    deviceNames.push_back(ChromaSDK::CHROMABOX);
}

/**
 * A member function that returns device name in const char* which matches the RZDEVICEID deviceName.
 * The name will be each namespace's variable names with underscore(_) removed.
 * For example, ChromaSDK::BLACKWIDOW_CHROMA will return BLACKWIDOW CHROMA
 * @param deviceName the DeviceID to look for
 * @return returns const char* of device names.
 */
const char* Razer::getDeviceName(RZDEVICEID deviceName){
    // Keyboards
    if (deviceName == ChromaSDK::BLACKWIDOW_CHROMA)
        return "BLACKWIDOW CHROMA";
    else if (deviceName == ChromaSDK::BLACKWIDOW_CHROMA_TE)
        return "BLACKWIDOW CHROMA TE";
    else if (deviceName == ChromaSDK::DEATHSTALKER_CHROMA)
        return "DEATHSTALKER CHROMA";
    else if (deviceName == ChromaSDK::OVERWATCH_KEYBOARD)
        return "OVERWATCH KEYBOARD";
    else if (deviceName == ChromaSDK::BLACKWIDOW_X_CHROMA)
        return "BLACKWIDOW X CHROMA";
    else if (deviceName == ChromaSDK::BLACKWIDOW_X_TE_CHROMA)
        return "BLACKWIDOW X TE CHROMA";
    else if (deviceName == ChromaSDK::ORNATA_CHROMA)
        return "ORNATA CHROMA";
    else if (deviceName == ChromaSDK::BLADE_STEALTH)
        return "BLADE STEALTH";
    else if (deviceName == ChromaSDK::BLADE)
        return "BLADE";
    else if (deviceName == ChromaSDK::BLADE_PRO)
        return "BLADE PRO";
    else if (deviceName == ChromaSDK::BLACKWIDOW_CHROMA2)
        return "BLACKWIDOW CHROMA2";

    // Mice
    else if (deviceName == ChromaSDK::DEATHADDER_CHROMA)
        return "DEATHADDER CHROMA";
    else if (deviceName == ChromaSDK::MAMBA_CHROMA_TE)
        return "MAMBA CHROMA TE";
    else if (deviceName == ChromaSDK::DIAMONDBACK_CHROMA)
        return "DIAMONDBACK CHROMA";
    else if (deviceName == ChromaSDK::MAMBA_CHROMA)
        return "MAMBA CHROMA";
    else if (deviceName == ChromaSDK::NAGA_EPIC_CHROMA)
        return "NAGA EPIC CHROMA";
    else if (deviceName == ChromaSDK::NAGA_CHROMA)
        return "NAGA CHROMA";
    else if (deviceName == ChromaSDK::OROCHI_CHROMA)
        return "OROCHI CHROMA";
    else if (deviceName == ChromaSDK::NAGA_HEX_CHROMA)
        return "NAGA HEX CHROMA";
    else if (deviceName == ChromaSDK::DEATHADDER_ELITE_CHROMA)
        return "DEATHADDER ELITE CHROMA";

    // Headsets
    else if (deviceName == ChromaSDK::KRAKEN71_CHROMA)
        return "KRAKEN71 CHROMA";
    else if (deviceName == ChromaSDK::MANOWAR_CHROMA)
        return "MANOWAR CHROMA";
    else if (deviceName == ChromaSDK::KRAKEN71_REFRESH_CHROMA)
        return "KRAKEN71 REFRESH_CHROMA";

    // Mouse mat
    else if (deviceName == ChromaSDK::FIREFLY_CHROMA)
        return "FIREFLY CHROMA";

    // Keypads
    else if (deviceName == ChromaSDK::TARTARUS_CHROMA)
        return "TARTARUS CHROMA";
    else if (deviceName == ChromaSDK::ORBWEAVER_CHROMA)
        return "ORBWEAVER CHROMA";

    // Chroma Linked devices
    else if (deviceName == ChromaSDK::LENOVO_Y900)
        return "LENOVO Y900";
    else if (deviceName == ChromaSDK::LENOVO_Y27)
        return "LENOVO Y27";
    else if (deviceName == ChromaSDK::CORE_CHROMA)
        return "CORE CHROMA";
    else if (deviceName == ChromaSDK::CHROMABOX)
        return "CHROMABOX";

    // All other devices would be considered UNKNOWN.
    else
        return "UNKNOWN";
}

/**
 * A connect member function for class Razer.
 * This member function will load CHROMASDKDLL which is determined by Razer.h and would be getting Process Address of
 * each functions and then will be saving those addresses as variables.
 * After this member function is done loading all process addresses, this will execute Init function and then return
 * If all functions from DLL is loaded correctly. Then this member function will call getAllDeviceInfo in order to
 * save all device information to the local attribute.
 * @return returns
 *        1 if all functions from GetProcAddress was loaded successfully,
 *        0 if any of those functions from GetProcAddress failed to load,
 *        -1 if already connected
 *        -2 if loading dll was not successful.
 */
int Razer::connect() {
    if (this->m_ChromaSDKModule == nullptr) { // if this is first time initializing Razer
        this->m_ChromaSDKModule = LoadLibrary(CHROMASDKDLL); // Load dll
        if (this->m_ChromaSDKModule != nullptr) { // if loading dll was successful, GetProcAddress
            CreateEffect = reinterpret_cast<CREATEEFFECT>(GetProcAddress(m_ChromaSDKModule, "CreateEffect"));
            CreateKeyboardEffect = reinterpret_cast<CREATEKEYBOARDEFFECT>(GetProcAddress(m_ChromaSDKModule,
                                                                                         "CreateKeyboardEffect"));
            CreateMouseEffect = reinterpret_cast<CREATEMOUSEEFFECT>(GetProcAddress(m_ChromaSDKModule,
                                                                                   "CreateMouseEffect"));
            CreateHeadsetEffect = reinterpret_cast<CREATEHEADSETEFFECT>(GetProcAddress(m_ChromaSDKModule,
                                                                                       "CreateHeadsetEffect"));
            CreateMousepadEffect = reinterpret_cast<CREATEMOUSEPADEFFECT>(GetProcAddress(m_ChromaSDKModule,
                                                                                         "CreateMousepadEffect"));
            CreateKeypadEffect = reinterpret_cast<CREATEKEYPADEFFECT>(GetProcAddress(m_ChromaSDKModule,
                                                                                     "CreateKeypadEffect"));
            CreateChromaLinkEffect = reinterpret_cast<CREATECHROMALINKEFFECT>(GetProcAddress(m_ChromaSDKModule,
                                                                                     "CreateChromaLinkEffect"));
            SetEffect = reinterpret_cast<SETEFFECT>(GetProcAddress(m_ChromaSDKModule, "SetEffect"));
            DeleteEffect = reinterpret_cast<DELETEEFFECT>(GetProcAddress(m_ChromaSDKModule, "DeleteEffect"));
            QueryDevice = reinterpret_cast<QUERYDEVICE>(GetProcAddress(m_ChromaSDKModule, "QueryDevice"));
            Init = (INIT)GetProcAddress(m_ChromaSDKModule, "Init"); // get process address of init
            UnInit = (INIT)GetProcAddress(m_ChromaSDKModule, "UnInit"); // get process address of init

            Init(); // perform init
            getAllDeviceInfo(); // Try getting all device information since this shall be done first right after init.
            return (CreateEffect && CreateKeyboardEffect && CreateMouseEffect && CreateHeadsetEffect &&
                CreateMousepadEffect && CreateKeypadEffect && CreateChromaLinkEffect && SetEffect && DeleteEffect
                && QueryDevice && Init && UnInit);
        }
        else{ // If loading dll was not successful.
            return -2;
        }
    }else{ // If SDK was already connected
        return -1;
    }
}

/**
 * A disconnect member function that performs UnInit for RazerSDK.
 * @return returns RZRESULT value which is in RzErrors.h
 */
int Razer::disconnect() {
    return this->UnInit();
}

/**
 * A member function that sets device rgb by type.
 * Different from Corsair, Razer has only Keyboards, Mice, Headset, MouseMat, Keypads and ChromaLink.
 * Keypads and ChromaLink will be considered as ETC devices with in our system. Thus all of those devices will be treated
 * as one device Type. If you would like controll over each devices, please modify code according to your taste.
 * @param type the type of device which is noted in our documentations.
 * @param r the red value of rgb color to set
 * @param g the green value of rgb color to set
 * @param b the blue value of rgb color to set
 * @return returns RZRESULT values according to its values. returns -1 if that specific device was not found.
 */
int Razer::setDeviceRgb(int type, int r , int g,  int b){
    switch (type) {
        case 0:
            return Razer::setMouseRgb(r, g, b);
        case 1:
            return Razer::setKeyboardRgb(r, g, b);
        case 2:
            return Razer::setHeadsetRgb(r, g, b);
        case 3:
            return Razer::setMouseMatRgb(r, g, b);
        case 9:
            return Razer::setETCRgb(r, g, b);
        case 10:
            return Razer::setAllRgb(r, g, b);
        default: // when we cannot find device type.
            return -1;
    }
}

/**
 * A member function that sets Mouse rgb.
 * @param r the red value of rgb color to set
 * @param g the green value of rgb color to set
 * @param b the blue value of rgb color to set
 * @return returns integer type cased RZRESULT as return value. see RzErrors.h for information about return values.
 */
int Razer::setMouseRgb(int r, int g, int b) {
    ChromaSDK::Mouse::STATIC_EFFECT_TYPE StaticEffect = {};
    RZEFFECTID EffectId;

    StaticEffect.Color = RGB(r, g, b);
    StaticEffect.LEDId = ChromaSDK::Mouse::RZLED_ALL;

    CreateMouseEffect(ChromaSDK::Mouse::CHROMA_STATIC, &StaticEffect, &EffectId);
    return (RZRESULT)SetEffect(EffectId);
}

/**
 * A member function that sets Keyboard rgb.
 * @param r the red value of rgb color to set
 * @param g the green value of rgb color to set
 * @param b the blue value of rgb color to set
 * @return returns integer type cased RZRESULT as return value. see RzErrors.h for information about return values.
 */
int Razer::setKeyboardRgb(int r, int g, int b) {
    ChromaSDK::Keyboard::STATIC_EFFECT_TYPE StaticEffect = {};
    RZEFFECTID EffectId;

    StaticEffect.Color = RGB(r, g, b);

    CreateKeyboardEffect(ChromaSDK::Keyboard::CHROMA_STATIC, &StaticEffect, &EffectId);
    return (RZRESULT)SetEffect(EffectId);
}

/**
 * A member function that sets Headset rgb.
 * @param r the red value of rgb color to set
 * @param g the green value of rgb color to set
 * @param b the blue value of rgb color to set
 * @return returns integer type cased RZRESULT as return value. see RzErrors.h for information about return values.
 */
int Razer::setHeadsetRgb(int r, int g, int b) {
    ChromaSDK::Headset::STATIC_EFFECT_TYPE StaticEffect = {};
    RZEFFECTID EffectId;

    StaticEffect.Color = RGB(r, g, b);

    CreateHeadsetEffect(ChromaSDK::Headset::CHROMA_STATIC, &StaticEffect, &EffectId);
    return (RZRESULT)SetEffect(EffectId);
}

/**
 * A member function that sets Mousemat rgb.
 * @param r the red value of rgb color to set
 * @param g the green value of rgb color to set
 * @param b the blue value of rgb color to set
 * @return returns integer type cased RZRESULT as return value. see RzErrors.h for information about return values.
 */
int Razer::setMouseMatRgb(int r, int g, int b) {
    ChromaSDK::Mousepad::STATIC_EFFECT_TYPE StaticEffect = {};
    RZEFFECTID EffectId;

    StaticEffect.Color = RGB(r, g, b);

    CreateMousepadEffect(ChromaSDK::Mousepad::CHROMA_STATIC, &StaticEffect, &EffectId);
    return (RZRESULT)SetEffect(EffectId);
}

/**
 * A member function that sets ETC device's rgb.
 * For Razer, we will be considering KeyPads and ChromaLink as ETC Devices.
 * @param r the red value of rgb color to set
 * @param g the green value of rgb color to set
 * @param b the blue value of rgb color to set
 * @return returns 1 if every devices were successful, 0 if any of devices were not successful.
 */
int Razer::setETCRgb(int r, int g, int b){
    ChromaSDK::Keypad::STATIC_EFFECT_TYPE KeypadStaticEffect = {};
    ChromaSDK::ChromaLink::STATIC_EFFECT_TYPE ChromaLinkStaticEffect = {};
    RZEFFECTID KeypadStaticEffectId;
    RZEFFECTID ChromaLinkStaticEffectId;

    KeypadStaticEffect.Color = RGB(r, g, b); // For Keypads
    ChromaLinkStaticEffect.Color = RGB(r, g, b); // For ChromaLink

    CreateKeypadEffect(ChromaSDK::Keypad::CHROMA_STATIC, &KeypadStaticEffect, &KeypadStaticEffectId);
    CreateChromaLinkEffect(ChromaSDK::ChromaLink::CHROMA_STATIC, &KeypadStaticEffect, &ChromaLinkStaticEffectId);

    return ((RZRESULT)SetEffect(KeypadStaticEffectId) || (RZRESULT)SetEffect(ChromaLinkStaticEffectId));
}

/**
 * A member function that sets all device rgb
 * @param r the red value of rgb color to set
 * @param g the green value of rgb color to set
 * @param b the blue value of rgb color to set
 * @return returns 0 if every devices were successful, returns error values according to RzErrors.
 */
int Razer::setAllRgb(int r, int g, int b) {
    return (setMouseRgb(r, g, b) ||
            setKeyboardRgb(r, g, b) ||
            setMouseMatRgb(r, g, b) ||
            setHeadsetRgb(r, g, b) ||
            setETCRgb(r, g, b));
}

/**
 * A method that counts total connected devices using isConnected
 * This also generates all deviceNames list which contains all CHROMA available devices' name in const char *
 * @return total count of connected devices.
 */
int Razer::getDeviceCount() {
    this->deviceCount = 0;

    for (int i = 0; i < deviceNames.size(); i++) {
        RZDEVICEID deviceName = getNthElementFromList(deviceNames, i);
        this->deviceCount += isConnectedDevice(deviceName);
    }
    return this->deviceCount;
}

/**
 * A member function that gets nth element from list using advance
 * Code was from https://stackoverflow.com/questions/16747591/how-to-get-an-element-at-specified-index-from-c-list
 * @param list the list to find element from
 * @param index the index to retrieve
 * @return returns value of index
 */
RZDEVICEID Razer::getNthElementFromList(std::list<RZDEVICEID> list, int index){
    auto l_front = list.begin();
    std::advance(l_front, index);
    return *l_front;
}

/**
 * A getAllDeviceInfo member function that stores all device device information.
 * This just sets the this->deviceList array with data, so if you would like to get information from devices,
 * use getDeviceInfo instead with index. This member function will call getDeviceCount to save how many devices are
 * connected currently and will be using QueryDevice function in order to save each data.
 */
void Razer::getAllDeviceInfo() {
    getDeviceCount();
    this->deviceList = (Device*)malloc(sizeof(Device) * this->deviceCount);
    int currentIndex = 0;
    for(int i = 0 ; i < this->deviceNames.size() ; i++){
        ChromaSDK::DEVICE_INFO_TYPE curDeviceInfo = {};
        RZDEVICEID deviceName = getNthElementFromList(deviceNames, i);
        QueryDevice(deviceName, curDeviceInfo);
        if (curDeviceInfo.Connected){
            this->deviceList[currentIndex].type = translateDeviceType(curDeviceInfo.DeviceType);
            this->deviceList[currentIndex].index = currentIndex;
            this->deviceList[currentIndex].name = getDeviceName(deviceName);
            currentIndex++;
        }
    }
}

/**
 * A member function that translates device type from Razer DeviceType to our Device types.
 * @param razerDeviceType the RazerDeviceType value to change from
 * @return translated device type in our Device struct. Default will be 9 if not specified.
 */
int Razer::translateDeviceType(int razerDeviceType){
    switch(razerDeviceType){
        case 1:
            return 1;
        case 2:
            return 0;
        case 3:
            return 2;
        case 4:
            return 3;
        default:
            return 9;
    }
}

/**
 * A member function that returns if a specific device with RZDEVICEID is connected or not
 * @param deviceName the RZDEVICEID to check connection.
 * @return returns 1 if connected, else 0
 */
bool Razer::isConnectedDevice(RZDEVICEID deviceName){
    ChromaSDK::DEVICE_INFO_TYPE curDeviceInfo = {};
    QueryDevice(deviceName, curDeviceInfo);
    return curDeviceInfo.Connected;
}

/**
 * A member function that retrieves a device information in Device type struct
 * @param index the index of device to retrieve information from
 * @return Device type struct that represents device information
 */
Device Razer::getDeviceInfo(int index){
    return this->deviceList[index];
}
