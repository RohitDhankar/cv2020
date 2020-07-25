##### Need to update flag for CUDA 11.0 DIR == -DCUDA_TOOLKIT_ROOT_DIR=/usr/local/cuda-11.0 \
```
-- Consider using CMake 3.12+ for better Python support
-- Looking for ccache - not found

-- Could NOT find CUDNN (missing: CUDNN_LIBRARY CUDNN_INCLUDE_DIR) (Required is at least version "7.5")

-- Performing Test HAVE_C_WERROR_NON_VIRTUAL_DTOR - Failed
-- Performing Test HAVE_CXX_WMISSING_PROTOTYPES - Failed
-- Performing Test HAVE_CXX_WSTRICT_PROTOTYPES - Failed
-- Performing Test HAVE_C_WSIGN_PROMO - Failed
-- Performing Test HAVE_C_WSUGGEST_OVERRIDE - Failed
-- Performing Test HAVE_C_WNO_DELETE_NON_VIRTUAL_DTOR - Failed
-- Performing Test HAVE_CXX_WNO_UNNAMED_TYPE_TEMPLATE_ARGS - Failed
-- Performing Test HAVE_C_WNO_UNNAMED_TYPE_TEMPLATE_ARGS - Failed
-- Performing Test HAVE_C_FVISIBILITY_INLINES_HIDDEN - Failed
```
#
###### Solving for - ccache . 
# 
- https://askubuntu.com/questions/470545/how-do-i-set-up-ccache

```
(opencv_cuda) dhankar@dhankar-1:~/opencv_cuda/opencv/build$ dpkg -l ccache
dpkg-query: no packages found matching ccache
(opencv_cuda) dhankar@dhankar-1:~/opencv_cuda/opencv/build$ 
(opencv_cuda) dhankar@dhankar-1:~/opencv_cuda/opencv/build$ sudo apt install -y ccache
[sudo] password for dhankar: 
Reading package lists... Done
Building dependency tree       
Reading state information... Done
Suggested packages:
  distcc
The following NEW packages will be installed:
  ccache
0 upgraded, 1 newly installed, 0 to remove and 22 not upgraded.
Need to get 110 kB of archives.
After this operation, 326 kB of additional disk space will be used.
Get:1 http://in.archive.ubuntu.com/ubuntu bionic/main amd64 ccache amd64 3.4.1-1 [110 kB]
Fetched 110 kB in 1s (126 kB/s)         
Selecting previously unselected package ccache.
(Reading database ... 314025 files and directories currently installed.)
Preparing to unpack .../ccache_3.4.1-1_amd64.deb ...
Unpacking ccache (3.4.1-1) ...
Setting up ccache (3.4.1-1) ...
Updating symlinks in /usr/lib/ccache ...
Processing triggers for man-db (2.8.3-2ubuntu0.1) ...


(opencv_cuda) dhankar@dhankar-1:~/opencv_cuda/opencv/build$ dpkg -l ccache
Desired=Unknown/Install/Remove/Purge/Hold
| Status=Not/Inst/Conf-files/Unpacked/halF-conf/Half-inst/trig-aWait/Trig-pend
|/ Err?=(none)/Reinst-required (Status,Err: uppercase=bad)
||/ Name                          Version             Architecture        Description
+++-=============================-===================-===================-================================================================
ii  ccache                        3.4.1-1             amd64               Compiler cache for fast recompilation of C/C++ code


(opencv_cuda) dhankar@dhankar-1:~/opencv_cuda/opencv/build$ which g++ gcc
/usr/bin/g++
/usr/bin/gcc

(opencv_cuda) dhankar@dhankar-1:~/opencv_cuda/opencv/build$ ccache -s
cache directory                     /home/dhankar/.ccache
primary config                      /home/dhankar/.ccache/ccache.conf
secondary config      (readonly)    /etc/ccache.conf
cache hit (direct)                     0
cache hit (preprocessed)               0
cache miss                             0
cache hit rate                      0.00 %
cleanups performed                     0
files in cache                         0
cache size                           0.0 kB
max cache size                       5.0 GB

(opencv_cuda) dhankar@dhankar-1:~/opencv_cuda/opencv/build$ sudo /usr/sbin/update-ccache-symlinks
(opencv_cuda) dhankar@dhankar-1:~/opencv_cuda/opencv/build$ echo 'export PATH="/usr/lib/ccache:$PATH"' | tee -a ~/.bashrc
export PATH="/usr/lib/ccache:$PATH"

(opencv_cuda) dhankar@dhankar-1:~/opencv_cuda/opencv/build$ source ~/.bashrc && echo $PATH
/usr/lib/ccache:/home/dhankar/anaconda3/bin:/home/dhankar/.virtualenvs/opencv_cuda/bin:/home/dhankar/anaconda3/condabin:/home/dhankar/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin

(base) dhankar@dhankar-1:~/opencv_cuda/opencv/build$ which g++ gcc
/usr/lib/ccache/g++
/usr/lib/ccache/gcc
(base) dhankar@dhankar-1:~/opencv_cuda/opencv/build$ 

```
#
###### Seems i have the same issue as this --- https://github.com/skvark/opencv-python/issues/330
- https://github.com/skvark/opencv-python/issues/330
- https://www.ics.com/blog/some-lesser-known-qt-tools-and-commands-part-5

> for now am trying by adding another Compile flag as suggested in the above issue - "-D WITH_QT=4"

#
```
(opencv_cuda) dhankar@dhankar-1:/usr/lib/qt5$ ls -ltr
total 4
drwxr-xr-x 2 root root 4096 Feb 11 08:30 bin
(opencv_cuda) dhankar@dhankar-1:/usr/lib/qt5$ cd bin
(opencv_cuda) dhankar@dhankar-1:/usr/lib/qt5/bin$ ls -ltr
total 12992
-rwxr-xr-x 1 root root   49240 Apr  4  2018 syncqt.pl
-rwxr-xr-x 1 root root    6344 Apr  4  2018 fixqt4headers.pl
-rwxr-xr-x 1 root root   22512 Apr 14  2018 qtplugininfo
-rwxr-xr-x 1 root root   22592 Apr 14  2018 qtpaths
-rwxr-xr-x 1 root root   59456 Apr 14  2018 qtdiag
-rwxr-xr-x 1 root root   67568 Apr 14  2018 qtattributionsscanner
-rwxr-xr-x 1 root root   22592 Apr 14  2018 qhelpgenerator
-rwxr-xr-x 1 root root  194624 Apr 14  2018 qhelpconverter
-rwxr-xr-x 1 root root 1462992 Apr 14  2018 qdoc
-rwxr-xr-x 1 root root  129088 Apr 14  2018 qdbusviewer
-rwxr-xr-x 1 root root   71744 Apr 14  2018 qcollectiongenerator
-rwxr-xr-x 1 root root   59456 Apr 14  2018 pixeltool
-rwxr-xr-x 1 root root  940176 Apr 14  2018 lupdate
-rwxr-xr-x 1 root root  522304 Apr 14  2018 lrelease
-rwxr-xr-x 1 root root 1460288 Apr 14  2018 linguist
-rwxr-xr-x 1 root root  301120 Apr 14  2018 lconvert
-rwxr-xr-x 1 root root  485448 Apr 14  2018 designer
-rwxr-xr-x 1 root root 1329736 Apr 14  2018 assistant
-rwxr-xr-x 1 root root  649280 Feb  7 21:11 uic
-rwxr-xr-x 1 root root  993472 Feb  7 21:11 rcc
-rwxr-xr-x 1 root root 2718192 Feb  7 21:11 qmake
-rwxr-xr-x 1 root root  202736 Feb  7 21:11 qlalr
-rwxr-xr-x 1 root root   79856 Feb  7 21:11 qdbusxml2cpp
-rwxr-xr-x 1 root root  284736 Feb  7 21:11 qdbuscpp2xml
-rwxr-xr-x 1 root root 1116352 Feb  7 21:11 moc
(opencv_cuda) dhankar@dhankar-1:/usr/lib/qt5/bin$ 

```

#
```
 WebP: /usr/lib/x86_64-linux-gnu/libwebp.so  
-- The imported target "openjp2_static" references the file
   "/usr/lib/x86_64-linux-gnu/libopenjp2.a"
but this file does not exist.  Possible reasons include:
* The file was deleted, renamed, or moved to another location.
* An install or uninstall procedure did not complete successfully.
* The installation package was faulty and contained
   "/usr/lib/x86_64-linux-gnu/openjpeg-2.3/OpenJPEGTargets.cmake"
but not all the files it references.

-- The imported target "openjpip" references the file
   "/usr/lib/x86_64-linux-gnu/libopenjpip.so.2.3.0"
but this file does not exist.  Possible reasons include:
* The file was deleted, renamed, or moved to another location.
* An install or uninstall procedure did not complete successfully.
* The installation package was faulty and contained
   "/usr/lib/x86_64-linux-gnu/openjpeg-2.3/OpenJPEGTargets.cmake"
but not all the files it references.

-- The imported target "openjpip_server" references the file
   "/usr/lib/x86_64-linux-gnu/libopenjpip_server.a"
but this file does not exist.  Possible reasons include:
* The file was deleted, renamed, or moved to another location.
* An install or uninstall procedure did not complete successfully.
* The installation package was faulty and contained
   "/usr/lib/x86_64-linux-gnu/openjpeg-2.3/OpenJPEGTargets.cmake"
but not all the files it references.

-- The imported target "opj_decompress" references the file
   "/usr/bin/opj_decompress"
but this file does not exist.  Possible reasons include:
* The file was deleted, renamed, or moved to another location.
* An install or uninstall procedure did not complete successfully.
* The installation package was faulty and contained
   "/usr/lib/x86_64-linux-gnu/openjpeg-2.3/OpenJPEGTargets.cmake"
but not all the files it references.

-- The imported target "opj_compress" references the file
   "/usr/bin/opj_compress"
but this file does not exist.  Possible reasons include:
* The file was deleted, renamed, or moved to another location.
* An install or uninstall procedure did not complete successfully.
* The installation package was faulty and contained
   "/usr/lib/x86_64-linux-gnu/openjpeg-2.3/OpenJPEGTargets.cmake"
but not all the files it references.

-- The imported target "opj_dump" references the file
   "/usr/bin/opj_dump"
but this file does not exist.  Possible reasons include:
* The file was deleted, renamed, or moved to another location.
* An install or uninstall procedure did not complete successfully.
* The installation package was faulty and contained
   "/usr/lib/x86_64-linux-gnu/openjpeg-2.3/OpenJPEGTargets.cmake"
but not all the files it references.

-- The imported target "opj_jpip_addxml" references the file
   "/usr/bin/opj_jpip_addxml"
but this file does not exist.  Possible reasons include:
* The file was deleted, renamed, or moved to another location.
* An install or uninstall procedure did not complete successfully.
* The installation package was faulty and contained
   "/usr/lib/x86_64-linux-gnu/openjpeg-2.3/OpenJPEGTargets.cmake"
but not all the files it references.

-- The imported target "opj_server" references the file
   "/usr/bin/opj_server"
but this file does not exist.  Possible reasons include:
* The file was deleted, renamed, or moved to another location.
* An install or uninstall procedure did not complete successfully.
* The installation package was faulty and contained
   "/usr/lib/x86_64-linux-gnu/openjpeg-2.3/OpenJPEGTargets.cmake"
but not all the files it references.

-- The imported target "opj_dec_server" references the file
   "/usr/bin/opj_dec_server"
but this file does not exist.  Possible reasons include:
* The file was deleted, renamed, or moved to another location.
* An install or uninstall procedure did not complete successfully.
* The installation package was faulty and contained
   "/usr/lib/x86_64-linux-gnu/openjpeg-2.3/OpenJPEGTargets.cmake"
but not all the files it references.

-- The imported target "opj_jpip_transcode" references the file
   "/usr/bin/opj_jpip_transcode"
but this file does not exist.  Possible reasons include:
* The file was deleted, renamed, or moved to another location.
* An install or uninstall procedure did not complete successfully.
* The installation package was faulty and contained
   "/usr/lib/x86_64-linux-gnu/openjpeg-2.3/OpenJPEGTargets.cmake"
but not all the files it references.

-- The imported target "opj_jpip_test" references the file
   "/usr/bin/opj_jpip_test"
but this file does not exist.  Possible reasons include:
* The file was deleted, renamed, or moved to another location.
* An install or uninstall procedure did not complete successfully.
* The installation package was faulty and contained
   "/usr/lib/x86_64-linux-gnu/openjpeg-2.3/OpenJPEGTargets.cmake"
but not all the files it references.
```

#

#

```
(opencv_cuda) dhankar@dhankar-1:~$ cd /usr/local/
(opencv_cuda) dhankar@dhankar-1:/usr/local$ 
(opencv_cuda) dhankar@dhankar-1:/usr/local$ ls -ltr
total 40
drwxr-xr-x  2 root root 4096 Aug  6  2019 src
drwxr-xr-x  2 root root 4096 Aug  6  2019 sbin
drwxr-xr-x  2 root root 4096 Aug  6  2019 include
drwxr-xr-x  2 root root 4096 Aug  6  2019 games
lrwxrwxrwx  1 root root    9 Dec 23  2019 man -> share/man
drwxr-xr-x  4 root root 4096 Apr 17 11:52 etc
drwxr-xr-x  5 root root 4096 May 13 10:29 lib
drwxr-xr-x  3 root root 4096 Jul  4 09:11 aws-cli
drwxr-xr-x 10 root root 4096 Jul 21 18:42 share
drwxr-xr-x 15 root root 4096 Jul 25 16:58 cuda-11.0
drwxr-xr-x  2 root root 4096 Jul 25 16:58 bin
lrwxrwxrwx  1 root root    9 Jul 25 16:59 cuda -> cuda-11.0
(opencv_cuda) dhankar@dhankar-1:/usr/local$ cd cuda-11.0
(opencv_cuda) dhankar@dhankar-1:/usr/local/cuda-11.0$ ls -ltr
total 116
lrwxrwxrwx  1 root root    24 Jun 12 23:37 lib64 -> targets/x86_64-linux/lib
lrwxrwxrwx  1 root root    28 Jun 12 23:37 include -> targets/x86_64-linux/include
-rw-r--r--  1 root root 59649 Jul  1 03:24 EULA.txt
-rw-r--r--  1 root root    22 Jul  1 03:24 version.txt
drwxr-xr-x  3 root root  4096 Jul 25 16:55 targets
drwxr-xr-x  7 root root  4096 Jul 25 16:57 nvvm
drwxr-xr-x  2 root root  4096 Jul 25 16:57 src
drwxr-xr-x  3 root root  4096 Jul 25 16:57 share
drwxr-xr-x  4 root root  4096 Jul 25 16:57 Sanitizer
drwxr-xr-x  2 root root  4096 Jul 25 16:58 nsightee_plugins
drwxr-xr-x  3 root root  4096 Jul 25 16:58 nvml
drwxr-xr-x  7 root root  4096 Jul 25 16:58 libnvvp
drwxr-xr-x 11 root root  4096 Jul 25 16:58 samples
drwxr-xr-x  3 root root  4096 Jul 25 16:58 bin
drwxr-xr-x  5 root root  4096 Jul 25 16:58 doc
drwxr-xr-x  2 root root  4096 Jul 25 16:58 tools
drwxr-xr-x  5 root root  4096 Jul 25 16:58 extras
(opencv_cuda) dhankar@dhankar-1:/usr/local/cuda-11.0$ 
```

#

```
(opencv_cuda) dhankar@dhankar-1:~$     
(opencv_cuda) dhankar@dhankar-1:~$ nvidia-smi -a

==============NVSMI LOG==============

Timestamp                                 : Sat Jul 25 17:42:45 2020
Driver Version                            : 450.51.05
CUDA Version                              : 11.0

Attached GPUs                             : 1
GPU 00000000:01:00.0
    Product Name                          : GeForce GTX 1650
    Product Brand                         : GeForce
    Display Mode                          : Enabled
    Display Active                        : Enabled
    Persistence Mode                      : Enabled
    MIG Mode
        Current                           : N/A
        Pending                           : N/A
    Accounting Mode                       : Disabled
    Accounting Mode Buffer Size           : 4000
    Driver Model
        Current                           : N/A
        Pending                           : N/A
    Serial Number                         : N/A
    GPU UUID                              : GPU-
    Minor Number                          : 0
    VBIOS Version                         : 90.........
    MultiGPU Board                        : No
    Board ID                              : 0x100
    GPU Part Number                       : N/A
    Inforom Version
        Image Version                     : G......
        OEM Object                        : 1.1
        ECC Object                        : N/A
        Power Management Object           : N/A
    GPU Operation Mode
        Current                           : N/A
        Pending                           : N/A
    GPU Virtualization Mode
        Virtualization Mode               : None
        Host VGPU Mode                    : N/A
    IBMNPU
        Relaxed Ordering Mode             : N/A
    PCI
        Bus                               : 0x01
        Device                            : 0x00
        Domain                            : 0x0000
        Device Id                         : 0
        Bus Id                            : 00
        Sub System Id                     : 0
        GPU Link Info
            PCIe Generation
                Max                       : 3
                Current                   : 1
            Link Width
                Max                       : 16x
                Current                   : 16x
        Bridge Chip
            Type                          : N/A
            Firmware                      : N/A
        Replays Since Reset               : 0
        Replay Number Rollovers           : 0
        Tx Throughput                     : 1000 KB/s
        Rx Throughput                     : 10000 KB/s
    Fan Speed                             : 0 %
    Performance State                     : P8
    Clocks Throttle Reasons
        Idle                              : Active
        Applications Clocks Setting       : Not Active
        SW Power Cap                      : Not Active
        HW Slowdown                       : Not Active
            HW Thermal Slowdown           : Not Active
            HW Power Brake Slowdown       : Not Active
        Sync Boost                        : Not Active
        SW Thermal Slowdown               : Not Active
        Display Clock Setting             : Not Active
    FB Memory Usage
        Total                             : 3910 MiB
        Used                              : 236 MiB
        Free                              : 3674 MiB
    BAR1 Memory Usage
        Total                             : 256 MiB
        Used                              : 7 MiB
        Free                              : 249 MiB
    Compute Mode                          : Default
    Utilization
        Gpu                               : 14 %
        Memory                            : 6 %
        Encoder                           : 0 %
        Decoder                           : 0 %
    Encoder Stats
        Active Sessions                   : 0
        Average FPS                       : 0
        Average Latency                   : 0
    FBC Stats
        Active Sessions                   : 0
        Average FPS                       : 0
        Average Latency                   : 0
    Ecc Mode
        Current                           : N/A
        Pending                           : N/A
    ECC Errors
        Volatile
            SRAM Correctable              : N/A
            SRAM Uncorrectable            : N/A
            DRAM Correctable              : N/A
            DRAM Uncorrectable            : N/A
        Aggregate
            SRAM Correctable              : N/A
            SRAM Uncorrectable            : N/A
            DRAM Correctable              : N/A
            DRAM Uncorrectable            : N/A
    Retired Pages
        Single Bit ECC                    : N/A
        Double Bit ECC                    : N/A
        Pending Page Blacklist            : N/A
    Remapped Rows                         : N/A
    Temperature
        GPU Current Temp                  : 48 C
        GPU Shutdown Temp                 : 97 C
        GPU Slowdown Temp                 : 94 C
        GPU Max Operating Temp            : 92 C
        Memory Current Temp               : N/A
        Memory Max Operating Temp         : N/A
    Power Readings
        Power Management                  : Supported
        Power Draw                        : 7.37 W
        Power Limit                       : 75.00 W
        Default Power Limit               : 75.00 W
        Enforced Power Limit              : 75.00 W
        Min Power Limit                   : 45.00 W
        Max Power Limit                   : 75.00 W
    Clocks
        Graphics                          : 300 MHz
        SM                                : 300 MHz
        Memory                            : 405 MHz
        Video                             : 540 MHz
    Applications Clocks
        Graphics                          : N/A
        Memory                            : N/A
    Default Applications Clocks
        Graphics                          : N/A
        Memory                            : N/A
    Max Clocks
        Graphics                          : 2145 MHz
        SM                                : 2145 MHz
        Memory                            : 4001 MHz
        Video                             : 1950 MHz
    Max Customer Boost Clocks
        Graphics                          : N/A
    Clock Policy
        Auto Boost                        : N/A
        Auto Boost Default                : N/A
    Processes
        GPU instance ID             : N/A
        Compute instance ID         : N/A
        Process ID                  : 1741
            Type                    : G
            Name                    : /usr/lib/xorg/Xorg
            Used GPU Memory         : 14 MiB
        GPU instance ID             : N/A
        Compute instance ID         : N/A
        Process ID                  : 2142
            Type                    : G
            Name                    : /usr/bin/gnome-shell
            Used GPU Memory         : 49 MiB
        GPU instance ID             : N/A
        Compute instance ID         : N/A
        Process ID                  : 3868
            Type                    : G
            Name                    : /usr/lib/xorg/Xorg
            Used GPU Memory         : 100 MiB
        GPU instance ID             : N/A
        Compute instance ID         : N/A
        Process ID                  : 4001
            Type                    : G
            Name                    : /usr/bin/gnome-shell
            Used GPU Memory         : 69 MiB

(opencv_cuda) dhankar@dhankar-1:~$ 
```
#

dhankar@dhankar-1:~/opencv_cuda/opencv/build$ workon opencv_cuda
(opencv_cuda) dhankar@dhankar-1:~/opencv_cuda/opencv/build$ 
(opencv_cuda) dhankar@dhankar-1:~/opencv_cuda/opencv/build$ cmake -D CMAKE_BUILD_TYPE=RELEASE \
> -D CMAKE_INSTALL_PREFIX=/usr/local \
> -D INSTALL_PYTHON_EXAMPLES=ON \
> -D INSTALL_C_EXAMPLES=OFF \
> -D OPENCV_ENABLE_NONFREE=ON \
> -D WITH_CUDA=ON \
> -D WITH_CUDNN=ON \
> -D OPENCV_DNN_CUDA=ON \
> -D ENABLE_FAST_MATH=1 \
> -D CUDA_FAST_MATH=1 \
> -D CUDA_ARCH_BIN=7.5 \
> -D WITH_CUBLAS=1 \
> -D OPENCV_EXTRA_MODULES_PATH=~/opencv_cuda/opencv_contrib/modules \
> -D HAVE_opencv_python3=ON \
> -D PYTHON_EXECUTABLE=~/.virtualenvs/opencv_cuda/bin/python \
>         -D WITH_TBB=ON \
>         -D WITH_V4L=ON \
>         -D WITH_OPENGL=ON \
> -D BUILD_EXAMPLES=ON ..
-- The CXX compiler identification is GNU 7.5.0
-- The C compiler identification is GNU 7.5.0
-- Check for working CXX compiler: /usr/bin/c++
-- Check for working CXX compiler: /usr/bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Check for working C compiler: /usr/bin/cc
-- Check for working C compiler: /usr/bin/cc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting C compile features - done
-- Detected processor: x86_64
-- Found PythonInterp: /home/dhankar/.virtualenvs/opencv_cuda/bin/python (found suitable version "3.7.4", minimum required is "2.7") 
CMake Warning at cmake/OpenCVDetectPython.cmake:81 (message):
  CMake's 'find_host_package(PythonInterp 2.7)' found wrong Python version:

  PYTHON_EXECUTABLE=/home/dhankar/.virtualenvs/opencv_cuda/bin/python

  PYTHON_VERSION_STRING=3.7.4

  Consider providing the 'PYTHON2_EXECUTABLE' variable via CMake command line
  or environment variables

Call Stack (most recent call first):
  cmake/OpenCVDetectPython.cmake:271 (find_python)
  CMakeLists.txt:598 (include)


-- Consider using CMake 3.12+ for better Python support
-- Found PythonInterp: /home/dhankar/.virtualenvs/opencv_cuda/bin/python3 (found suitable version "3.7.4", minimum required is "3.2") 
-- Could NOT find PythonLibs (missing: PYTHON_LIBRARIES PYTHON_INCLUDE_DIRS) (Required is exact version "3.7.4")
-- Looking for ccache - not found
-- Performing Test HAVE_CXX_FSIGNED_CHAR
-- Performing Test HAVE_CXX_FSIGNED_CHAR - Success
-- Performing Test HAVE_C_FSIGNED_CHAR
-- Performing Test HAVE_C_FSIGNED_CHAR - Success
-- Performing Test HAVE_CXX_FFAST_MATH
-- Performing Test HAVE_CXX_FFAST_MATH - Success
-- Performing Test HAVE_C_FFAST_MATH
-- Performing Test HAVE_C_FFAST_MATH - Success
-- Performing Test HAVE_CXX_W
-- Performing Test HAVE_CXX_W - Success
-- Performing Test HAVE_C_W
-- Performing Test HAVE_C_W - Success
-- Performing Test HAVE_CXX_WALL
-- Performing Test HAVE_CXX_WALL - Success
-- Performing Test HAVE_C_WALL
-- Performing Test HAVE_C_WALL - Success
-- Performing Test HAVE_CXX_WERROR_RETURN_TYPE
-- Performing Test HAVE_CXX_WERROR_RETURN_TYPE - Success
-- Performing Test HAVE_C_WERROR_RETURN_TYPE
-- Performing Test HAVE_C_WERROR_RETURN_TYPE - Success
-- Performing Test HAVE_CXX_WERROR_NON_VIRTUAL_DTOR
-- Performing Test HAVE_CXX_WERROR_NON_VIRTUAL_DTOR - Success
-- Performing Test HAVE_C_WERROR_NON_VIRTUAL_DTOR
-- Performing Test HAVE_C_WERROR_NON_VIRTUAL_DTOR - Failed
-- Performing Test HAVE_CXX_WERROR_ADDRESS
-- Performing Test HAVE_CXX_WERROR_ADDRESS - Success
-- Performing Test HAVE_C_WERROR_ADDRESS
-- Performing Test HAVE_C_WERROR_ADDRESS - Success
-- Performing Test HAVE_CXX_WERROR_SEQUENCE_POINT
-- Performing Test HAVE_CXX_WERROR_SEQUENCE_POINT - Success
-- Performing Test HAVE_C_WERROR_SEQUENCE_POINT
-- Performing Test HAVE_C_WERROR_SEQUENCE_POINT - Success
-- Performing Test HAVE_CXX_WFORMAT
-- Performing Test HAVE_CXX_WFORMAT - Success
-- Performing Test HAVE_C_WFORMAT
-- Performing Test HAVE_C_WFORMAT - Success
-- Performing Test HAVE_CXX_WERROR_FORMAT_SECURITY
-- Performing Test HAVE_CXX_WERROR_FORMAT_SECURITY - Success
-- Performing Test HAVE_C_WERROR_FORMAT_SECURITY
-- Performing Test HAVE_C_WERROR_FORMAT_SECURITY - Success
-- Performing Test HAVE_CXX_WMISSING_DECLARATIONS
-- Performing Test HAVE_CXX_WMISSING_DECLARATIONS - Success
-- Performing Test HAVE_C_WMISSING_DECLARATIONS
-- Performing Test HAVE_C_WMISSING_DECLARATIONS - Success
-- Performing Test HAVE_CXX_WMISSING_PROTOTYPES
-- Performing Test HAVE_CXX_WMISSING_PROTOTYPES - Failed
-- Performing Test HAVE_C_WMISSING_PROTOTYPES
-- Performing Test HAVE_C_WMISSING_PROTOTYPES - Success
-- Performing Test HAVE_CXX_WSTRICT_PROTOTYPES
-- Performing Test HAVE_CXX_WSTRICT_PROTOTYPES - Failed
-- Performing Test HAVE_C_WSTRICT_PROTOTYPES
-- Performing Test HAVE_C_WSTRICT_PROTOTYPES - Success
-- Performing Test HAVE_CXX_WUNDEF
-- Performing Test HAVE_CXX_WUNDEF - Success
-- Performing Test HAVE_C_WUNDEF
-- Performing Test HAVE_C_WUNDEF - Success
-- Performing Test HAVE_CXX_WINIT_SELF
-- Performing Test HAVE_CXX_WINIT_SELF - Success
-- Performing Test HAVE_C_WINIT_SELF
-- Performing Test HAVE_C_WINIT_SELF - Success
-- Performing Test HAVE_CXX_WPOINTER_ARITH
-- Performing Test HAVE_CXX_WPOINTER_ARITH - Success
-- Performing Test HAVE_C_WPOINTER_ARITH
-- Performing Test HAVE_C_WPOINTER_ARITH - Success
-- Performing Test HAVE_CXX_WSHADOW
-- Performing Test HAVE_CXX_WSHADOW - Success
-- Performing Test HAVE_C_WSHADOW
-- Performing Test HAVE_C_WSHADOW - Success
-- Performing Test HAVE_CXX_WSIGN_PROMO
-- Performing Test HAVE_CXX_WSIGN_PROMO - Success
-- Performing Test HAVE_C_WSIGN_PROMO
-- Performing Test HAVE_C_WSIGN_PROMO - Failed
-- Performing Test HAVE_CXX_WUNINITIALIZED
-- Performing Test HAVE_CXX_WUNINITIALIZED - Success
-- Performing Test HAVE_C_WUNINITIALIZED
-- Performing Test HAVE_C_WUNINITIALIZED - Success
-- Performing Test HAVE_CXX_WSUGGEST_OVERRIDE
-- Performing Test HAVE_CXX_WSUGGEST_OVERRIDE - Success
-- Performing Test HAVE_C_WSUGGEST_OVERRIDE
-- Performing Test HAVE_C_WSUGGEST_OVERRIDE - Failed
-- Performing Test HAVE_CXX_WNO_DELETE_NON_VIRTUAL_DTOR
-- Performing Test HAVE_CXX_WNO_DELETE_NON_VIRTUAL_DTOR - Success
-- Performing Test HAVE_C_WNO_DELETE_NON_VIRTUAL_DTOR
-- Performing Test HAVE_C_WNO_DELETE_NON_VIRTUAL_DTOR - Failed
-- Performing Test HAVE_CXX_WNO_UNNAMED_TYPE_TEMPLATE_ARGS
-- Performing Test HAVE_CXX_WNO_UNNAMED_TYPE_TEMPLATE_ARGS - Failed
-- Performing Test HAVE_C_WNO_UNNAMED_TYPE_TEMPLATE_ARGS
-- Performing Test HAVE_C_WNO_UNNAMED_TYPE_TEMPLATE_ARGS - Failed
-- Performing Test HAVE_CXX_WNO_COMMENT
-- Performing Test HAVE_CXX_WNO_COMMENT - Success
-- Performing Test HAVE_C_WNO_COMMENT
-- Performing Test HAVE_C_WNO_COMMENT - Success
-- Performing Test HAVE_CXX_WIMPLICIT_FALLTHROUGH_3
-- Performing Test HAVE_CXX_WIMPLICIT_FALLTHROUGH_3 - Success
-- Performing Test HAVE_C_WIMPLICIT_FALLTHROUGH_3
-- Performing Test HAVE_C_WIMPLICIT_FALLTHROUGH_3 - Success
-- Performing Test HAVE_CXX_WNO_STRICT_OVERFLOW
-- Performing Test HAVE_CXX_WNO_STRICT_OVERFLOW - Success
-- Performing Test HAVE_C_WNO_STRICT_OVERFLOW
-- Performing Test HAVE_C_WNO_STRICT_OVERFLOW - Success
-- Performing Test HAVE_CXX_FDIAGNOSTICS_SHOW_OPTION
-- Performing Test HAVE_CXX_FDIAGNOSTICS_SHOW_OPTION - Success
-- Performing Test HAVE_C_FDIAGNOSTICS_SHOW_OPTION
-- Performing Test HAVE_C_FDIAGNOSTICS_SHOW_OPTION - Success
-- Performing Test HAVE_CXX_WNO_LONG_LONG
-- Performing Test HAVE_CXX_WNO_LONG_LONG - Success
-- Performing Test HAVE_C_WNO_LONG_LONG
-- Performing Test HAVE_C_WNO_LONG_LONG - Success
-- Performing Test HAVE_CXX_PTHREAD
-- Performing Test HAVE_CXX_PTHREAD - Success
-- Performing Test HAVE_C_PTHREAD
-- Performing Test HAVE_C_PTHREAD - Success
-- Performing Test HAVE_CXX_FOMIT_FRAME_POINTER
-- Performing Test HAVE_CXX_FOMIT_FRAME_POINTER - Success
-- Performing Test HAVE_C_FOMIT_FRAME_POINTER
-- Performing Test HAVE_C_FOMIT_FRAME_POINTER - Success
-- Performing Test HAVE_CXX_FFUNCTION_SECTIONS
-- Performing Test HAVE_CXX_FFUNCTION_SECTIONS - Success
-- Performing Test HAVE_C_FFUNCTION_SECTIONS
-- Performing Test HAVE_C_FFUNCTION_SECTIONS - Success
-- Performing Test HAVE_CXX_FDATA_SECTIONS
-- Performing Test HAVE_CXX_FDATA_SECTIONS - Success
-- Performing Test HAVE_C_FDATA_SECTIONS
-- Performing Test HAVE_C_FDATA_SECTIONS - Success
-- Performing Test HAVE_CXX_MSSE (check file: cmake/checks/cpu_sse.cpp)
-- Performing Test HAVE_CXX_MSSE - Success
-- Performing Test HAVE_CXX_MSSE2 (check file: cmake/checks/cpu_sse2.cpp)
-- Performing Test HAVE_CXX_MSSE2 - Success
-- Performing Test HAVE_CXX_MSSE3 (check file: cmake/checks/cpu_sse3.cpp)
-- Performing Test HAVE_CXX_MSSE3 - Success
-- Performing Test HAVE_CXX_MSSSE3 (check file: cmake/checks/cpu_ssse3.cpp)
-- Performing Test HAVE_CXX_MSSSE3 - Success
-- Performing Test HAVE_CXX_MSSE4_1 (check file: cmake/checks/cpu_sse41.cpp)
-- Performing Test HAVE_CXX_MSSE4_1 - Success
-- Performing Test HAVE_CXX_MPOPCNT (check file: cmake/checks/cpu_popcnt.cpp)
-- Performing Test HAVE_CXX_MPOPCNT - Success
-- Performing Test HAVE_CXX_MSSE4_2 (check file: cmake/checks/cpu_sse42.cpp)
-- Performing Test HAVE_CXX_MSSE4_2 - Success
-- Performing Test HAVE_CXX_MF16C (check file: cmake/checks/cpu_fp16.cpp)
-- Performing Test HAVE_CXX_MF16C - Success
-- Performing Test HAVE_CXX_MFMA
-- Performing Test HAVE_CXX_MFMA - Success
-- Performing Test HAVE_CXX_MAVX (check file: cmake/checks/cpu_avx.cpp)
-- Performing Test HAVE_CXX_MAVX - Success
-- Performing Test HAVE_CXX_MAVX2 (check file: cmake/checks/cpu_avx2.cpp)
-- Performing Test HAVE_CXX_MAVX2 - Success
-- Performing Test HAVE_CXX_MAVX512F (check file: cmake/checks/cpu_avx512.cpp)
-- Performing Test HAVE_CXX_MAVX512F - Success
-- Performing Test HAVE_CXX_MAVX512F_MAVX512CD (check file: cmake/checks/cpu_avx512common.cpp)
-- Performing Test HAVE_CXX_MAVX512F_MAVX512CD - Success
-- Performing Test HAVE_CXX_MAVX512F_MAVX512CD_MAVX512VL_MAVX512BW_MAVX512DQ (check file: cmake/checks/cpu_avx512skx.cpp)
-- Performing Test HAVE_CXX_MAVX512F_MAVX512CD_MAVX512VL_MAVX512BW_MAVX512DQ - Success
-- Performing Test HAVE_CPU_BASELINE_FLAGS
-- Performing Test HAVE_CPU_BASELINE_FLAGS - Success
-- Performing Test HAVE_CPU_DISPATCH_FLAGS_SSE4_1
-- Performing Test HAVE_CPU_DISPATCH_FLAGS_SSE4_1 - Success
-- Performing Test HAVE_CPU_DISPATCH_FLAGS_SSE4_2
-- Performing Test HAVE_CPU_DISPATCH_FLAGS_SSE4_2 - Success
-- Performing Test HAVE_CPU_DISPATCH_FLAGS_FP16
-- Performing Test HAVE_CPU_DISPATCH_FLAGS_FP16 - Success
-- Performing Test HAVE_CPU_DISPATCH_FLAGS_AVX
-- Performing Test HAVE_CPU_DISPATCH_FLAGS_AVX - Success
-- Performing Test HAVE_CPU_DISPATCH_FLAGS_AVX2
-- Performing Test HAVE_CPU_DISPATCH_FLAGS_AVX2 - Success
-- Performing Test HAVE_CPU_DISPATCH_FLAGS_AVX512_SKX
-- Performing Test HAVE_CPU_DISPATCH_FLAGS_AVX512_SKX - Success
-- Performing Test HAVE_CXX_FVISIBILITY_HIDDEN
-- Performing Test HAVE_CXX_FVISIBILITY_HIDDEN - Success
-- Performing Test HAVE_C_FVISIBILITY_HIDDEN
-- Performing Test HAVE_C_FVISIBILITY_HIDDEN - Success
-- Performing Test HAVE_CXX_FVISIBILITY_INLINES_HIDDEN
-- Performing Test HAVE_CXX_FVISIBILITY_INLINES_HIDDEN - Success
-- Performing Test HAVE_C_FVISIBILITY_INLINES_HIDDEN
-- Performing Test HAVE_C_FVISIBILITY_INLINES_HIDDEN - Failed
-- Performing Test HAVE_LINK_AS_NEEDED
-- Performing Test HAVE_LINK_AS_NEEDED - Success
-- Looking for pthread.h
-- Looking for pthread.h - found
-- Looking for posix_memalign
-- Looking for posix_memalign - found
-- Looking for malloc.h
-- Looking for malloc.h - found
-- Looking for memalign
-- Looking for memalign - found
-- Check if the system is big endian
-- Searching 16 bit integer
-- Looking for sys/types.h
-- Looking for sys/types.h - found
-- Looking for stdint.h
-- Looking for stdint.h - found
-- Looking for stddef.h
-- Looking for stddef.h - found
-- Check size of unsigned short
-- Check size of unsigned short - done
-- Using unsigned short
-- Check if the system is big endian - little endian
-- Found ZLIB: /usr/lib/x86_64-linux-gnu/libz.so (found suitable version "1.2.11", minimum required is "1.2.3") 
-- Found JPEG: /usr/lib/x86_64-linux-gnu/libjpeg.so  
-- Found TIFF: /usr/lib/x86_64-linux-gnu/libtiff.so (found version "4.0.9") 
-- Found WebP: /usr/lib/x86_64-linux-gnu/libwebp.so  
-- The imported target "openjp2_static" references the file
   "/usr/lib/x86_64-linux-gnu/libopenjp2.a"
but this file does not exist.  Possible reasons include:
* The file was deleted, renamed, or moved to another location.
* An install or uninstall procedure did not complete successfully.
* The installation package was faulty and contained
   "/usr/lib/x86_64-linux-gnu/openjpeg-2.3/OpenJPEGTargets.cmake"
but not all the files it references.

-- The imported target "openjpip" references the file
   "/usr/lib/x86_64-linux-gnu/libopenjpip.so.2.3.0"
but this file does not exist.  Possible reasons include:
* The file was deleted, renamed, or moved to another location.
* An install or uninstall procedure did not complete successfully.
* The installation package was faulty and contained
   "/usr/lib/x86_64-linux-gnu/openjpeg-2.3/OpenJPEGTargets.cmake"
but not all the files it references.

-- The imported target "openjpip_server" references the file
   "/usr/lib/x86_64-linux-gnu/libopenjpip_server.a"
but this file does not exist.  Possible reasons include:
* The file was deleted, renamed, or moved to another location.
* An install or uninstall procedure did not complete successfully.
* The installation package was faulty and contained
   "/usr/lib/x86_64-linux-gnu/openjpeg-2.3/OpenJPEGTargets.cmake"
but not all the files it references.

-- The imported target "opj_decompress" references the file
   "/usr/bin/opj_decompress"
but this file does not exist.  Possible reasons include:
* The file was deleted, renamed, or moved to another location.
* An install or uninstall procedure did not complete successfully.
* The installation package was faulty and contained
   "/usr/lib/x86_64-linux-gnu/openjpeg-2.3/OpenJPEGTargets.cmake"
but not all the files it references.

-- The imported target "opj_compress" references the file
   "/usr/bin/opj_compress"
but this file does not exist.  Possible reasons include:
* The file was deleted, renamed, or moved to another location.
* An install or uninstall procedure did not complete successfully.
* The installation package was faulty and contained
   "/usr/lib/x86_64-linux-gnu/openjpeg-2.3/OpenJPEGTargets.cmake"
but not all the files it references.

-- The imported target "opj_dump" references the file
   "/usr/bin/opj_dump"
but this file does not exist.  Possible reasons include:
* The file was deleted, renamed, or moved to another location.
* An install or uninstall procedure did not complete successfully.
* The installation package was faulty and contained
   "/usr/lib/x86_64-linux-gnu/openjpeg-2.3/OpenJPEGTargets.cmake"
but not all the files it references.

-- The imported target "opj_jpip_addxml" references the file
   "/usr/bin/opj_jpip_addxml"
but this file does not exist.  Possible reasons include:
* The file was deleted, renamed, or moved to another location.
* An install or uninstall procedure did not complete successfully.
* The installation package was faulty and contained
   "/usr/lib/x86_64-linux-gnu/openjpeg-2.3/OpenJPEGTargets.cmake"
but not all the files it references.

-- The imported target "opj_server" references the file
   "/usr/bin/opj_server"
but this file does not exist.  Possible reasons include:
* The file was deleted, renamed, or moved to another location.
* An install or uninstall procedure did not complete successfully.
* The installation package was faulty and contained
   "/usr/lib/x86_64-linux-gnu/openjpeg-2.3/OpenJPEGTargets.cmake"
but not all the files it references.

-- The imported target "opj_dec_server" references the file
   "/usr/bin/opj_dec_server"
but this file does not exist.  Possible reasons include:
* The file was deleted, renamed, or moved to another location.
* An install or uninstall procedure did not complete successfully.
* The installation package was faulty and contained
   "/usr/lib/x86_64-linux-gnu/openjpeg-2.3/OpenJPEGTargets.cmake"
but not all the files it references.

-- The imported target "opj_jpip_transcode" references the file
   "/usr/bin/opj_jpip_transcode"
but this file does not exist.  Possible reasons include:
* The file was deleted, renamed, or moved to another location.
* An install or uninstall procedure did not complete successfully.
* The installation package was faulty and contained
   "/usr/lib/x86_64-linux-gnu/openjpeg-2.3/OpenJPEGTargets.cmake"
but not all the files it references.

-- The imported target "opj_jpip_test" references the file
   "/usr/bin/opj_jpip_test"
but this file does not exist.  Possible reasons include:
* The file was deleted, renamed, or moved to another location.
* An install or uninstall procedure did not complete successfully.
* The installation package was faulty and contained
   "/usr/lib/x86_64-linux-gnu/openjpeg-2.3/OpenJPEGTargets.cmake"
but not all the files it references.

-- Found OpenJPEG: openjp2 (found version "2.3.0")
-- Found ZLIB: /usr/lib/x86_64-linux-gnu/libz.so (found version "1.2.11") 
-- Found PNG: /usr/lib/x86_64-linux-gnu/libpng.so (found version "1.6.34") 
-- Looking for /usr/include/libpng/png.h
-- Looking for /usr/include/libpng/png.h - found
-- Looking for semaphore.h
-- Looking for semaphore.h - found
-- Performing Test HAVE_CXX_WNO_SHADOW
-- Performing Test HAVE_CXX_WNO_SHADOW - Success
-- Performing Test HAVE_CXX_WNO_UNUSED
-- Performing Test HAVE_CXX_WNO_UNUSED - Success
-- Performing Test HAVE_CXX_WNO_SIGN_COMPARE
-- Performing Test HAVE_CXX_WNO_SIGN_COMPARE - Success
-- Performing Test HAVE_CXX_WNO_UNDEF
-- Performing Test HAVE_CXX_WNO_UNDEF - Success
-- Performing Test HAVE_CXX_WNO_MISSING_DECLARATIONS
-- Performing Test HAVE_CXX_WNO_MISSING_DECLARATIONS - Success
-- Performing Test HAVE_CXX_WNO_UNINITIALIZED
-- Performing Test HAVE_CXX_WNO_UNINITIALIZED - Success
-- Performing Test HAVE_CXX_WNO_SWITCH
-- Performing Test HAVE_CXX_WNO_SWITCH - Success
-- Performing Test HAVE_CXX_WNO_PARENTHESES
-- Performing Test HAVE_CXX_WNO_PARENTHESES - Success
-- Performing Test HAVE_CXX_WNO_ARRAY_BOUNDS
-- Performing Test HAVE_CXX_WNO_ARRAY_BOUNDS - Success
-- Performing Test HAVE_CXX_WNO_EXTRA
-- Performing Test HAVE_CXX_WNO_EXTRA - Success
-- Performing Test HAVE_CXX_WNO_DEPRECATED_DECLARATIONS
-- Performing Test HAVE_CXX_WNO_DEPRECATED_DECLARATIONS - Success
-- Performing Test HAVE_CXX_WNO_MISLEADING_INDENTATION
-- Performing Test HAVE_CXX_WNO_MISLEADING_INDENTATION - Success
-- Performing Test HAVE_CXX_WNO_DEPRECATED
-- Performing Test HAVE_CXX_WNO_DEPRECATED - Success
-- Performing Test HAVE_CXX_WNO_SUGGEST_OVERRIDE
-- Performing Test HAVE_CXX_WNO_SUGGEST_OVERRIDE - Success
-- Performing Test HAVE_CXX_WNO_INCONSISTENT_MISSING_OVERRIDE
-- Performing Test HAVE_CXX_WNO_INCONSISTENT_MISSING_OVERRIDE - Failed
-- Performing Test HAVE_CXX_WNO_IMPLICIT_FALLTHROUGH
-- Performing Test HAVE_CXX_WNO_IMPLICIT_FALLTHROUGH - Success
-- Performing Test HAVE_CXX_WNO_TAUTOLOGICAL_COMPARE
-- Performing Test HAVE_CXX_WNO_TAUTOLOGICAL_COMPARE - Success
-- Performing Test HAVE_CXX_WNO_MISSING_PROTOTYPES
-- Performing Test HAVE_CXX_WNO_MISSING_PROTOTYPES - Failed
-- Performing Test HAVE_CXX_WNO_REORDER
-- Performing Test HAVE_CXX_WNO_REORDER - Success
-- Performing Test HAVE_CXX_WNO_UNUSED_RESULT
-- Performing Test HAVE_CXX_WNO_UNUSED_RESULT - Success
-- Checking for module 'gtk+-3.0'
--   Found gtk+-3.0, version 3.22.30
-- Checking for module 'gthread-2.0'
--   Found gthread-2.0, version 2.56.4
-- IPPICV: Download: ippicv_2020_lnx_intel64_20191018_general.tgz
-- found Intel IPP (ICV version): 2020.0.0 [2020.0.0 Gold]
-- at: /home/dhankar/opencv_cuda/opencv/build/3rdparty/ippicv/ippicv_lnx/icv
-- found Intel IPP Integration Wrappers sources: 2020.0.0
-- at: /home/dhankar/opencv_cuda/opencv/build/3rdparty/ippicv/ippicv_lnx/iw
-- Looking for pthread.h
-- Looking for pthread.h - found
-- Looking for pthread_create
-- Looking for pthread_create - not found
-- Looking for pthread_create in pthreads
-- Looking for pthread_create in pthreads - not found
-- Looking for pthread_create in pthread
-- Looking for pthread_create in pthread - found
-- Found Threads: TRUE  
-- Could NOT find CUDNN (missing: CUDNN_LIBRARY CUDNN_INCLUDE_DIR) (Required is at least version "7.5")
-- CUDA detected: 9.1
-- CUDA NVCC target flags: -gencode;arch=compute_75,code=sm_75;-D_FORCE_INLINES
-- Could not find OpenBLAS include. Turning OpenBLAS_FOUND off
-- Could not find OpenBLAS lib. Turning OpenBLAS_FOUND off
-- Could NOT find Atlas (missing: Atlas_CLAPACK_INCLUDE_DIR) 
-- Looking for sgemm_
-- Looking for sgemm_ - found
-- A library with BLAS API found.
-- Looking for cheev_
-- Looking for cheev_ - found
-- A library with LAPACK API found.
-- Performing Test HAVE_CXX_WNO_UNUSED_PARAMETER
-- Performing Test HAVE_CXX_WNO_UNUSED_PARAMETER - Success
-- Performing Test HAVE_CXX_WNO_UNUSED_LOCAL_TYPEDEFS
-- Performing Test HAVE_CXX_WNO_UNUSED_LOCAL_TYPEDEFS - Success
-- Performing Test HAVE_CXX_WNO_SIGN_PROMO
-- Performing Test HAVE_CXX_WNO_SIGN_PROMO - Success
-- Performing Test HAVE_CXX_WNO_TAUTOLOGICAL_UNDEFINED_COMPARE
-- Performing Test HAVE_CXX_WNO_TAUTOLOGICAL_UNDEFINED_COMPARE - Failed
-- Performing Test HAVE_CXX_WNO_IGNORED_QUALIFIERS
-- Performing Test HAVE_CXX_WNO_IGNORED_QUALIFIERS - Success
-- Performing Test HAVE_CXX_WNO_UNUSED_FUNCTION
-- Performing Test HAVE_CXX_WNO_UNUSED_FUNCTION - Success
-- Performing Test HAVE_CXX_WNO_UNUSED_CONST_VARIABLE
-- Performing Test HAVE_CXX_WNO_UNUSED_CONST_VARIABLE - Success
-- Performing Test HAVE_CXX_WNO_SHORTEN_64_TO_32
-- Performing Test HAVE_CXX_WNO_SHORTEN_64_TO_32 - Failed
-- Performing Test HAVE_CXX_WNO_INVALID_OFFSETOF
-- Performing Test HAVE_CXX_WNO_INVALID_OFFSETOF - Success
-- Performing Test HAVE_CXX_WNO_ENUM_COMPARE_SWITCH
-- Performing Test HAVE_CXX_WNO_ENUM_COMPARE_SWITCH - Failed
-- Could NOT find JNI (missing: JAVA_INCLUDE_PATH JAVA_INCLUDE_PATH2 JAVA_AWT_INCLUDE_PATH) 
-- Could NOT find Pylint (missing: PYLINT_EXECUTABLE) 
-- Could NOT find Flake8 (missing: FLAKE8_EXECUTABLE) 
-- VTK is not found. Please set -DVTK_DIR in CMake to VTK build directory, or to VTK install subdirectory with VTKConfig.cmake file
-- Performing Test HAVE_C_WNO_UNUSED_VARIABLE
-- Performing Test HAVE_C_WNO_UNUSED_VARIABLE - Success
-- Performing Test HAVE_C_WNO_SHADOW
-- Performing Test HAVE_C_WNO_SHADOW - Success
-- Looking for dlerror in dl
-- Looking for dlerror in dl - found
-- Performing Test HAVE_C_WNO_IMPLICIT_FALLTHROUGH
-- Performing Test HAVE_C_WNO_IMPLICIT_FALLTHROUGH - Success
-- Performing Test HAVE_C_WNO_UNDEF
-- Performing Test HAVE_C_WNO_UNDEF - Success
-- Performing Test HAVE_C_WNO_SIGN_COMPARE
-- Performing Test HAVE_C_WNO_SIGN_COMPARE - Success
-- ADE: Download: v0.1.1f.zip
-- OpenCV Python: during development append to PYTHONPATH: /home/dhankar/opencv_cuda/opencv/build/python_loader
-- Performing Test HAVE_CXX_WNO_STRICT_ALIASING
-- Performing Test HAVE_CXX_WNO_STRICT_ALIASING - Success
-- Checking for modules 'libavcodec;libavformat;libavutil;libswscale'
--   Found libavcodec, version 58.35.100
--   Found libavformat, version 58.20.100
--   Found libavutil, version 56.22.100
--   Found libswscale, version 5.3.100
-- Checking for module 'libavresample'
--   No package 'libavresample' found
-- Checking for module 'gstreamer-base-1.0'
--   No package 'gstreamer-base-1.0' found
-- Checking for module 'gstreamer-app-1.0'
--   No package 'gstreamer-app-1.0' found
-- Checking for module 'gstreamer-riff-1.0'
--   No package 'gstreamer-riff-1.0' found
-- Checking for module 'gstreamer-pbutils-1.0'
--   No package 'gstreamer-pbutils-1.0' found
-- Checking for module 'libdc1394-2'
--   No package 'libdc1394-2' found
-- Caffe:   NO
-- Protobuf:   NO
-- Glog:   NO
-- Performing Test HAVE_CXX_WNO_UNUSED_VARIABLE
-- Performing Test HAVE_CXX_WNO_UNUSED_VARIABLE - Success
-- Performing Test HAVE_CXX_WNO_ENUM_COMPARE
-- Performing Test HAVE_CXX_WNO_ENUM_COMPARE - Success
-- Checking for module 'freetype2'
--   Found freetype2, version 21.0.15
-- Checking for module 'harfbuzz'
--   Found harfbuzz, version 1.7.2
-- freetype2:   YES (ver 21.0.15)
-- harfbuzz:    YES (ver 1.7.2)
-- HDF5: Using hdf5 compiler wrapper to determine C configuration
-- Found HDF5: /usr/lib/x86_64-linux-gnu/hdf5/serial/libhdf5.so;/usr/lib/x86_64-linux-gnu/libpthread.so;/usr/lib/x86_64-linux-gnu/libsz.so;/usr/lib/x86_64-linux-gnu/libz.so;/usr/lib/x86_64-linux-gnu/libdl.so;/usr/lib/x86_64-linux-gnu/libm.so (found version "1.10.0.1")  
-- Module opencv_ovis disabled because OGRE3D was not found
-- No preference for use of exported gflags CMake configuration set, and no hints for include/library directories provided. Defaulting to preferring an installed/exported gflags CMake configuration if available.
-- Failed to find installed gflags CMake configuration, searching for gflags build directories exported with CMake.
-- Found exported gflags build directory: /home/dhankar/_dc_all/odmOwnUp/OpenDroneMap/ODM/SuperBuild/install/lib/cmake/gflags
-- Detected gflags version: 2.2.2
-- Failed to find glog - Could not find glog include directory, set GLOG_INCLUDE_DIR to directory containing glog/logging.h
-- Module opencv_sfm disabled because the following dependencies are not found: Glog/Gflags
-- Checking for module 'tesseract'
--   Found tesseract, version 4.0.0-beta.1
-- Tesseract:   YES (ver 4.0.0-beta.1)
-- Allocator metrics storage type: 'long long'
-- Performing Test HAVE_CXX_WNO_UNUSED_BUT_SET_VARIABLE
-- Performing Test HAVE_CXX_WNO_UNUSED_BUT_SET_VARIABLE - Success
-- HDF5: Using hdf5 compiler wrapper to determine C configuration
-- Registering hook 'INIT_MODULE_SOURCES_opencv_dnn': /home/dhankar/opencv_cuda/opencv/modules/dnn/cmake/hooks/INIT_MODULE_SOURCES_opencv_dnn.cmake
-- opencv_dnn: filter out cuda4dnn source code
-- Performing Test HAVE_CXX_WNO_OVERLOADED_VIRTUAL
-- Performing Test HAVE_CXX_WNO_OVERLOADED_VIRTUAL - Success
-- xfeatures2d/boostdesc: Download: boostdesc_bgm.i
-- xfeatures2d/boostdesc: Download: boostdesc_bgm_bi.i
-- xfeatures2d/boostdesc: Download: boostdesc_bgm_hd.i
-- xfeatures2d/boostdesc: Download: boostdesc_binboost_064.i
-- xfeatures2d/boostdesc: Download: boostdesc_binboost_128.i
-- xfeatures2d/boostdesc: Download: boostdesc_binboost_256.i
-- xfeatures2d/boostdesc: Download: boostdesc_lbgm.i
-- xfeatures2d/vgg: Download: vgg_generated_48.i
-- xfeatures2d/vgg: Download: vgg_generated_64.i
-- xfeatures2d/vgg: Download: vgg_generated_80.i
-- xfeatures2d/vgg: Download: vgg_generated_120.i
-- data: Download: face_landmark_model.dat
-- NVIDIA_OPTICAL_FLOW: Download: 79c6cee80a2df9a196f20afd6b598a9810964c32.zip
-- 
-- General configuration for OpenCV 4.3.0 =====================================
--   Version control:               unknown
-- 
--   Extra modules:
--     Location (extra):            /home/dhankar/opencv_cuda/opencv_contrib/modules
--     Version control (extra):     unknown
-- 
--   Platform:
--     Timestamp:                   2020-07-25T12:43:57Z
--     Host:                        Linux 5.4.0-42-generic x86_64
--     CMake:                       3.10.2
--     CMake generator:             Unix Makefiles
--     CMake build tool:            /usr/bin/make
--     Configuration:               RELEASE
-- 
--   CPU/HW features:
--     Baseline:                    SSE SSE2 SSE3
--       requested:                 SSE3
--     Dispatched code generation:  SSE4_1 SSE4_2 FP16 AVX AVX2 AVX512_SKX
--       requested:                 SSE4_1 SSE4_2 AVX FP16 AVX2 AVX512_SKX
--       SSE4_1 (16 files):         + SSSE3 SSE4_1
--       SSE4_2 (2 files):          + SSSE3 SSE4_1 POPCNT SSE4_2
--       FP16 (1 files):            + SSSE3 SSE4_1 POPCNT SSE4_2 FP16 AVX
--       AVX (5 files):             + SSSE3 SSE4_1 POPCNT SSE4_2 AVX
--       AVX2 (30 files):           + SSSE3 SSE4_1 POPCNT SSE4_2 FP16 FMA3 AVX AVX2
--       AVX512_SKX (6 files):      + SSSE3 SSE4_1 POPCNT SSE4_2 FP16 FMA3 AVX AVX2 AVX_512F AVX512_COMMON AVX512_SKX
-- 
--   C/C++:
--     Built as dynamic libs?:      YES
--     C++ standard:                11
--     C++ Compiler:                /usr/bin/c++  (ver 7.5.0)
--     C++ flags (Release):         -fsigned-char -ffast-math -W -Wall -Werror=return-type -Werror=non-virtual-dtor -Werror=address -Werror=sequence-point -Wformat -Werror=format-security -Wmissing-declarations -Wundef -Winit-self -Wpointer-arith -Wshadow -Wsign-promo -Wuninitialized -Winit-self -Wsuggest-override -Wno-delete-non-virtual-dtor -Wno-comment -Wimplicit-fallthrough=3 -Wno-strict-overflow -fdiagnostics-show-option -Wno-long-long -pthread -fomit-frame-pointer -ffunction-sections -fdata-sections  -msse -msse2 -msse3 -fvisibility=hidden -fvisibility-inlines-hidden -O3 -DNDEBUG  -DNDEBUG
--     C++ flags (Debug):           -fsigned-char -ffast-math -W -Wall -Werror=return-type -Werror=non-virtual-dtor -Werror=address -Werror=sequence-point -Wformat -Werror=format-security -Wmissing-declarations -Wundef -Winit-self -Wpointer-arith -Wshadow -Wsign-promo -Wuninitialized -Winit-self -Wsuggest-override -Wno-delete-non-virtual-dtor -Wno-comment -Wimplicit-fallthrough=3 -Wno-strict-overflow -fdiagnostics-show-option -Wno-long-long -pthread -fomit-frame-pointer -ffunction-sections -fdata-sections  -msse -msse2 -msse3 -fvisibility=hidden -fvisibility-inlines-hidden -g  -O0 -DDEBUG -D_DEBUG
--     C Compiler:                  /usr/bin/cc
--     C flags (Release):           -fsigned-char -ffast-math -W -Wall -Werror=return-type -Werror=address -Werror=sequence-point -Wformat -Werror=format-security -Wmissing-declarations -Wmissing-prototypes -Wstrict-prototypes -Wundef -Winit-self -Wpointer-arith -Wshadow -Wuninitialized -Winit-self -Wno-comment -Wimplicit-fallthrough=3 -Wno-strict-overflow -fdiagnostics-show-option -Wno-long-long -pthread -fomit-frame-pointer -ffunction-sections -fdata-sections  -msse -msse2 -msse3 -fvisibility=hidden -O3 -DNDEBUG  -DNDEBUG
--     C flags (Debug):             -fsigned-char -ffast-math -W -Wall -Werror=return-type -Werror=address -Werror=sequence-point -Wformat -Werror=format-security -Wmissing-declarations -Wmissing-prototypes -Wstrict-prototypes -Wundef -Winit-self -Wpointer-arith -Wshadow -Wuninitialized -Winit-self -Wno-comment -Wimplicit-fallthrough=3 -Wno-strict-overflow -fdiagnostics-show-option -Wno-long-long -pthread -fomit-frame-pointer -ffunction-sections -fdata-sections  -msse -msse2 -msse3 -fvisibility=hidden -g  -O0 -DDEBUG -D_DEBUG
--     Linker flags (Release):      -Wl,--exclude-libs,libippicv.a -Wl,--exclude-libs,libippiw.a   -Wl,--gc-sections -Wl,--as-needed  
--     Linker flags (Debug):        -Wl,--exclude-libs,libippicv.a -Wl,--exclude-libs,libippiw.a   -Wl,--gc-sections -Wl,--as-needed  
--     ccache:                      NO
--     Precompiled headers:         NO
--     Extra dependencies:          m pthread cudart_static -lpthread dl rt nppc nppial nppicc nppicom nppidei nppif nppig nppim nppist nppisu nppitc npps cublas cufft -L/usr/lib/x86_64-linux-gnu
--     3rdparty dependencies:
-- 
--   OpenCV modules:
--     To be built:                 alphamat aruco bgsegm bioinspired calib3d ccalib core cudaarithm cudabgsegm cudacodec cudafeatures2d cudafilters cudaimgproc cudalegacy cudaobjdetect cudaoptflow cudastereo cudawarping cudev datasets dnn dnn_objdetect dnn_superres dpm face features2d flann freetype fuzzy gapi hdf hfs highgui img_hash imgcodecs imgproc intensity_transform line_descriptor ml objdetect optflow phase_unwrapping photo plot quality rapid reg rgbd saliency shape stereo stitching structured_light superres surface_matching text tracking ts video videoio videostab xfeatures2d ximgproc xobjdetect xphoto
--     Disabled:                    world
--     Disabled by dependency:      -
--     Unavailable:                 cnn_3dobj cvv java js matlab ovis python2 python3 sfm viz
--     Applications:                tests perf_tests examples apps
--     Documentation:               NO
--     Non-free algorithms:         YES
-- 
--   GUI: 
--     GTK+:                        YES (ver 3.22.30)
--       GThread :                  YES (ver 2.56.4)
--       GtkGlExt:                  NO
--     OpenGL support:              NO
--     VTK support:                 NO
-- 
--   Media I/O: 
--     ZLib:                        /usr/lib/x86_64-linux-gnu/libz.so (ver 1.2.11)
--     JPEG:                        /usr/lib/x86_64-linux-gnu/libjpeg.so (ver 80)
--     WEBP:                        /usr/lib/x86_64-linux-gnu/libwebp.so (ver encoder: 0x020e)
--     PNG:                         /usr/lib/x86_64-linux-gnu/libpng.so (ver 1.6.34)
--     TIFF:                        /usr/lib/x86_64-linux-gnu/libtiff.so (ver 42 / 4.0.9)
--     JPEG 2000:                   OpenJPEG (ver 2.3.0)
--     OpenEXR:                     build (ver 2.3.0)
--     HDR:                         YES
--     SUNRASTER:                   YES
--     PXM:                         YES
--     PFM:                         YES
-- 
--   Video I/O:
--     DC1394:                      NO
--     FFMPEG:                      YES
--       avcodec:                   YES (58.35.100)
--       avformat:                  YES (58.20.100)
--       avutil:                    YES (56.22.100)
--       swscale:                   YES (5.3.100)
--       avresample:                NO
--     GStreamer:                   NO
--     v4l/v4l2:                    YES (linux/videodev2.h)
-- 
--   Parallel framework:            pthreads
-- 
--   Trace:                         YES (with Intel ITT)
-- 
--   Other third-party libraries:
--     Intel IPP:                   2020.0.0 Gold [2020.0.0]
--            at:                   /home/dhankar/opencv_cuda/opencv/build/3rdparty/ippicv/ippicv_lnx/icv
--     Intel IPP IW:                sources (2020.0.0)
--               at:                /home/dhankar/opencv_cuda/opencv/build/3rdparty/ippicv/ippicv_lnx/iw
--     Lapack:                      NO
--     Eigen:                       YES (ver 3.3.4)
--     Custom HAL:                  NO
--     Protobuf:                    build (3.5.1)
-- 
--   NVIDIA CUDA:                   YES (ver 9.1, CUFFT CUBLAS FAST_MATH)
--     NVIDIA GPU arch:             75
--     NVIDIA PTX archs:
-- 
--   cuDNN:                         NO
-- 
--   OpenCL:                        YES (no extra features)
--     Include path:                /home/dhankar/opencv_cuda/opencv/3rdparty/include/opencl/1.2
--     Link libraries:              Dynamic load
-- 
--   Python (for build):            /home/dhankar/.virtualenvs/opencv_cuda/bin/python3
-- 
--   Java:                          
--     ant:                         NO
--     JNI:                         NO
--     Java wrappers:               NO
--     Java tests:                  NO
-- 
--   Install to:                    /usr/local
-- -----------------------------------------------------------------
-- 
-- Configuring done
-- Generating done
-- Build files have been written to: /home/dhankar/opencv_cuda/opencv/build
(opencv_cuda) dhankar@dhankar-1:~/opencv_cuda/opencv/build$ 
(opencv_cuda) dhankar@dhankar-1:~/opencv_cuda/opencv/build$ 

