# SDK Wrappers
**SDK Wrappers** are Python scripts and C++ codes in order to provide interfaces which are easy to use for developers. The goal of each SDK Wrapper is *to provide high-level interface of SDKs to provide easy use of library and polymorphism for ease of development*. 

# Making a Wrapper Module
## How the Wrapper Module is set
`PyPeripheral` is made with `cython`. Since SDK brands do not offer that much support for Python, we have to wrap it using C++ or C in order for us to use it with Python. So each Wrapper Module will contain two parts:
1. C++ or C part that **implements** low-level operation and **interacts** with respective SDK.
2. Cython or Python part that **wraps** those C++ and C part. 

### This sounds too complex
Using `cython` is more complicated than using just Python or C++. However this is due to performances and features of each official SDKs. For example **Razer SDK** offers those SDK options. The table below shows comparison between two SDKs.

|Features |REST API| Using DLLS in C++ |
|--|--|--|
|**Set RGB Colors** | Supported | Supported | 
|**Get Connected Devices**|Not Supported| Supported|
|**Get Error Values**| Highly Limited  |Supported| 
|**Speed**| Has Delays | Fast
|**Get Device Events** | Not Supported | Supported
|**Play Animations**|Not Supported | Supported
|...|...|...|

Thus using `cython` in order to fully use C++ features and better performance are worth it even with its complexity. 
### Sounds good, I want to make one Wrapper
Making a new SDK Wrapper means a lot to this project. I cannot have every RGB devices in planet Earth. Also I am not that rich. I just got devices from Corsair and Razer to test with. Thus, contributing to this project by making a Wrapper will be helping people with same issues in the future and making their development more easier. **Please refer to "Guide for Wrapper Module"** for more information. 


# Guide for Wrapper Module
Before we start, in our Library `PyPeripheral` there is a directory named `AbstractSDK` for abstraction and introduction on how to make a SDK Wrapper module for our project. The introduction below is for detailed explanation of each process.
## Part 0. Requirements
Those are following requirements before you start making a Wrapper Module.
- Basic knowledge about C++ and C
- Basic knowledge about the SDK that you will be using
- Basic knowledge about Python and Cython

If you have not reached those requirements, please do a bit of research on each requirements and then start making a Wrapper Module for our project. If you think you are ready, please go to **Part 1**. 
## Part 1. C++ and C
This part  **implements** low-level operation and **interacts** with SDK. There should be two files made in this part. 

 ### **Header File in C** 

A C Header that **defines** our SDK class that we would be using in the future. That header file should also **include** libraries and other `includes` in order for the SDK to run. The `AbstractSDK.h` includes those following codes as its example:

```
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
```
It is 100% up to you adding up additional attributes or member functions as you wish. However, there should be two rules. 
1. You should **NOT** remove or modify names of those member functions and attributes. Since we will be using polymorphism in `cython`, keeping consistency with names of member functions is the key. 
2. It is highly suggested to set additional member functions and attributes as `private`. 

Also this header file must include `Device` type struct in following format. 
```
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
typedef struct Device{
  const char* name; // The name of this current device  
  int type; // The device type of this device  
  int index; 
}Device;
```

### **Source File in C++ or C**

A Source File is that **implements** those SDK classes that we have defined in our header files. Also each member functions **must** be implemented in a way that is represented below.

 ### `int connect();` 
- This member function must let SDK know that our Library would be using SDK features. This includes actions such as, requesting control over SDK features, getting SDK access, initializing SDKs. **This member function must prepare everything so that the developers are able to use any features with the SDK right after this member function.**
- **Returns**: `1` if successful, `0` if not successful, and other integer error codes that you would like to return to Python for further information. 

 ### `int disconnect();` 
- This member function must let SDK know that our Library would be stop using SDK features. This includes actions such as, releasing control over SDK features, returning SDK access, stoping SDKs. **This member function must return everything back to a state before `connect` was called**
- **Returns**: `1` if successful, `0` if not successful, and other integer error codes that you would like to return to Python for further information. 

 ### `int setDeviceRgb(int type, int r, int g, int b);` 
- This member function must set device RGB color by device type. The device type can be found over in the `Device` comment section of `struct` definition. . Since this member function can get multiple types, `switch` and `case` expression is suggested for implementing this member function.
- **Returns**: `1` if successful, `0` if not successful, and other integer error codes that you would like to return to Python for further information. 

 ### `int getDeviceCount();` 
- This member function must return integer value of total devices connected to the SDK. Since this member function can be called lots of times in the future, it is highly suggested that it just returns `this->deviceCount` values instead of retrieving each device counts every time. 
- **Returns**: `int` value of connected devices. This should NOT return negative values. 


 ### `Device getDeviceInfo(int index);` 
- This member function must return device information in `Device` struct.  There might be some SDKs that does not provide each device's index. It is highly recommended to get all connected device information when `int connect()` is called, then save all those device information to `this->deviceList` then returning each `Device` struct by `index` parameters. 
- **Returns**: `Device` value of device with `index` 


## Part 2. Python and Cython
This is the part that **wraps** those C++ and C part. Since we are going to use `cython`, if you have no experience with `cython`, please check the official documents [here](https://cython.readthedocs.io/en/stable/index.html). There are Wrapper codes included in `abstractSDK.pxd` file and `SDK.pyx`. Those two files are located in `PyPeripheral/AbstractSDK/` directory and has detailed explanations. There are cython functions that must be implemented. 


### `cdef connect(self):`
This is a method for interacting with `int AbstractSDK::connect();` If it is not possible to connect or request control over SDKs, it is recommended to `raise` errors or exceptions. 
 - **Returns**: returned value from original member function
 - **Params**: None

### `cdef disconnect(self):`
This is a method for interacting with `int AbstractSDK::disconnect();` If it is not possible to connect or request control over SDKs, it is recommended to `raise` errors or exceptions. 
 - **Returns**: returned value from original member function
 - **Params**: None

### `def get_device_information(self, index)` : 
This is a method for interacting with `int AbstractSDK::getDeviceInfo(int);` This method is for getting a single device information by index. This method is expected to return a `tuple` type object as its result in following format. A example is shown below. If it is not retrieve information by index, it is recommended to `raise` errors or exceptions. A example is shown below.
```
('Keyboard', 'K95 RGB PLATINUM')
```
`tuple` object must contain **devices type and device name** as its values. 
 - **Returns**: `tuple` type that contains information of requested device. 
 - **Params**: `integer` type that represents the index of device


### `def get_all_device_information(self):` 
 This method is for getting all connected device information from SDK. Since the C++ and C side does not have a member function for this method, please implement this method `def get_device_information(self, index)`. This method is expected to return a `dict` type object as its result in a format.  Examples are shown below.
 
- **Just with one connected device types **
```
{'MouseMat': [('MM800RGB', 0)], 'Keyboard': [('K95 RGB PLATINUM', 1)], 'Headset': [('VOID PRO USB', 2)],  
'Motherboard': [('ASUS Motherboard', 3)], ...}
```
- **Multiple connected device types**
```
{'Mouse': [('DeathAdderEssential', 0), ('DeathAdderElite', 1)]}
```
- **Multiple devices with same types**
```
{'Corsair SDK': {'Mouse': [('GLAIVE RGB', 0)]}, 'Razer SDK': {'Mouse': [('DeathAdderEssential', 0)]}}
```
Each `dict` object should contain `type` as its `key` and `list` type object containing the connected devices name, and index number as its value. If there is no index assigned by original SDKs, it is suggested to assign one by yourself. **There is no assigning rule, however there should be no multiple index numbers assigned to different devices.** The `type` of devices are listed below. **Please be aware that the list types can be updated later**
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
 - **Returns**: `dict` type that contains information of connected devices. 
 - **Params**: None

### `def set_rgb(self, rgb_info)` : 
This is a method for interacting with `int AbstractSDK::setDeviceRgb(int, int, int, int);` This method is expected to take `tuple` of `dict` objects containing following data.
```
({Keyboard, (255,0,0)}, {Mouse, (255,0,0)}, {Headset, (255,0,0)} ...)
```
If requested as up above, this method should be able to set the whole device color as requested `dict` values. Each `dict` object contains `type` and `tuple` type of RGB values. For example, the request up above would set devices as below.
1. **Keyboard** : RGB 255, 0, 0
2. **Mouse** : RGB 255, 0, 0
3. **Headset** : RGB 255, 0, 0
 - **Returns**: None
 - **Params**: `tuple` object that contains `dict` that represents `type` and `tuple` object that contains RGB values.

Since this method would be getting device types in Python `String` object, there should be a script that translates Python `String` object that contains device type into `int` value for  `int AbstractSDK::setDeviceRgb(int, int, int, int);` 

### `def __repr__(self)` : 
This method is to return current object as `object`. It is highly recommended to return in following format. This method will be represented in `All` Class as the SDK's name.
- `SDKNAME SDK`
- Example : `Corsair SDK`, `Razer SDK`

## Hey, I made a new Wrapper SDK Class! What shall I do?
If you are willing to contribute to our project, and would like your Python Wrapper SDK Class as our library's official Wrapper Class, please Pull Request. However, please verify that the submitted Wrapper SDK Class is working on your devices also, please send me a proof that the code works. Unfortunately, I do not have that many devices to test with, so I am not able to check your code is working or not. My apologies for your inconvenience. Please PR in following format.

1. SDK's Name :
2. SDK Brand : 
3. Proof that the Code works (Video or Image URL) : 
4. Tested device's name : 