I would be posting update logs here in order for people and me to understand what is going on from September 2019. Before September, all the update logs "can" be found by using Github's commitment history system, which is not suggested. I would be posting some personal comments about the project going on. There might be jokes, do not take these too seriously. :)
***
**2019.09.05**  

 - Working on Config files for multiple use. 
 -  Added Basic GUI Module.

**_Personal Comments:_**
  For Config files, I would be just using simple text files. I do not want my program to find all the connected devices every time they run. It is way less effective. Corsair Does support connected device list, however, Razer does not. To make things worse, it even does not return values if the effect setting was physically valid.

I do not have any experience with GUI, So I might not be able to make something fancy. Would try my best for the design. I will keep everything straight forward as much as possible. However, I am just an Computer Science and Engineering student who is never familiar with Arts and Design... (Never got better than grade C. Back in high school, my art teacher got surprised of the result of my work. Of course in bad way.)

Also, personally, a new semester had begun. That would make me study useless subjects that would never help me out with my life. Those subjects would take time from me coding. I hate those.

I am kind of having difficulties in developing this program in Python. There are toooooooo many limits by using Python than the comfort of using Python. I thought there might have been some more good modules that would help me out with this project. However, the reality was cruel. Seriously, who uses Python for hardware control? All the SDKs that are provided by the Manufacturers are written in C++ or C#. So I am planning to learn C++ and implement this whole project to that language. Might need some time for me to learn C++ skills. I would miss my PyCharm...

Lastly, there had been someone who just sent me an email regarding this project. That guy offered me test support using his devices. That was nice of him. I just wanted to reply the email. However, I was not able. I have sent my email from two different email service providers, however, I was not able to send that at all. Outlook just failed. If you are seeing this text, I am sorry for my late reply.
***
**2019.09.07** 

 - Config file work is fully done
 -  Efficient Commands
 - Made some Classes for OOP 
 - Working on GUIs

***Personal Comments***
 Config file is now fully working. When you first run this program, it would generate a file called Config.txt. Inside that file, it should look like this.

    #PyPheperial Config File
    #Please DO NOT change anything from this file unless you know how it works.
    MOUSE=RAZER,CORSAIR
    KEYBOARD=CORSAIR
    MOUSEPAD=CORSAIR
    HEADSET=CORSAIR
    ETC=CORSAIR
    EOF

It stores informations regarding SDKs for the program to use in the future. Before this update, this program was just kind of brute force. Regardless of the SDKs of your device, this program used to command every device connected to the PC. This was kind of unefficient and not only took more time but more resource as well. 

Classes.
That is the main update of this project. Although I am still working on turning this project into OOP based project, some of major things are already shifted to OOP Classes. Actually, to be honest, I did not know how to use Classes. That was the main thing that I had not used a single Class in my project, which was kind of dumb. Now I know how to use Classes a little bit in order to organize all the functions and variables neatly for myself and others as well.

Now working on Tkinter for GUIs. As I have mentioned up above, I am a seriously bad designer. I had never developed GUIs at all. Personally, I am more used to CLI environment. This would make some think that I am just a geek (Joking). So, If there are someone with Tkinter skills, please let me know. I need some of your help with this project. I can develop GUIs in slower pace, however, I have bunch of other things to do with this project; SDK Wrapping, Reactive keys, and other things. 
***
**2019.09.14**

 - Source Code optimization.
 - Working on Mystic Light  (MSI)
 - Working on Reactive Keys

***Personal Comments***
Sorry for no updates for a while. I have been going to school right now to study some things that would be not of a help for my entire life. It has been Korean Thanks Giving holiday for about 2 days till now and 2 days to go. 

I have been working on MSI Mystic Light and I am quite done with it. No, not in the positive way. In a negative way. There are some things that are getting in my way for developing Mystic Light SDK for Python.

1. Shitty Documentation. 
2. Almost impossible for Python Wrapping.
3. 32bit only DLLs.
4. Lack of C++ skills.


Their documentation is almost no help at all. There are some function details, however it is almost not a help at all. I am pretty sure that they even did not know what they were making at the first place. No explanation of the variable types, no example for their codes, not a single help from them.

I had been almost doing everything I can and I came to conclusion that wrapping this into Python module is almost impossible (at least for me). The dll they provided was 32bit based, which is kind of not a definitely a good thing for developers nowadays. 

The python version that this project had been developing was based on 64bit version. Not 32bit version. It is possible for me to get that dll working by using [msl-loadlib](https://github.com/MSLNZ/msl-loadlib) . I full saw the dll working at the moment right now. However, the things are more quite complicated right after this process is done.

As some of you know, the data types between C(++) and Python is different in terms of a lot of things. C is kind of more low-level based data types. However, Python is more of a high-level based data types (actually there is not a term in Python for data types.

For example, in this dll for Mystic Light, there is a Structure called "SAFEARRAY" which is not supported in python. Also, I have tried to make this structure in python for this thing to get working. However, there has to be a difference between the real one and Python one since it is written in different language. For example, structure of SAFEARRAY contains SAFEARRAYBOUND which should be created as a structure(class) for Python. Also, SAFEARRAYBOUND is connected to something called LPSAFEARRAYBOUND. If you solve a question there is another one to solve. which is kind of impossible for me to implement this feature to Python .

The last thing is that I am almost unable to use C++. It would be just great for me to turn this whole project into C++ . However, I lack so much C++ skills. It took about 2 days for me to include SDK header files into my project. However, it is not working at all. 

I will keep trying for myself and everyone who would be using this program in the future.
