## Screen Reactive Lighting
This Markdown document is for screen reactive effects.
You must have those dependencies for this python script to work.

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

## Demo Images
**Demo #1 : Night Vision Goggles** 
![NightVisionDemo](https://github.com/gooday2die/PyPheperial/blob/master/Pics/demo1.gif?raw=true)

**Demo #2 : FlashBang**  
![FlashbangDemo](https://github.com/gooday2die/PyPheperial/blob/master/Pics/demo2.gif?raw=true)


**Demo #3 : Blood** 

![BloodDemo](https://github.com/gooday2die/PyPheperial/blob/master/Pics/demo3.gif?raw=true)

***
I do know that this is not perfect and would be able to reduce latency time with mode smart ideas. For now, this is working, so I would like to share the source with you guys. Thanks.
