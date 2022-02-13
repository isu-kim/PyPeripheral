# Demos
This directory is for demonstration of the library. Currently there are following demonstrations.
- Screen Reactive
- Rainbow All
- Static Color

Currently I am working on making all these steps simple for everyone even who do not know how to program or code by using GUI as well. Please stay tuned!

## Screen Reactive
This is the most loved demo all the time by lots of people! You must have those dependencies for this python script to work.

 - Numpy
 - Scipy
 - MSS
 - Pillow (AKA PIL)
Rough Steps on how it works.
1. Using **MSS** module, we take screenshots per interval and store it to memory.
2. By accessing that memory and retrieving the image, we resize it 150x150 using **PIL** for faster analysis.
3. By using that resized image, we use **Numpy** and **Scipy** for getting the dominant colour on the screen.
4. As we process the most dominant colour as RGB format, we use PyPheperial as the interface control.

Huge thanks for [someone on StackOverFlow](https://stackoverflow.com/questions/3241929/python-find-dominant-most-common-color-in-an-image) for the source and main structure of K-means Clustering algorithm.

Also, note that there is quite a delay between the real screen and the LED response in your pheperials. (Due to the processing latency of MSS and Clustering)

### Demo Images
**Demo #1 : Night Vision Goggles** 

![NightVisionDemo](https://github.com/gooday2die/PyPheperial/blob/master/Pics/demo1.gif?raw=true)


**Demo #2 : FlashBang**  

![FlashbangDemo](https://github.com/gooday2die/PyPheperial/blob/master/Pics/demo2.gif?raw=true)


**Demo #3 : Blood** 

![BloodDemo](https://github.com/gooday2die/PyPheperial/blob/master/Pics/demo3.gif?raw=true)


### Installation
Follow these steps in order to make the script work on your PC (or laptop).
 1. Install numpy : `pip install numpy`
 2. Install scipy : `pip install scipy`
 3. Install mss : `pip install mss`
 4. Install PIL : `pip install pillow`
 5. Install PyPeripheral : `pip install PyPeripheral`
 6. Run ScreenReactive.py : `python3 ScreenReactive.py`
## Rainbow All
Turns makes every connected devices' color into rainbow shifting mode.
### Installation
Follow these steps in order to make the script work on your PC (or laptop).
 1. Install PyPeripheral : `pip install PyPeripheral`
 2. Run ScreenReactive.py : `python3 RainbowAll.py`

## Static Color
Turns makes every connected devices' color into static color.
### Installation
Follow these steps in order to make the script work on your PC (or laptop).
 1. Install PyPeripheral : `pip install PyPeripheral`
 2. Run ScreenReactive.py : `python3 StaticColor.py`