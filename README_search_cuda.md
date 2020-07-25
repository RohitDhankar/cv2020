#### While Compiling OpenCv with CUDA - getting to see multiple CUDA installs > Confusion . 
#
CMAKE Build process the terminal output states == -- CUDA detected: 9.1
#
##### As suggested here on SO -- Searching for CUDA version.txt fails -- https://stackoverflow.com/a/42122965/4928635 
```
(base) dhankar@dhankar-1:~/_dc_all/cv20/cv2020$ which nvcc
/usr/bin/nvcc
(base) dhankar@dhankar-1:~/_dc_all/cv20/cv2020$ cat /usr/local/cuda/version.txt
cat: /usr/local/cuda/version.txt: No such file or directory
```
#
```
(base) dhankar@dhankar-1:/usr/local$ ls -ltr cuda*
ls: cannot access 'cuda*': No such file or directory
(base) dhankar@dhankar-1:/usr/local$ 

```
#
##### The dates seen below - Dec  2  2017- are NOT my CUDA install dates - i bought this PC in 2019.
```
(base) dhankar@dhankar-1:/usr/bin$ ls -ltr cuda*
-rwxr-xr-x 1 root root  286872 Dec  2  2017 cuda-memcheck
-rwxr-xr-x 1 root root  577848 Dec  2  2017 cuda-gdbserver
-rwxr-xr-x 1 root root 8878568 Dec  2  2017 cuda-gdb
-rwxr-xr-x 1 root root 4139256 Dec  2  2017 cudafe++
-rwxr-xr-x 1 root root 4555144 Dec  2  2017 cudafe
(base) dhankar@dhankar-1:/usr/bin$ 

```
#
##### 

```
(base) dhankar@dhankar-1:/usr/bin$ dpkg -l | grep cuda
ii  libcudart9.1:amd64                         9.1.85-3ubuntu1                                  amd64        NVIDIA CUDA Runtime Library
ii  libcudnn7                                  7.6.4.38-1+cuda10.1                              amd64        cuDNN runtime libraries
ii  nvidia-cuda-dev                            9.1.85-3ubuntu1                                  amd64        NVIDIA CUDA development files
ii  nvidia-cuda-doc                            9.1.85-3ubuntu1                                  all          NVIDIA CUDA and OpenCL documentation
ii  nvidia-cuda-gdb                            9.1.85-3ubuntu1                                  amd64        NVIDIA CUDA Debugger (GDB)
ii  nvidia-cuda-toolkit                        9.1.85-3ubuntu1                                  amd64        NVIDIA CUDA development toolkit
(base) dhankar@dhankar-1:/usr/bin$ 

```
#

##### Searching for CUDA package installs within the - dpkg log files 

#
```
(base) dhankar@dhankar-1:/var/log$ ls -ltr dpkg*
-rw-r--r-- 1 root root 126019 Jan  9  2020 dpkg.log.7.gz
-rw-r--r-- 1 root root  22318 Feb  7 12:44 dpkg.log.6.gz
-rw-r--r-- 1 root root  27125 Feb 27 10:35 dpkg.log.5.gz
-rw-r--r-- 1 root root   9958 Apr  1 09:26 dpkg.log.4.gz
-rw-r--r-- 1 root root   8307 May  1 12:52 dpkg.log.3.gz
-rw-r--r-- 1 root root  15690 May 30 21:54 dpkg.log.2.gz
-rw-r--r-- 1 root root 234531 Jun 29 17:58 dpkg.log.1
-rw-r--r-- 1 root root 496486 Jul 24 19:03 dpkg.log
(base) dhankar@dhankar-1:/var/log$ 

```
#
```
grep installed dpkg.log.1 > ~/log_packs1.txt
grep installed dpkg.log.2.gz > ~/log_packs2_May2020.txt

```

##### Seen below these are the Log extracts related to CUDA 
#
```
2020-05-04 18:35:20 install libcudart9.1:amd64 <none> 9.1.85-3ubuntu1
2020-05-04 18:35:20 status half-installed libcudart9.1:amd64 9.1.85-3ubuntu1
#
2020-05-04 18:36:17 install nvidia-cuda-dev:amd64 <none> 9.1.85-3ubuntu1
2020-05-04 18:36:17 status half-installed nvidia-cuda-dev:amd64 9.1.85-3ubuntu1
2020-05-04 18:36:39 install nvidia-cuda-doc:all <none> 9.1.85-3ubuntu1
2020-05-04 18:36:39 status half-installed nvidia-cuda-doc:all 9.1.85-3ubuntu1
2020-05-04 18:36:44 install nvidia-cuda-gdb:amd64 <none> 9.1.85-3ubuntu1
2020-05-04 18:36:44 status half-installed nvidia-cuda-gdb:amd64 9.1.85-3ubuntu1
#
2020-05-04 18:36:47 install nvidia-cuda-toolkit:amd64 <none> 9.1.85-3ubuntu1
2020-05-04 18:36:47 status half-installed nvidia-cuda-toolkit:amd64 9.1.85-3ubuntu1
#
2020-05-04 18:36:57 status installed nvidia-cuda-doc:all 9.1.85-3ubuntu1
2020-05-04 18:36:59 status installed nvidia-cuda-gdb:amd64 9.1.85-3ubuntu1
2020-05-04 18:37:02 status installed libcudart9.1:amd64 9.1.85-3ubuntu1
#


```
#
