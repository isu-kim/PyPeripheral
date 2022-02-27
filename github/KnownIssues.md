
# Known Issues & Bugs
This page is for tracking known issues and bugs that I had encountered while building the project and installing it in my PC. 
## Installing (setup.py)
### Issues with `data_files`
`data_files` in `setup()` cannot retrieve `site-packages` directory correctly. I have tried various ways for retrieving `site-packages`, however `data_files` does not retrieve directory correctly. Thus, `CUESDK.x64_2019.dll` is not moved into a directory where it should be at. 
- **Solution 1** : added a simple code ```shutil.copy("./PyPeripheral/Corsair/dlls/CUESDK.x64_2019.dll", site_packages_dir + "/PyPeripheral")``` that copies the `dll` into the directory where `site-packages` is located. 
- **Known issues to solution 1**: Since the `dll` is 'copied' by `shutill.copy`, when the package needs to be `uninstalled`, it does NOT recognize that `dll` as this package's components. This means `pip uninstall PyPeripheral` would NOT delete `dll` file that was moved by Solution 1 and would not have 'Clean' uninstallation process.
### Issues with  Microsoft C++ Build Tools
PyPeripheral uses C++ compiler from Microsoft Visual Studio. If you encounter error `error: Microsoft Visual C++ 14.0 or greater is required. Get it with "Microsoft C++ Build Tools": https://visualstudio.microsoft.com/visual-cpp-build-tools/` 
- **Solution 1** : Visit https://visualstudio.microsoft.com/visual-cpp-build-tools/ to download Visual CPP build Tools to compile the `cython` project.

**Any suggestions are always welcomed and if you have better solution, please  PR. I am sick of fixing this same directory bug issues everyday**

### Issues with `pip`
When installing PyPeripheral with `pip install . ` or `pip install PyPeripheral`, sometimes there is an error that occurs during installation. Which is `ERROR: Could not install packages due to an OSError: [Errno 2] No such file or directory:` This is well known issue due to Window's limitation of directory string. This [link](https://stackoverflow.com/questions/65980952/python-could-not-install-packages-due-to-an-oserror-errno-2-no-such-file-or) has some good information about it so please consider visiting the link. 

- **Solution 1:** Install the PyPeripheral using `pip install . --user` or `pip install PyPeripheral --user`. The `--user` option worked in my case

## Corsair Wrapper
### Issues with `import PyPeripheral.Corsair`
When executing `import PyPeripheral.Corsair` in order to use Corsair Wrapper or All Wrapper (Since All Wrapper will execute `import PyPeripheral.Corsair` in order to use Corsair Wrapper features) there is well known bug. `importError: DLL load failed while importing` might occur due to missing `CUESDK.x64_2019.dll`. This is due to **Issues with `data_files`** from **Installing (setup.py)** section. Follow those steps below in order to fix this bug.
1. Locate where PyPeripheral is installed in your environment.
2. Download `CUESDK.x64_2019.dll` from [here](https://github.com/gooday2die/PeripheralPy/raw/cython/PyPeripheral/Corsair/dlls/CUESDK.x64_2019.dll). 
3. Move `CUESDK.x64_2019.dll` into PyPeripheral directory where it contains `Corsair.xxx-win_xxx.pyd` . The `.pxd` file will have different name depending on your environment. 

## Razer Wrapper
### Issue with `get_all_device_information()`
There are missing devices when executing get_all_device_information(). For example, my *Deathadder V2* does **NOT** get recognized as a device and `device_list` does not count this device as Razer device. However, it does set device RGB. Thus there might be some devices missing with Razer Devices
- **Solution**: None. There is no other choice but waiting for Razer's official to add more devices into `RzChromaSDKDefines.h`