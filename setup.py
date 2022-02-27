"""
@project : CPythonPyPeripheral
@author : Gooday2die
@date : 2022-02-24
@file : setup.py

Short message of setup.py from Gooday2die
I was so much pissed off due to this script working wierd.
Everytime I try to open the project and then add more SDKs or make up more features, the project DOES NOT load.
Then I try to make this code load again and again. The basic process of each day while I am making this library is:

1. Open up Pycharm
2. Do a bit of testing with previous code from last night
3. Does NOT work.
4. Fix setup.py and environments and do things in order to fix the same setup issues with different reason every day.
5. And I am sick of going from 1~4 everyday just to make things fixed into a state that was working before.

Bunch of known issues with setup.py
1. data_files of setup() does NOT get proper directory of where the DLLs should be located.
   Everytime when I try to get the directory of PyPeripheral library, it does not retrieve the correct directory.
   Thus, this should be avoided and ran as a separate commands.
2. ERROR: Could not install packages due to an OSError: [Errno 2] No such file or directory:
   This is due to Windows maximum length of directory. Check
   https://stackoverflow.com/questions/52949531/could-not-install-packages-due-to-an-environmenterror-errno-13
   for more information. Bottom line is that to solve this, install package with pip install . --user.
"""

from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
import shutil
# We included pyproject.toml in order for Cython to be installed before executing setup.py


import site

for i in site.getsitepackages():
    # Get site-packages directory
    if "site-packages" in i:
        site_packages_dir = i

with open("README.md", "r", encoding="utf-8") as fh:  # Read README.md file for long_description
    long_description = fh.read()

ext_modules = [
    # Extension for Corsair
    Extension("PyPeripheral.Corsair",
              ["./PyPeripheral/Corsair/SDK.pyx"],
              include_dirs=["./PyPeripheral/Corsair/includes/"],
              libraries=["CUESDK.x64_2019"],
              library_dirs=['./PyPeripheral/Corsair/libs/'],
              language='c++',
              ),

    #Extension for Razer
    Extension("PyPeripheral.Razer",
              ["./PyPeripheral/Razer/SDK.pyx"],
              include_dirs=["./PyPeripheral/Razer/includes/"],
              ),

    #Extension for All
    Extension("PyPeripheral.All",
              ["./PyPeripheral/All/SDK.pyx"],
              ),
    ]

# General setup process
setup(
    name='PyPeripheral',
    version='2.0.0',
    description='A RGB Controlling Library for Python',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/gooday2die/PyPeripheral',
    author='Gooday2die',
    author_email='edina00@naver.com',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3.8',
        'Environment :: Win32 (MS Windows)',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: Microsoft :: Windows',
        'Topic :: System :: Hardware',
    ],
    install_requires=['cython'],
    ext_modules=cythonize(ext_modules),
    data_files=[("./PyPeripheral", ["./PyPeripheral/Corsair/dlls/CUESDK.x64_2019.dll"])]
    # This data_files section is making everything messed up.
    # The dlls MUST be located in the same directory where the pyd file is generated in order for them to load dlls.
    # However, there is a wierd bug that get_python_lib and site_packages_dir cannot catch the proper
    # site-packages directory in order to locate dll file with pyd file.
    # This must be refactored and the dlls should be moved using a different python function after setup()
)
shutil.copy("./PyPeripheral/Corsair/dlls/CUESDK.x64_2019.dll", site_packages_dir + "/PyPeripheral")