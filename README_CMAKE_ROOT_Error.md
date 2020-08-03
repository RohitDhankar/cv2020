##### CMAKE installed and upgraded to latest version according to instructions on their official site here - 
- https://cmake.org/download/

>  If there is no existing CMake installation, a bootstrap script is provided:

```
./bootstrap
sudo make install

```
#

###### Now calling CMAKE to build OpenCV gives error as below - 
```
CMake Error: Could not find CMAKE_ROOT !!!
CMake has most likely not been installed correctly.
Modules directory not found in
/usr/local/share/cmake-3.10
CMake Error: Error executing cmake::LoadCache(). Aborting.

```

#
- https://askubuntu.com/a/612400/958183

> Recommnded here - https://askubuntu.com/questions/612397/cmake-error-while-building-gromacs-ubuntu-14-10-64-bit .   
Use ``` sudo checkinstall ``` inplace of ```sudo make install ``` as probably done by me earlier - i seem to have followed ( probably incorrectly a YouTube tutorial ) 

#

> Also as recommended in the official site - https://cmake.org/download/ , we need to Remove the earlier installed CMAKE before we run the ``` bootstrap ``` script . I probably did not remove the earlier CMAKE . 
#


