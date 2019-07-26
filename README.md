# PyPheperial
A program written in python for syncing all the Peripherals connected to computer using SDKs.


## Basic Info 

Personally I use those Peripherals for my inputs into computer

 - Mouse 1 : Razer  DeathAdder Elite
 - Mouse 2 : Corsair Glaive RGB Pro
 - Keyboard : Corsair K95 RGB Platinum
 - Mouse Pad : Corsair MM800 RGB
 - Head Phones : Corsair Void RGB Pro
 - And more soon...

As you can see, Mouse 1 and all the other devices are using the different programs for their RGB LED controls. Mouse 1 uses Razer SDK for their RGB LED controls. Meanwhile, all the other devices use Corsair ICUE SDK  for their RGB LED controls. 

Some of you might have seen some programs that does sync all the devices regardless of the manufacturer. However, those programs do have unsupported devices for me, such as Mouse Pad.
So, I am planning to make a program that syncs all the LED of devices together.

Since I possess Razer and Corsair products right now, I am now planning to sync both SDKs.

I think this project would take a lot of time for to make since both SDKs are not made with Python.
Both seems to use DLL or C++ files for their own libraries. However, I do not have that much knowledge in terms of non-Python libraries.  


## References

I will be borrowing and modifying. some open source projects for this program. Since it would be almost impossible for me to make a python wrapper just by myself. Those projects are ones that I am currently borrowing. Those might be removed or added later.

- Corsair ICUE SDK
[http://forum.corsair.com/v3/showthread.php?t=179027](http://forum.corsair.com/v3/showthread.php?t=179027)
for main Corsair ICUE SDK

 - CUE_SDK by 10se1ucgo
 [https://github.com/10se1ucgo/cue_sdk](https://github.com/10se1ucgo/cue_sdk)
 for Corsair ICUE SDK wrapping

Massive thanks to those project contributors.
 
 ## Goals
 The main goal is to sync as many devices as possible just by using this software. I do know that there would be definitely bugs and unsupported devices as well. However, I will try my best for this program.

 - Sync SDKs
 - Support APIs for other developers in the future,
 - Make GUIs for this program.

## Supported Devices
None yet. However, those following devices would be supported for sure.
 - Razer  DeathAdder Elite [Razer SDK]
 - Corsair Glaive RGB Pro [ICUE SDK]
 - Corsair K95 RGB Platinum [ICUE SDK]
 - Corsair MM800 RGB [ICUE SDK]
 - Corsair Void RGB Pro [ICUE SDK]



## ETC
As some of you might know by now, this is my first big project using different libraries and SDKs. 
I do know that there would be bugs and unsupported devices. However, I will be trying very hard to keep those as minimum. If you happen to visit this repository, feel free to suggest some ideas for this project. Also, contributions are always welcomed. If you want to be a contributor, just contact me  edina00@naver.com. 

*If there are some issues regarding copyrights, or other things, I would be happy to remove or replace them with other things in the future. Just let me know. *

I would like to thank all those who have visited this repository. Thanks.

Starting 2019/07/27
