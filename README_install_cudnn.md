###### Install the latest compatible version of the - CUDNN
Last attempt at Build for CUDA supported OpenCV gave error for CUDNN as seen below  -

```
Could NOT find CUDNN (missing: CUDNN_LIBRARY CUDNN_INCLUDE_DIR) (Required is at least version "7.5")
```
#
```
(base) dhankar@dhankar-1:~/opencv_cuda/cudNN_installers$ ls -ltr
total 1009620
-rw-rw-r-- 1 dhankar dhankar   4263872 Jul 25 22:50 libcudnn8-doc_8.0.1.13-1+cuda11.0_amd64.deb
-rw-rw-r-- 1 dhankar dhankar 308249274 Jul 25 22:50 libcudnn8_8.0.1.13-1+cuda11.0_amd64.deb
-rw-rw-r-- 1 dhankar dhankar 307894558 Jul 25 22:50 libcudnn8_8.0.1.13-1+cuda11.0_ppc64el.deb
-rw-rw-r-- 1 dhankar dhankar   5182040 Jul 25 22:50 libcudnn8-doc_8.0.1.13-1+cuda11.0_ppc64el.deb
-rw-rw-r-- 1 dhankar dhankar 408239062 Jul 25 22:51 libcudnn8-dev_8.0.1.13-1+cuda11.0_ppc64el.deb

(base) dhankar@dhankar-1:~/opencv_cuda/cudNN_installers$ dpkg -l | grep cudnn
ii  libcudnn7                                  7.6.4.38-1+cuda10.1                              amd64        cuDNN runtime libraries
(base) dhankar@dhankar-1:~/opencv_cuda/cudNN_installers$ 
```

##### Before installing new compatible versions of - CUDNN -  need to remove using - dpkg - the old version seen above. 

```
(base) dhankar@dhankar-1:~/opencv_cuda/cudNN_installers$ sudo dpkg -r libcudnn7
[sudo] password for dhankar: 
(Reading database ... 314041 files and directories currently installed.)
Removing libcudnn7 (7.6.4.38-1+cuda10.1) ...
Processing triggers for libc-bin (2.27-3ubuntu1.2) ...

(base) dhankar@dhankar-1:~/opencv_cuda/cudNN_installers$ dpkg -l | grep cudnn

```
#

> sudo dpkg -i libcudnn8_8.0.1.13-1+cuda11.0_amd64.deb   
sudo dpkg -i libcudnn8-dev_8.0.1.13-1+cuda11.0_amd64.deb   
sudo dpkg -i libcudnn8-doc_8.0.1.13-1+cuda11.0_amd64.deb   

#

```
#

(base) dhankar@dhankar-1:~/opencv_cuda/cudNN_installers$ sudo dpkg -i libcudnn8_8.0.1.13-1+cuda11.0_amd64.deb
[sudo] password for dhankar: 
Selecting previously unselected package libcudnn8.
(Reading database ... 314036 files and directories currently installed.)
Preparing to unpack libcudnn8_8.0.1.13-1+cuda11.0_amd64.deb ...
Unpacking libcudnn8 (8.0.1.13-1+cuda11.0) ...
Setting up libcudnn8 (8.0.1.13-1+cuda11.0) ...
Processing triggers for libc-bin (2.27-3ubuntu1.2) ...

(base) dhankar@dhankar-1:~/opencv_cuda/cudNN_installers$ sudo dpkg -i libcudnn8-dev_8.0.1.13-1+cuda11.0_amd64.deb
Selecting previously unselected package libcudnn8-dev.
(Reading database ... 314054 files and directories currently installed.)
Preparing to unpack libcudnn8-dev_8.0.1.13-1+cuda11.0_amd64.deb ...
Unpacking libcudnn8-dev (8.0.1.13-1+cuda11.0) ...
Setting up libcudnn8-dev (8.0.1.13-1+cuda11.0) ...
update-alternatives: using /usr/include/x86_64-linux-gnu/cudnn_v8.h to provide /usr/include/cudnn.h (libcudnn) in auto mode
(base) dhankar@dhankar-1:~/opencv_cuda/cudNN_installers$ 

(base) dhankar@dhankar-1:~/opencv_cuda/cudNN_installers$ sudo dpkg -i libcudnn8-doc_8.0.1.13-1+cuda11.0_amd64.deb
[sudo] password for dhankar: 
Selecting previously unselected package libcudnn8-doc.
(Reading database ... 314074 files and directories currently installed.)
Preparing to unpack libcudnn8-doc_8.0.1.13-1+cuda11.0_amd64.deb ...
Unpacking libcudnn8-doc (8.0.1.13-1+cuda11.0) ...
Setting up libcudnn8-doc (8.0.1.13-1+cuda11.0) ...
(base) dhankar@dhankar-1:~/opencv_cuda/cudNN_installers$ 


```
#

```
# below paths for documentation purpose only , not to be used for CMAKE
/usr/share/doc/libcudnn8
/usr/share/doc/libcudnn8-dev
#

(base) dhankar@dhankar-1:~/opencv_cuda/cudNN_installers$ dpkg -l | grep cudnn
ii  libcudnn8                                  8.0.1.13-1+cuda11.0                              amd64        cuDNN runtime libraries
ii  libcudnn8-dev                              8.0.1.13-1+cuda11.0                              amd64        cuDNN development libraries and
headers
ii  libcudnn8-doc                              8.0.1.13-1+cuda11.0                              amd64        cuDNN documents and samples

#

(base) dhankar@dhankar-1:~/opencv_cuda/cudNN_installers$ locate libcudnn | grep cudnn8-dev
/home/dhankar/opencv_cuda/cudNN_installers/libcudnn8-dev_8.0.1.13-1+cuda11.0_amd64.deb
/home/dhankar/opencv_cuda/cudNN_installers/libcudnn8-dev_8.0.1.13-1+cuda11.0_ppc64el.deb
/usr/share/doc/libcudnn8-dev
/usr/share/doc/libcudnn8-dev/changelog.Debian.gz
/usr/share/doc/libcudnn8-dev/copyright
/usr/share/lintian/overrides/libcudnn8-dev
/var/lib/dpkg/info/libcudnn8-dev.list
/var/lib/dpkg/info/libcudnn8-dev.md5sums
/var/lib/dpkg/info/libcudnn8-dev.postinst
/var/lib/dpkg/info/libcudnn8-dev.prerm
(base) dhankar@dhankar-1:~/opencv_cuda/cudNN_installers$ 

```
#

> Now within the - CmakeCache.txt file - we will need to provide the DIR PATH for the - cudnn - installed. 
//location of the cuDNN library
CUDNN_LIBRARY:FILEPATH=CUDA_cudnn_LIBRARY-NOTFOUND

#
```
dhankar@dhankar-1:~$ cd /usr/local/
dhankar@dhankar-1:/usr/local$ 
dhankar@dhankar-1:/usr/local$ ls -ltr
total 40
............................
drwxr-xr-x 10 root root 4096 Jul 21 18:42 share
drwxr-xr-x 15 root root 4096 Jul 25 16:58 cuda-11.0
drwxr-xr-x  2 root root 4096 Jul 25 16:58 bin
lrwxrwxrwx  1 root root    9 Jul 25 16:59 cuda -> cuda-11.0
#
dhankar@dhankar-1:/usr/local$ cd cuda-11.0
dhankar@dhankar-1:/usr/local/cuda-11.0$ ls -ltr
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
dhankar@dhankar-1:/usr/local/cuda-11.0$ 
dhankar@dhankar-1:/usr/local/cuda-11.0$ # gedit version.txt # CUDA Version 11.0.207
#
dhankar@dhankar-1:/usr/local/cuda-11.0$ cd ..
dhankar@dhankar-1:/usr/local$ cd cuda
dhankar@dhankar-1:/usr/local/cuda$ ls -ltr
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
dhankar@dhankar-1:/usr/local/cuda$ 

```
#
####### Thus confirmed that the -- /usr/local/cuda -- points to -- /usr/local/cuda-11.0 , having CUDA version == CUDA Version 11.0.207
#
####### Testing the CUDNN install by running - mnistCUDNN

```
(base) dhankar@dhankar-1:~/opencv_cuda/cudNN_installers$ cd /usr/src/
(base) dhankar@dhankar-1:/usr/src$ ls -ltr
total 28
...output truncated...

drwxr-xr-x  8 root root 4096 Jul 25 16:56 nvidia-450.51.05
drwxr-xr-x  6 root root 4096 Jul 26 14:01 cudnn_samples_v8

(base) dhankar@dhankar-1:/usr/src$ cd cudnn_samples_v8/
(base) dhankar@dhankar-1:/usr/src/cudnn_samples_v8$ ls -ltr
total 20
-rw-r--r-- 1 root root  892 Jun  9 09:17 samples_common.mk
drwxr-xr-x 2 root root 4096 Jul 26 14:01 RNN
drwxr-xr-x 2 root root 4096 Jul 26 14:01 conv_sample
drwxr-xr-x 2 root root 4096 Jul 26 14:01 multiHeadAttention
drwxr-xr-x 4 root root 4096 Jul 26 14:01 mnistCUDNN
(base) dhankar@dhankar-1:/usr/src/cudnn_samples_v8$ 

```
# 
###### Create own Writable Path - own DIR in HOME DIR == /home/dhankar/opencv_cuda/cudnn_tests
Copy the - cudnn_samples_v8 - to the New DIR and run the tests. 
```
#cp -r /usr/src/cudnn_samples_v8/ $HOME
cp -r /usr/src/cudnn_samples_v8/ /home/dhankar/opencv_cuda/cudnn_tests
```
#
```
(base) dhankar@dhankar-1:/usr/src$ 
(base) dhankar@dhankar-1:/usr/src$ cd cudnn_samples_v8/
(base) dhankar@dhankar-1:/usr/src/cudnn_samples_v8$ ls -ltr
total 20
-rw-r--r-- 1 root root  892 Jun  9 09:17 samples_common.mk
drwxr-xr-x 2 root root 4096 Jul 26 14:01 RNN
drwxr-xr-x 2 root root 4096 Jul 26 14:01 conv_sample
drwxr-xr-x 2 root root 4096 Jul 26 14:01 multiHeadAttention
drwxr-xr-x 4 root root 4096 Jul 26 14:01 mnistCUDNN

(base) dhankar@dhankar-1:/usr/src/cudnn_samples_v8$ cp -r /usr/src/cudnn_samples_v8/ /home/dhankar/opencv_cuda/cudnn_tests
(base) dhankar@dhankar-1:/usr/src/cudnn_samples_v8$ cd /home/dhankar/opencv_cuda/cudnn_tests
(base) dhankar@dhankar-1:~/opencv_cuda/cudnn_tests$ ls -ltr
total 4
drwxr-xr-x 6 dhankar dhankar 4096 Jul 26 14:12 cudnn_samples_v8
(base) dhankar@dhankar-1:~/opencv_cuda/cudnn_tests$ 
(base) dhankar@dhankar-1:~/opencv_cuda/cudnn_tests$ cd cudnn_samples_v8/
(base) dhankar@dhankar-1:~/opencv_cuda/cudnn_tests/cudnn_samples_v8$ cd mnistCUDNN/
(base) dhankar@dhankar-1:~/opencv_cuda/cudnn_tests/cudnn_samples_v8/mnistCUDNN$ ls -ltr
total 96
drwxr-xr-x 4 dhankar dhankar  4096 Jul 26 14:12 FreeImage
-rw-r--r-- 1 dhankar dhankar  1287 Jul 26 14:12 readme.txt
-rw-r--r-- 1 dhankar dhankar 37208 Jul 26 14:12 mnistCUDNN.cpp
-rw-r--r-- 1 dhankar dhankar  7062 Jul 26 14:12 Makefile
-rw-r--r-- 1 dhankar dhankar  3488 Jul 26 14:12 gemv.h
-rw-r--r-- 1 dhankar dhankar  5484 Jul 26 14:12 fp16_emu.h
-rw-r--r-- 1 dhankar dhankar  5019 Jul 26 14:12 fp16_emu.cpp
-rw-r--r-- 1 dhankar dhankar   588 Jul 26 14:12 fp16_dev.h
-rw-r--r-- 1 dhankar dhankar  1299 Jul 26 14:12 fp16_dev.cu
-rw-r--r-- 1 dhankar dhankar  7384 Jul 26 14:12 error_util.h
drwxr-xr-x 2 dhankar dhankar  4096 Jul 26 14:12 data


(base) dhankar@dhankar-1:~/opencv_cuda/cudnn_tests/cudnn_samples_v8/mnistCUDNN$ make clean && make
rm -rf *o
rm -rf mnistCUDNN
Linking agains cublasLt = true
CUDA VERSION: 11000
TARGET ARCH: x86_64
HOST_ARCH: x86_64
TARGET OS: linux
SMS: 35 50 53 60 61 62 70 72 75 80
/usr/local/cuda/bin/nvcc -ccbin g++ -I/usr/local/cuda/include -I/usr/local/cuda/targets/ppc64le-linux/include -IFreeImage/include  -m64    -gencode arch=compute_35,code=sm_35 -gencode arch=compute_50,code=sm_50 -gencode arch=compute_53,code=sm_53 -gencode arch=compute_60,code=sm_60 -gencode arch=compute_61,code=sm_61 -gencode arch=compute_62,code=sm_62 -gencode arch=compute_70,code=sm_70 -gencode arch=compute_72,code=sm_72 -gencode arch=compute_75,code=sm_75 -gencode arch=compute_80,code=sm_80 -gencode arch=compute_80,code=compute_80 -o fp16_dev.o -c fp16_dev.cu
nvcc warning : The 'compute_35', 'compute_37', 'compute_50', 'sm_35', 'sm_37' and 'sm_50' architectures are deprecated, and may be removed in a future release (Use -Wno-deprecated-gpu-targets to suppress warning).
g++ -I/usr/local/cuda/include -I/usr/local/cuda/targets/ppc64le-linux/include -IFreeImage/include   -o fp16_emu.o -c fp16_emu.cpp
g++ -I/usr/local/cuda/include -I/usr/local/cuda/targets/ppc64le-linux/include -IFreeImage/include   -o mnistCUDNN.o -c mnistCUDNN.cpp
/usr/local/cuda/bin/nvcc -ccbin g++   -m64      -gencode arch=compute_35,code=sm_35 -gencode arch=compute_50,code=sm_50 -gencode arch=compute_53,code=sm_53 -gencode arch=compute_60,code=sm_60 -gencode arch=compute_61,code=sm_61 -gencode arch=compute_62,code=sm_62 -gencode arch=compute_70,code=sm_70 -gencode arch=compute_72,code=sm_72 -gencode arch=compute_75,code=sm_75 -gencode arch=compute_80,code=sm_80 -gencode arch=compute_80,code=compute_80 -o mnistCUDNN fp16_dev.o fp16_emu.o mnistCUDNN.o -I/usr/local/cuda/include -I/usr/local/cuda/targets/ppc64le-linux/include -IFreeImage/include -L/usr/local/cuda/lib64 -L/usr/local/cuda/targets/ppc64le-linux/lib -lcublasLt -LFreeImage/lib/linux/x86_64 -LFreeImage/lib/linux -lcudart -lcublas -lcudnn -lfreeimage -lstdc++ -lm
nvcc warning : The 'compute_35', 'compute_37', 'compute_50', 'sm_35', 'sm_37' and 'sm_50' architectures are deprecated, and may be removed in a future release (Use -Wno-deprecated-gpu-targets to suppress warning).


(base) dhankar@dhankar-1:~/opencv_cuda/cudnn_tests/cudnn_samples_v8/mnistCUDNN$ ls -ltr
total 3132
drwxr-xr-x 4 dhankar dhankar    4096 Jul 26 14:12 FreeImage
-rw-r--r-- 1 dhankar dhankar    1287 Jul 26 14:12 readme.txt
-rw-r--r-- 1 dhankar dhankar   37208 Jul 26 14:12 mnistCUDNN.cpp
-rw-r--r-- 1 dhankar dhankar    7062 Jul 26 14:12 Makefile
-rw-r--r-- 1 dhankar dhankar    3488 Jul 26 14:12 gemv.h
-rw-r--r-- 1 dhankar dhankar    5484 Jul 26 14:12 fp16_emu.h
-rw-r--r-- 1 dhankar dhankar    5019 Jul 26 14:12 fp16_emu.cpp
-rw-r--r-- 1 dhankar dhankar     588 Jul 26 14:12 fp16_dev.h
-rw-r--r-- 1 dhankar dhankar    1299 Jul 26 14:12 fp16_dev.cu
-rw-r--r-- 1 dhankar dhankar    7384 Jul 26 14:12 error_util.h
drwxr-xr-x 2 dhankar dhankar    4096 Jul 26 14:12 data
-rw-r--r-- 1 dhankar dhankar   59576 Jul 26 14:13 fp16_dev.o
-rw-r--r-- 1 dhankar dhankar    9080 Jul 26 14:13 fp16_emu.o
-rw-r--r-- 1 dhankar dhankar  245032 Jul 26 14:13 mnistCUDNN.o
-rwxr-xr-x 1 dhankar dhankar 2785864 Jul 26 14:13 mnistCUDNN
(base) dhankar@dhankar-1:~/opencv_cuda/cudnn_tests/cudnn_samples_v8/mnistCUDNN$ 

```
#

```
#./mnistCUDNN


(base) dhankar@dhankar-1:~/opencv_cuda/cudnn_tests/cudnn_samples_v8/mnistCUDNN$ ./mnistCUDNN
Executing: mnistCUDNN
cudnnGetVersion() : 8001 , CUDNN_VERSION from cudnn.h : 8001 (8.0.1)
Host compiler version : GCC 7.5.0

There are 1 CUDA capable devices on your machine :
device 0 : sms 14  Capabilities 7.5, SmClock 1710.0 Mhz, MemSize (Mb) 3910, MemClock 4001.0 Mhz, Ecc=0, boardGroupID=0
Using device 0

Testing single precision
Loading binary file data/conv1.bin
Loading binary file data/conv1.bias.bin
Loading binary file data/conv2.bin
Loading binary file data/conv2.bias.bin
Loading binary file data/ip1.bin
Loading binary file data/ip1.bias.bin
Loading binary file data/ip2.bin
Loading binary file data/ip2.bias.bin
Loading image data/one_28x28.pgm
Performing forward propagation ...
Testing cudnnGetConvolutionForwardAlgorithm_v7 ...
^^^^ CUDNN_STATUS_SUCCESS for Algo 1: -1.000000 time requiring 0 memory
^^^^ CUDNN_STATUS_SUCCESS for Algo 0: -1.000000 time requiring 0 memory
^^^^ CUDNN_STATUS_SUCCESS for Algo 2: -1.000000 time requiring 0 memory
^^^^ CUDNN_STATUS_SUCCESS for Algo 4: -1.000000 time requiring 184784 memory
^^^^ CUDNN_STATUS_SUCCESS for Algo 7: -1.000000 time requiring 2057744 memory
^^^^ CUDNN_STATUS_SUCCESS for Algo 5: -1.000000 time requiring 178432 memory
^^^^ CUDNN_STATUS_NOT_SUPPORTED for Algo 6: -1.000000 time requiring 0 memory
^^^^ CUDNN_STATUS_NOT_SUPPORTED for Algo 3: -1.000000 time requiring 0 memory
Testing cudnnFindConvolutionForwardAlgorithm ...
^^^^ CUDNN_STATUS_SUCCESS for Algo 2: 0.019680 time requiring 0 memory
^^^^ CUDNN_STATUS_SUCCESS for Algo 1: 0.023360 time requiring 0 memory
^^^^ CUDNN_STATUS_SUCCESS for Algo 0: 0.024576 time requiring 0 memory
^^^^ CUDNN_STATUS_SUCCESS for Algo 5: 0.222016 time requiring 178432 memory
^^^^ CUDNN_STATUS_SUCCESS for Algo 7: 0.261664 time requiring 2057744 memory
^^^^ CUDNN_STATUS_SUCCESS for Algo 4: 52.081951 time requiring 184784 memory
^^^^ CUDNN_STATUS_NOT_SUPPORTED for Algo 6: -1.000000 time requiring 0 memory
^^^^ CUDNN_STATUS_NOT_SUPPORTED for Algo 3: -1.000000 time requiring 0 memory
Testing cudnnGetConvolutionForwardAlgorithm_v7 ...
^^^^ CUDNN_STATUS_SUCCESS for Algo 1: -1.000000 time requiring 0 memory
^^^^ CUDNN_STATUS_SUCCESS for Algo 0: -1.000000 time requiring 0 memory
^^^^ CUDNN_STATUS_SUCCESS for Algo 7: -1.000000 time requiring 1433120 memory
^^^^ CUDNN_STATUS_SUCCESS for Algo 2: -1.000000 time requiring 128000 memory
^^^^ CUDNN_STATUS_SUCCESS for Algo 4: -1.000000 time requiring 2450080 memory
^^^^ CUDNN_STATUS_SUCCESS for Algo 5: -1.000000 time requiring 4656640 memory
^^^^ CUDNN_STATUS_NOT_SUPPORTED for Algo 6: -1.000000 time requiring 0 memory
^^^^ CUDNN_STATUS_NOT_SUPPORTED for Algo 3: -1.000000 time requiring 0 memory
Testing cudnnFindConvolutionForwardAlgorithm ...
^^^^ CUDNN_STATUS_SUCCESS for Algo 0: 0.065568 time requiring 0 memory
^^^^ CUDNN_STATUS_SUCCESS for Algo 2: 0.111712 time requiring 128000 memory
^^^^ CUDNN_STATUS_SUCCESS for Algo 1: 0.153216 time requiring 0 memory
^^^^ CUDNN_STATUS_SUCCESS for Algo 5: 0.207200 time requiring 4656640 memory
^^^^ CUDNN_STATUS_SUCCESS for Algo 7: 8.467040 time requiring 1433120 memory
^^^^ CUDNN_STATUS_SUCCESS for Algo 4: 20.297184 time requiring 2450080 memory
^^^^ CUDNN_STATUS_NOT_SUPPORTED for Algo 6: -1.000000 time requiring 0 memory
^^^^ CUDNN_STATUS_NOT_SUPPORTED for Algo 3: -1.000000 time requiring 0 memory
Resulting weights from Softmax:
0.0000000 0.9999399 0.0000000 0.0000000 0.0000561 0.0000000 0.0000012 0.0000017 0.0000010 0.0000000 
Loading image data/three_28x28.pgm
Performing forward propagation ...
Testing cudnnGetConvolutionForwardAlgorithm_v7 ...
^^^^ CUDNN_STATUS_SUCCESS for Algo 1: -1.000000 time requiring 0 memory
^^^^ CUDNN_STATUS_SUCCESS for Algo 0: -1.000000 time requiring 0 memory
^^^^ CUDNN_STATUS_SUCCESS for Algo 2: -1.000000 time requiring 0 memory
^^^^ CUDNN_STATUS_SUCCESS for Algo 4: -1.000000 time requiring 184784 memory
^^^^ CUDNN_STATUS_SUCCESS for Algo 7: -1.000000 time requiring 2057744 memory
^^^^ CUDNN_STATUS_SUCCESS for Algo 5: -1.000000 time requiring 178432 memory
^^^^ CUDNN_STATUS_NOT_SUPPORTED for Algo 6: -1.000000 time requiring 0 memory
^^^^ CUDNN_STATUS_NOT_SUPPORTED for Algo 3: -1.000000 time requiring 0 memory
Testing cudnnFindConvolutionForwardAlgorithm ...
^^^^ CUDNN_STATUS_SUCCESS for Algo 2: 0.032608 time requiring 0 memory
^^^^ CUDNN_STATUS_SUCCESS for Algo 1: 0.037024 time requiring 0 memory
^^^^ CUDNN_STATUS_SUCCESS for Algo 0: 0.040064 time requiring 0 memory
^^^^ CUDNN_STATUS_SUCCESS for Algo 7: 0.169536 time requiring 2057744 memory
^^^^ CUDNN_STATUS_SUCCESS for Algo 4: 0.178176 time requiring 184784 memory
^^^^ CUDNN_STATUS_SUCCESS for Algo 5: 0.238080 time requiring 178432 memory
^^^^ CUDNN_STATUS_NOT_SUPPORTED for Algo 6: -1.000000 time requiring 0 memory
^^^^ CUDNN_STATUS_NOT_SUPPORTED for Algo 3: -1.000000 time requiring 0 memory
Testing cudnnGetConvolutionForwardAlgorithm_v7 ...
^^^^ CUDNN_STATUS_SUCCESS for Algo 1: -1.000000 time requiring 0 memory
^^^^ CUDNN_STATUS_SUCCESS for Algo 0: -1.000000 time requiring 0 memory
^^^^ CUDNN_STATUS_SUCCESS for Algo 7: -1.000000 time requiring 1433120 memory
^^^^ CUDNN_STATUS_SUCCESS for Algo 2: -1.000000 time requiring 128000 memory
^^^^ CUDNN_STATUS_SUCCESS for Algo 4: -1.000000 time requiring 2450080 memory
^^^^ CUDNN_STATUS_SUCCESS for Algo 5: -1.000000 time requiring 4656640 memory
^^^^ CUDNN_STATUS_NOT_SUPPORTED for Algo 6: -1.000000 time requiring 0 memory
^^^^ CUDNN_STATUS_NOT_SUPPORTED for Algo 3: -1.000000 time requiring 0 memory
Testing cudnnFindConvolutionForwardAlgorithm ...
^^^^ CUDNN_STATUS_SUCCESS for Algo 0: 0.076320 time requiring 0 memory
^^^^ CUDNN_STATUS_SUCCESS for Algo 2: 0.097888 time requiring 128000 memory
^^^^ CUDNN_STATUS_SUCCESS for Algo 1: 0.161792 time requiring 0 memory
^^^^ CUDNN_STATUS_SUCCESS for Algo 4: 0.168448 time requiring 2450080 memory
^^^^ CUDNN_STATUS_SUCCESS for Algo 7: 0.173536 time requiring 1433120 memory
^^^^ CUDNN_STATUS_SUCCESS for Algo 5: 0.214688 time requiring 4656640 memory
^^^^ CUDNN_STATUS_NOT_SUPPORTED for Algo 6: -1.000000 time requiring 0 memory
^^^^ CUDNN_STATUS_NOT_SUPPORTED for Algo 3: -1.000000 time requiring 0 memory
Resulting weights from Softmax:
0.0000000 0.0000000 0.0000000 0.9999288 0.0000000 0.0000711 0.0000000 0.0000000 0.0000000 0.0000000 
Loading image data/five_28x28.pgm
Performing forward propagation ...
Resulting weights from Softmax:
0.0000000 0.0000008 0.0000000 0.0000002 0.0000000 0.9999820 0.0000154 0.0000000 0.0000012 0.0000006 

Result of classification: 1 3 5

Test passed!

Testing half precision (math in single precision)
Loading binary file data/conv1.bin
Loading binary file data/conv1.bias.bin
Loading binary file data/conv2.bin
Loading binary file data/conv2.bias.bin
Loading binary file data/ip1.bin
Loading binary file data/ip1.bias.bin
Loading binary file data/ip2.bin
Loading binary file data/ip2.bias.bin
Loading image data/one_28x28.pgm
Performing forward propagation ...
Testing cudnnGetConvolutionForwardAlgorithm_v7 ...
^^^^ CUDNN_STATUS_SUCCESS for Algo 1: -1.000000 time requiring 0 memory
^^^^ CUDNN_STATUS_SUCCESS for Algo 0: -1.000000 time requiring 0 memory
^^^^ CUDNN_STATUS_SUCCESS for Algo 2: -1.000000 time requiring 0 memory
^^^^ CUDNN_STATUS_SUCCESS for Algo 4: -1.000000 time requiring 184784 memory
^^^^ CUDNN_STATUS_SUCCESS for Algo 7: -1.000000 time requiring 2057744 memory
^^^^ CUDNN_STATUS_SUCCESS for Algo 5: -1.000000 time requiring 178432 memory
^^^^ CUDNN_STATUS_NOT_SUPPORTED for Algo 6: -1.000000 time requiring 0 memory
^^^^ CUDNN_STATUS_NOT_SUPPORTED for Algo 3: -1.000000 time requiring 0 memory
Testing cudnnFindConvolutionForwardAlgorithm ...
^^^^ CUDNN_STATUS_SUCCESS for Algo 2: 0.018336 time requiring 0 memory
^^^^ CUDNN_STATUS_SUCCESS for Algo 0: 0.020768 time requiring 0 memory
^^^^ CUDNN_STATUS_SUCCESS for Algo 1: 0.021184 time requiring 0 memory
^^^^ CUDNN_STATUS_SUCCESS for Algo 4: 0.090624 time requiring 184784 memory
^^^^ CUDNN_STATUS_SUCCESS for Algo 5: 0.098272 time requiring 178432 memory
^^^^ CUDNN_STATUS_SUCCESS for Algo 7: 0.109504 time requiring 2057744 memory
^^^^ CUDNN_STATUS_NOT_SUPPORTED for Algo 6: -1.000000 time requiring 0 memory
^^^^ CUDNN_STATUS_NOT_SUPPORTED for Algo 3: -1.000000 time requiring 0 memory
Testing cudnnGetConvolutionForwardAlgorithm_v7 ...
^^^^ CUDNN_STATUS_SUCCESS for Algo 7: -1.000000 time requiring 1433120 memory
^^^^ CUDNN_STATUS_SUCCESS for Algo 1: -1.000000 time requiring 0 memory
^^^^ CUDNN_STATUS_SUCCESS for Algo 0: -1.000000 time requiring 0 memory
^^^^ CUDNN_STATUS_SUCCESS for Algo 2: -1.000000 time requiring 64000 memory
^^^^ CUDNN_STATUS_SUCCESS for Algo 4: -1.000000 time requiring 2450080 memory
^^^^ CUDNN_STATUS_SUCCESS for Algo 5: -1.000000 time requiring 4656640 memory
^^^^ CUDNN_STATUS_NOT_SUPPORTED for Algo 6: -1.000000 time requiring 0 memory
^^^^ CUDNN_STATUS_NOT_SUPPORTED for Algo 3: -1.000000 time requiring 0 memory
Testing cudnnFindConvolutionForwardAlgorithm ...
^^^^ CUDNN_STATUS_SUCCESS for Algo 0: 0.040960 time requiring 0 memory
^^^^ CUDNN_STATUS_SUCCESS for Algo 2: 0.112096 time requiring 64000 memory
^^^^ CUDNN_STATUS_SUCCESS for Algo 4: 0.179200 time requiring 2450080 memory
^^^^ CUDNN_STATUS_SUCCESS for Algo 7: 0.202528 time requiring 1433120 memory
^^^^ CUDNN_STATUS_SUCCESS for Algo 5: 0.239200 time requiring 4656640 memory
^^^^ CUDNN_STATUS_SUCCESS for Algo 1: 0.635296 time requiring 0 memory
^^^^ CUDNN_STATUS_NOT_SUPPORTED for Algo 6: -1.000000 time requiring 0 memory
^^^^ CUDNN_STATUS_NOT_SUPPORTED for Algo 3: -1.000000 time requiring 0 memory
Resulting weights from Softmax:
0.0000001 1.0000000 0.0000001 0.0000000 0.0000563 0.0000001 0.0000012 0.0000017 0.0000010 0.0000001 
Loading image data/three_28x28.pgm
Performing forward propagation ...
Testing cudnnGetConvolutionForwardAlgorithm_v7 ...
^^^^ CUDNN_STATUS_SUCCESS for Algo 1: -1.000000 time requiring 0 memory
^^^^ CUDNN_STATUS_SUCCESS for Algo 0: -1.000000 time requiring 0 memory
^^^^ CUDNN_STATUS_SUCCESS for Algo 2: -1.000000 time requiring 0 memory
^^^^ CUDNN_STATUS_SUCCESS for Algo 4: -1.000000 time requiring 184784 memory
^^^^ CUDNN_STATUS_SUCCESS for Algo 7: -1.000000 time requiring 2057744 memory
^^^^ CUDNN_STATUS_SUCCESS for Algo 5: -1.000000 time requiring 178432 memory
^^^^ CUDNN_STATUS_NOT_SUPPORTED for Algo 6: -1.000000 time requiring 0 memory
^^^^ CUDNN_STATUS_NOT_SUPPORTED for Algo 3: -1.000000 time requiring 0 memory
Testing cudnnFindConvolutionForwardAlgorithm ...
^^^^ CUDNN_STATUS_SUCCESS for Algo 2: 0.037824 time requiring 0 memory
^^^^ CUDNN_STATUS_SUCCESS for Algo 0: 0.038848 time requiring 0 memory
^^^^ CUDNN_STATUS_SUCCESS for Algo 4: 0.139104 time requiring 184784 memory
^^^^ CUDNN_STATUS_SUCCESS for Algo 5: 0.141760 time requiring 178432 memory
^^^^ CUDNN_STATUS_SUCCESS for Algo 7: 0.186624 time requiring 2057744 memory
^^^^ CUDNN_STATUS_SUCCESS for Algo 1: 0.247104 time requiring 0 memory
^^^^ CUDNN_STATUS_NOT_SUPPORTED for Algo 6: -1.000000 time requiring 0 memory
^^^^ CUDNN_STATUS_NOT_SUPPORTED for Algo 3: -1.000000 time requiring 0 memory
Testing cudnnGetConvolutionForwardAlgorithm_v7 ...
^^^^ CUDNN_STATUS_SUCCESS for Algo 7: -1.000000 time requiring 1433120 memory
^^^^ CUDNN_STATUS_SUCCESS for Algo 1: -1.000000 time requiring 0 memory
^^^^ CUDNN_STATUS_SUCCESS for Algo 0: -1.000000 time requiring 0 memory
^^^^ CUDNN_STATUS_SUCCESS for Algo 2: -1.000000 time requiring 64000 memory
^^^^ CUDNN_STATUS_SUCCESS for Algo 4: -1.000000 time requiring 2450080 memory
^^^^ CUDNN_STATUS_SUCCESS for Algo 5: -1.000000 time requiring 4656640 memory
^^^^ CUDNN_STATUS_NOT_SUPPORTED for Algo 6: -1.000000 time requiring 0 memory
^^^^ CUDNN_STATUS_NOT_SUPPORTED for Algo 3: -1.000000 time requiring 0 memory
Testing cudnnFindConvolutionForwardAlgorithm ...
^^^^ CUDNN_STATUS_SUCCESS for Algo 0: 0.071680 time requiring 0 memory
^^^^ CUDNN_STATUS_SUCCESS for Algo 2: 0.102528 time requiring 64000 memory
^^^^ CUDNN_STATUS_SUCCESS for Algo 4: 0.166720 time requiring 2450080 memory
^^^^ CUDNN_STATUS_SUCCESS for Algo 7: 0.183744 time requiring 1433120 memory
^^^^ CUDNN_STATUS_SUCCESS for Algo 5: 0.217440 time requiring 4656640 memory
^^^^ CUDNN_STATUS_SUCCESS for Algo 1: 0.653376 time requiring 0 memory
^^^^ CUDNN_STATUS_NOT_SUPPORTED for Algo 6: -1.000000 time requiring 0 memory
^^^^ CUDNN_STATUS_NOT_SUPPORTED for Algo 3: -1.000000 time requiring 0 memory
Resulting weights from Softmax:
0.0000000 0.0000000 0.0000000 1.0000000 0.0000000 0.0000714 0.0000000 0.0000000 0.0000000 0.0000000 
Loading image data/five_28x28.pgm
Performing forward propagation ...
Resulting weights from Softmax:
0.0000000 0.0000008 0.0000000 0.0000002 0.0000000 1.0000000 0.0000154 0.0000000 0.0000012 0.0000006 

Result of classification: 1 3 5

Test passed!
(base) dhankar@dhankar-1:~/opencv_cuda/cudnn_tests/cudnn_samples_v8/mnistCUDNN$ 

```
#



