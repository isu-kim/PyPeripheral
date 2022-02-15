# PyPeripheral  
### A Python Library for Controlling RGB Devices  
### Motivation & Goal  
I got multiple RGB peripheral devices from multiple brands: Razer, Corsair, MSI. So, whenever I try to use a simple `rainbow` effect for each devices, they do not sync. So the main motivation and goal of this project is to **"Provide a Python library for controlling every RGB devices all together"**   
## Installing this Project  
Installing this library for your personal project would be a piece of cake. There will be multiple ways of installing this project, however the easiest way would be using `pip`. 
  
  ### Installation by PIP
  1. `pip install PyPeripheral`
  2. That's it!
  
## Example Codes
> Please note that current version of PyPeripheral supports two SDKs.
> - Corsair
> - Razer

### Setting Corsair Keyboard's Color All Red

```
from PyPeripheral import Corsair
c = Corsair.SDK()
c.connect()
c.set_rgb({"Keyboard": (255, 0, 0)})
```

### Setting Razer Mouse Color All Blue
```
from PyPeripheral import Razer
r = Razer.SDK()
r.connect()
r.set_rgb({"Mouse": (0, 0, 255)})
```

### Setting Every Device All Green
```
from PyPeripheral import All
a = All.SDK()
a.connect()
a.set_rgb({"All": (0, 255, 0)})
```
### Getting All Razer Devices
```
>>> r.get_all_device_information()
{'Mouse': [('DeathAdderElite', 0), ('DeathAdderEssential', 1)]}
>>> r.get_device_information(1)
('Mouse', 'DeathAdderEssential')
```

## Demos
For demonstration videos and gifs, please check [here](https://github.com/gooday2die/PyPeripheral/tree/OOP_Version/Demos) for more information! The demo contains most loved **Screen Reactive Lightning** feature as well!
ix that bug yourself, please do a PR. Any Issues or PR are always welcomed!

## Supported SDKs
- Corsair ICUE SDK (thanks to [cue-sdk](https://github.com/CorsairOfficial/cue-sdk))
- Razer Chroma SDK (thanks to [requests](https://github.com/psf/requests))

