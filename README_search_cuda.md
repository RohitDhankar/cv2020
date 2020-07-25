
##### NVIDIA Drivers and CUDA updated - latest sys specifications as seen below
#

```
(base) dhankar@dhankar-1:~/_dc_all/cv20/cv2020$ nvidia-smi
Sat Jul 25 17:22:23 2020       
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 450.51.05    Driver Version: 450.51.05    CUDA Version: 11.0     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                               |                      |               MIG M. |
|===============================+======================+======================|
|   0  GeForce GTX 1650    On   | 00000000:01:00.0  On |                  N/A |
|  0%   45C    P8     4W /  75W |    216MiB /  3910MiB |      1%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+
                                                                               
+-----------------------------------------------------------------------------+
| Processes:                                                                  |
|  GPU   GI   CI        PID   Type   Process name                  GPU Memory |
|        ID   ID                                                   Usage      |
|=============================================================================|
|    0   N/A  N/A      1741      G   /usr/lib/xorg/Xorg                 14MiB |
|    0   N/A  N/A      2142      G   /usr/bin/gnome-shell               49MiB |
|    0   N/A  N/A      3868      G   /usr/lib/xorg/Xorg                 86MiB |
|    0   N/A  N/A      4001      G   /usr/bin/gnome-shell               62MiB |
+-----------------------------------------------------------------------------+

```
#

Earlier for the OpenCV - CMAKE Build process , the terminal output stated == -- CUDA detected: 9.1
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

###### UPDATED_NVIDIA

#

```
(base) dhankar@dhankar-1:~/_dc_all/cv20/cv2020$ nvidia-smi
Sat Jul 25 16:07:42 2020       
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 440.100      Driver Version: 440.100      CUDA Version: 10.2     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|===============================+======================+======================|
|   0  GeForce GTX 1650    Off  | 00000000:01:00.0  On |                  N/A |
|  0%   48C    P8     5W /  75W |    309MiB /  3910MiB |      2%      Default |
+-------------------------------+----------------------+----------------------+
                                                                               
+-----------------------------------------------------------------------------+
| Processes:                                                       GPU Memory |
|  GPU       PID   Type   Process name                             Usage      |
|=============================================================================|
|    0      2050      G   /usr/lib/xorg/Xorg                            14MiB |
|    0      2150      G   /usr/bin/gnome-shell                          48MiB |
|    0      3509      G   /usr/lib/xorg/Xorg                           156MiB |
|    0      3740      G   /usr/bin/gnome-shell                          83MiB |
|    0     10712      G   /usr/lib/firefox/firefox                       2MiB |
+-----------------------------------------------------------------------------+
(base) dhankar@dhankar-1:~/_dc_all/cv20/cv2020$ 
(base) dhankar@dhankar-1:~/_dc_all/cv20/cv2020$ which nvcc
/usr/bin/nvcc
(base) dhankar@dhankar-1:~/_dc_all/cv20/cv2020$ cat /usr/local/cuda/version.txt
cat: /usr/local/cuda/version.txt: No such file or directory
(base) dhankar@dhankar-1:~/_dc_all/cv20/cv2020$ cd /usr/bin/
(base) dhankar@dhankar-1:/usr/bin$ ls -ltr nvcc*
-rwxr-xr-x 1 root root 59 Mar 12  2018 nvcc
(base) dhankar@dhankar-1:/usr/bin$ ls -ltr cuda*
-rwxr-xr-x 1 root root  286872 Dec  2  2017 cuda-memcheck
-rwxr-xr-x 1 root root  577848 Dec  2  2017 cuda-gdbserver
-rwxr-xr-x 1 root root 8878568 Dec  2  2017 cuda-gdb
-rwxr-xr-x 1 root root 4139256 Dec  2  2017 cudafe++
-rwxr-xr-x 1 root root 4555144 Dec  2  2017 cudafe
(base) dhankar@dhankar-1:/usr/bin$ dpkg -l | grep cuda
ii  libcudart9.1:amd64                         9.1.85-3ubuntu1                                  amd64        NVIDIA CUDA Runtime Library
ii  libcudnn7                                  7.6.4.38-1+cuda10.1                              amd64        cuDNN runtime libraries
ii  nvidia-cuda-dev                            9.1.85-3ubuntu1                                  amd64        NVIDIA CUDA development files
ii  nvidia-cuda-doc                            9.1.85-3ubuntu1                                  all          NVIDIA CUDA and OpenCL documentation
ii  nvidia-cuda-gdb                            9.1.85-3ubuntu1                                  amd64        NVIDIA CUDA Debugger (GDB)
ii  nvidia-cuda-toolkit                        9.1.85-3ubuntu1                                  amd64        NVIDIA CUDA development toolkit
(base) dhankar@dhankar-1:/usr/bin$ 
```
###### Following official NVIDIA site -- 

- https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html

```
(base) dhankar@dhankar-1:/usr/bin$ gcc --version
gcc (Ubuntu 7.5.0-3ubuntu1~18.04) 7.5.0
Copyright (C) 2017 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

(base) dhankar@dhankar-1:/usr/bin$ lspci | grep -i nvidia
01:00.0 VGA compatible controller: NVIDIA Corporation Device 1f82 (rev a1)
01:00.1 Audio device: NVIDIA Corporation Device 10fa (rev a1)


(base) dhankar@dhankar-1:/usr/bin$ uname -r
5.4.0-42-generic


(base) dhankar@dhankar-1:/usr/bin$ sudo apt-get install linux-headers-5.4.0-42-generic
[sudo] password for dhankar: 
Reading package lists... Done
Building dependency tree       
Reading state information... Done
linux-headers-5.4.0-42-generic is already the newest version (5.4.0-42.46~18.04.1).
linux-headers-5.4.0-42-generic set to manually installed.
(base) dhankar@dhankar-1:/usr/bin$ 

```
#
```
(base) dhankar@dhankar-1:/usr/bin$ 
(base) dhankar@dhankar-1:/usr/bin$ workon 
opencv_cuda
(base) dhankar@dhankar-1:/usr/bin$ 
(base) dhankar@dhankar-1:/usr/bin$ workon opencv_cuda
(opencv_cuda) (base) dhankar@dhankar-1:/usr/bin$ 
(opencv_cuda) (base) dhankar@dhankar-1:/usr/bin$ conda deactivate
(opencv_cuda) dhankar@dhankar-1:/usr/bin$ 
(opencv_cuda) dhankar@dhankar-1:/usr/bin$ 

```
#

```
(base) dhankar@dhankar-1:/usr/bin$ 
(base) dhankar@dhankar-1:/usr/bin$ workon 
opencv_cuda
(base) dhankar@dhankar-1:/usr/bin$ 
(base) dhankar@dhankar-1:/usr/bin$ workon opencv_cuda
(opencv_cuda) (base) dhankar@dhankar-1:/usr/bin$ 
(opencv_cuda) (base) dhankar@dhankar-1:/usr/bin$ conda deactivate
(opencv_cuda) dhankar@dhankar-1:/usr/bin$ 
(opencv_cuda) dhankar@dhankar-1:/usr/bin$ cd ~
(opencv_cuda) dhankar@dhankar-1:~$ wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/cuda-ubuntu1804.pin
--2020-07-25 16:49:00--  https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/cuda-ubuntu1804.pin
Resolving developer.download.nvidia.com (developer.download.nvidia.com)... 152.199.39.144
Connecting to developer.download.nvidia.com (developer.download.nvidia.com)|152.199.39.144|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 190 [application/octet-stream]
Saving to: ‘cuda-ubuntu1804.pin’

cuda-ubuntu1804.pin                 100%[=================================================================>]     190  --.-KB/s    in 0s      

2020-07-25 16:49:01 (10.2 MB/s) - ‘cuda-ubuntu1804.pin’ saved [190/190]

(opencv_cuda) dhankar@dhankar-1:~$ 
(opencv_cuda) dhankar@dhankar-1:~$ sudo mv cuda-ubuntu1804.pin /etc/apt/preferences.d/cuda-repository-pin-600
[sudo] password for dhankar: 
(opencv_cuda) dhankar@dhankar-1:~$ wget http://developer.download.nvidia.com/compute/cuda/11.0.2/local_installers/cuda-repo-ubuntu1804-11-0-local_11.0.2-450.51.05-1_amd64.deb
--2020-07-25 16:49:59--  http://developer.download.nvidia.com/compute/cuda/11.0.2/local_installers/cuda-repo-ubuntu1804-11-0-local_11.0.2-450.51.05-1_amd64.deb
Resolving developer.download.nvidia.com (developer.download.nvidia.com)... 152.199.39.144
Connecting to developer.download.nvidia.com (developer.download.nvidia.com)|152.199.39.144|:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 2273753684 (2.1G) [application/x-deb]
Saving to: ‘cuda-repo-ubuntu1804-11-0-local_11.0.2-450.51.05-1_amd64.deb’

cuda-repo-ubuntu1804-11-0-local_11. 100%[=================================================================>]   2.12G  26.4MB/s    in 82s     

2020-07-25 16:51:21 (26.5 MB/s) - ‘cuda-repo-ubuntu1804-11-0-local_11.0.2-450.51.05-1_amd64.deb’ saved [2273753684/2273753684]

(opencv_cuda) dhankar@dhankar-1:~$ 
(opencv_cuda) dhankar@dhankar-1:~$ sudo dpkg -i cuda-repo-ubuntu1804-11-0-local_11.0.2-450.51.05-1_amd64.deb
Selecting previously unselected package cuda-repo-ubuntu1804-11-0-local.
(Reading database ... 301564 files and directories currently installed.)
Preparing to unpack cuda-repo-ubuntu1804-11-0-local_11.0.2-450.51.05-1_amd64.deb ...
Unpacking cuda-repo-ubuntu1804-11-0-local (11.0.2-450.51.05-1) ...
Setting up cuda-repo-ubuntu1804-11-0-local (11.0.2-450.51.05-1) ...

The public CUDA GPG key does not appear to be installed.
To install the key, run this command:
sudo apt-key add /var/cuda-repo-ubuntu1804-11-0-local/7fa2af80.pub

(opencv_cuda) dhankar@dhankar-1:~$ sudo apt-key add /var/cuda-repo-ubuntu1804-11-0-local/7fa2af80.pub
OK
(opencv_cuda) dhankar@dhankar-1:~$ 
(opencv_cuda) dhankar@dhankar-1:~$ sudo apt-get update
Get:1 file:/var/cuda-repo-ubuntu1804-11-0-local  InRelease
Ign:1 file:/var/cuda-repo-ubuntu1804-11-0-local  InRelease
Get:2 file:/var/cuda-repo-ubuntu1804-11-0-local  Release [564 B]
Get:2 file:/var/cuda-repo-ubuntu1804-11-0-local  Release [564 B]
Get:3 file:/var/cuda-repo-ubuntu1804-11-0-local  Release.gpg [836 B]
Get:3 file:/var/cuda-repo-ubuntu1804-11-0-local  Release.gpg [836 B]
Get:4 file:/var/cuda-repo-ubuntu1804-11-0-local  Packages [23.9 kB]                                     
Get:5 http://security.ubuntu.com/ubuntu bionic-security InRelease [88.7 kB]                         
Get:6 http://security.ubuntu.com/ubuntu bionic-security/main amd64 DEP-11 Metadata [46.0 kB]               
Get:7 http://security.ubuntu.com/ubuntu bionic-security/universe amd64 DEP-11 Metadata [49.2 kB]                              
Get:8 http://security.ubuntu.com/ubuntu bionic-security/multiverse amd64 DEP-11 Metadata [2,464 B]                             
Hit:9 http://packages.microsoft.com/repos/vscode stable InRelease                                                                    
Hit:10 https://repo.skype.com/deb stable InRelease                                                    
Hit:11 https://download.docker.com/linux/ubuntu bionic InRelease                                      
Hit:12 http://packages.ros.org/ros/ubuntu bionic InRelease                                                                                   
Hit:13 http://dl.google.com/linux/chrome/deb stable InRelease                                                                                
Hit:14 https://packagecloud.io/slacktechnologies/slack/debian jessie InRelease                                                               
Hit:15 http://ppa.launchpad.net/apandada1/brightness-controller/ubuntu bionic InRelease                                                      
Hit:16 http://ppa.launchpad.net/cybermax-dexter/sdl2-backport/ubuntu bionic InRelease                                                        
Hit:17 http://ppa.launchpad.net/kxstudio-debian/libs/ubuntu bionic InRelease                                                                 
Hit:18 http://ppa.launchpad.net/kxstudio-debian/music/ubuntu bionic InRelease                                                                
Hit:19 http://ppa.launchpad.net/kxstudio-debian/plugins/ubuntu bionic InRelease                                                              
Hit:20 http://ppa.launchpad.net/kxstudio-debian/apps/ubuntu bionic InRelease                                                                 
Hit:21 http://ppa.launchpad.net/kxstudio-debian/kxstudio/ubuntu bionic InRelease                                                             
Hit:22 http://ppa.launchpad.net/mixxx/mixxx/ubuntu bionic InRelease                                                                          
Hit:23 http://ppa.launchpad.net/ubuntugis/ubuntugis-unstable/ubuntu bionic InRelease                                                         
Hit:24 http://in.archive.ubuntu.com/ubuntu bionic InRelease                                                                                  
Get:25 http://in.archive.ubuntu.com/ubuntu bionic-updates InRelease [88.7 kB]                                                                
Get:26 http://in.archive.ubuntu.com/ubuntu bionic-backports InRelease [74.6 kB]                                                              
Get:27 http://in.archive.ubuntu.com/ubuntu bionic-updates/main i386 Packages [719 kB]                                                        
Get:28 http://in.archive.ubuntu.com/ubuntu bionic-updates/main amd64 Packages [1,023 kB]                                                     
Get:29 http://in.archive.ubuntu.com/ubuntu bionic-updates/main amd64 DEP-11 Metadata [295 kB]                                                
Get:30 http://in.archive.ubuntu.com/ubuntu bionic-updates/universe amd64 Packages [1,094 kB]                                                 
Get:31 http://in.archive.ubuntu.com/ubuntu bionic-updates/universe i386 Packages [1,026 kB]                                                  
Get:32 http://in.archive.ubuntu.com/ubuntu bionic-updates/universe amd64 DEP-11 Metadata [279 kB]                                            
Get:33 http://in.archive.ubuntu.com/ubuntu bionic-updates/multiverse amd64 DEP-11 Metadata [2,464 B]                                         
Get:34 http://in.archive.ubuntu.com/ubuntu bionic-backports/universe amd64 DEP-11 Metadata [9,288 B]                                         
Hit:35 https://qgis.org/ubuntugis bionic InRelease                                                                                           
Hit:36 https://qgis.org/ubuntu bionic InRelease                                                                                              
Hit:37 https://dl.winehq.org/wine-builds/ubuntu bionic InRelease                                      
Err:38 https://kx.studio/repo stable InRelease                                                                                               
  Could not connect to kx.studio:443 (95.216.41.244), connection timed out
Err:39 https://kx.studio/repo gcc5 InRelease
  Unable to connect to kx.studio:https:
Fetched 4,797 kB in 49s (97.0 kB/s)
Reading package lists... Done
W: Failed to fetch https://kx.studio/repo/dists/stable/InRelease  Could not connect to kx.studio:443 (95.216.41.244), connection timed out
W: Failed to fetch https://kx.studio/repo/dists/gcc5/InRelease  Unable to connect to kx.studio:https:
W: Some index files failed to download. They have been ignored, or old ones used instead.
(opencv_cuda) dhankar@dhankar-1:~$ 
(opencv_cuda) dhankar@dhankar-1:~$ sudo apt-get -y install cuda
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following additional packages will be installed:
  cuda-11-0 cuda-command-line-tools-11-0 cuda-compiler-11-0 cuda-cudart-11-0 cuda-cudart-dev-11-0 cuda-cuobjdump-11-0 cuda-cupti-11-0
  cuda-cupti-dev-11-0 cuda-demo-suite-11-0 cuda-documentation-11-0 cuda-driver-dev-11-0 cuda-drivers cuda-drivers-450 cuda-gdb-11-0
  cuda-libraries-11-0 cuda-libraries-dev-11-0 cuda-memcheck-11-0 cuda-nsight-11-0 cuda-nsight-compute-11-0 cuda-nsight-systems-11-0
  cuda-nvcc-11-0 cuda-nvdisasm-11-0 cuda-nvml-dev-11-0 cuda-nvprof-11-0 cuda-nvprune-11-0 cuda-nvrtc-11-0 cuda-nvrtc-dev-11-0 cuda-nvtx-11-0
  cuda-nvvp-11-0 cuda-runtime-11-0 cuda-samples-11-0 cuda-sanitizer-11-0 cuda-toolkit-11-0 cuda-tools-11-0 cuda-visual-tools-11-0
  default-jre default-jre-headless freeglut3 freeglut3-dev libcublas-11-0 libcublas-dev-11-0 libcufft-11-0 libcufft-dev-11-0 libcurand-11-0
  libcurand-dev-11-0 libcusolver-11-0 libcusolver-dev-11-0 libcusparse-11-0 libcusparse-dev-11-0 libnpp-11-0 libnpp-dev-11-0
  libnvidia-cfg1-450 libnvidia-common-450 libnvidia-compute-450 libnvidia-decode-450 libnvidia-encode-450 libnvidia-extra-450
  libnvidia-fbc1-450 libnvidia-gl-450 libnvidia-ifr1-450 libnvjpeg-11-0 libnvjpeg-dev-11-0 nsight-compute-2020.1.1 nsight-systems-2020.3.2
  nvidia-compute-utils-450 nvidia-dkms-450 nvidia-driver-450 nvidia-kernel-common-450 nvidia-kernel-source-450 nvidia-modprobe
  nvidia-settings nvidia-utils-450 openjdk-11-jre openjdk-11-jre-headless xserver-xorg-video-nvidia-450
Suggested packages:
  fonts-ipafont-gothic fonts-ipafont-mincho fonts-wqy-microhei | fonts-wqy-zenhei
Recommended packages:
  libnvidia-compute-450:i386 libnvidia-decode-450:i386 libnvidia-encode-450:i386 libnvidia-ifr1-450:i386 libnvidia-fbc1-450:i386
  libnvidia-gl-450:i386
The following packages will be REMOVED:
  libnvidia-cfg1-440 libnvidia-compute-440 libnvidia-compute-440:i386 libnvidia-decode-440 libnvidia-decode-440:i386 libnvidia-encode-440
  libnvidia-encode-440:i386 libnvidia-extra-440 libnvidia-fbc1-440 libnvidia-fbc1-440:i386 libnvidia-gl-440 libnvidia-gl-440:i386
  libnvidia-ifr1-440 libnvidia-ifr1-440:i386 nvidia-compute-utils-440 nvidia-dkms-440 nvidia-driver-440 nvidia-kernel-common-440
  nvidia-kernel-source-440 nvidia-utils-440 xserver-xorg-video-nvidia-440
The following NEW packages will be installed:
  cuda cuda-11-0 cuda-command-line-tools-11-0 cuda-compiler-11-0 cuda-cudart-11-0 cuda-cudart-dev-11-0 cuda-cuobjdump-11-0 cuda-cupti-11-0
  cuda-cupti-dev-11-0 cuda-demo-suite-11-0 cuda-documentation-11-0 cuda-driver-dev-11-0 cuda-drivers cuda-drivers-450 cuda-gdb-11-0
  cuda-libraries-11-0 cuda-libraries-dev-11-0 cuda-memcheck-11-0 cuda-nsight-11-0 cuda-nsight-compute-11-0 cuda-nsight-systems-11-0
  cuda-nvcc-11-0 cuda-nvdisasm-11-0 cuda-nvml-dev-11-0 cuda-nvprof-11-0 cuda-nvprune-11-0 cuda-nvrtc-11-0 cuda-nvrtc-dev-11-0 cuda-nvtx-11-0
  cuda-nvvp-11-0 cuda-runtime-11-0 cuda-samples-11-0 cuda-sanitizer-11-0 cuda-toolkit-11-0 cuda-tools-11-0 cuda-visual-tools-11-0
  default-jre default-jre-headless freeglut3 freeglut3-dev libcublas-11-0 libcublas-dev-11-0 libcufft-11-0 libcufft-dev-11-0 libcurand-11-0
  libcurand-dev-11-0 libcusolver-11-0 libcusolver-dev-11-0 libcusparse-11-0 libcusparse-dev-11-0 libnpp-11-0 libnpp-dev-11-0
  libnvidia-cfg1-450 libnvidia-common-450 libnvidia-compute-450 libnvidia-decode-450 libnvidia-encode-450 libnvidia-extra-450
  libnvidia-fbc1-450 libnvidia-gl-450 libnvidia-ifr1-450 libnvjpeg-11-0 libnvjpeg-dev-11-0 nsight-compute-2020.1.1 nsight-systems-2020.3.2
  nvidia-compute-utils-450 nvidia-dkms-450 nvidia-driver-450 nvidia-kernel-common-450 nvidia-kernel-source-450 nvidia-modprobe
  nvidia-utils-450 openjdk-11-jre openjdk-11-jre-headless xserver-xorg-video-nvidia-450
The following packages will be upgraded:
  nvidia-settings
1 upgraded, 75 newly installed, 21 to remove and 22 not upgraded.
Need to get 37.8 MB/2,272 MB of archives.
After this operation, 4,728 MB of additional disk space will be used.




Get:1 http://in.archive.ubuntu.com/ubuntu bionic-updates/main amd64 openjdk-11-jre-headless amd64 11.0.8+10-0ubuntu1~18.04.1 [37.6 MB]
Get:2 file:/var/cuda-repo-ubuntu1804-11-0-local  libnvidia-compute-450 450.51.05-0ubuntu1 [21.8 MB]
Get:3 file:/var/cuda-repo-ubuntu1804-11-0-local  cuda-cudart-11-0 11.0.194-1 [129 kB]
Get:4 file:/var/cuda-repo-ubuntu1804-11-0-local  cuda-nvrtc-11-0 11.0.194-1 [6,521 kB]
Get:5 file:/var/cuda-repo-ubuntu1804-11-0-local  libcublas-11-0 11.1.0.229-1 [118 MB]
Get:6 http://in.archive.ubuntu.com/ubuntu bionic-updates/main amd64 default-jre-headless amd64 2:1.11-68ubuntu1~18.04.1 [10.9 kB]
Get:7 http://in.archive.ubuntu.com/ubuntu bionic-updates/main amd64 openjdk-11-jre amd64 11.0.8+10-0ubuntu1~18.04.1 [34.4 kB]
Get:8 http://in.archive.ubuntu.com/ubuntu bionic-updates/main amd64 default-jre amd64 2:1.11-68ubuntu1~18.04.1 [1,076 B]
Get:9 http://in.archive.ubuntu.com/ubuntu bionic/universe amd64 freeglut3 amd64 2.8.1-3 [73.6 kB]
Get:10 http://in.archive.ubuntu.com/ubuntu bionic/universe amd64 freeglut3-dev amd64 2.8.1-3 [124 kB]
Get:11 file:/var/cuda-repo-ubuntu1804-11-0-local  libcufft-11-0 10.2.0.218-1 [94.1 MB]
Get:12 file:/var/cuda-repo-ubuntu1804-11-0-local  libcurand-11-0 10.2.1.218-1 [39.2 MB]
Get:13 file:/var/cuda-repo-ubuntu1804-11-0-local  libcusolver-11-0 10.5.0.218-1 [277 MB]
Get:14 file:/var/cuda-repo-ubuntu1804-11-0-local  libcusparse-11-0 11.1.0.218-1 [71.2 MB]
Get:15 file:/var/cuda-repo-ubuntu1804-11-0-local  libnpp-11-0 11.1.0.218-1 [56.6 MB]
Get:16 file:/var/cuda-repo-ubuntu1804-11-0-local  libnvjpeg-11-0 11.1.0.218-1 [1,391 kB]                                                     
Get:17 file:/var/cuda-repo-ubuntu1804-11-0-local  cuda-libraries-11-0 11.0.2-1 [2,490 B]                                                     
Get:18 file:/var/cuda-repo-ubuntu1804-11-0-local  libnvidia-common-450 450.51.05-0ubuntu1 [10.0 kB]                                          
Get:19 file:/var/cuda-repo-ubuntu1804-11-0-local  libnvidia-decode-450 450.51.05-0ubuntu1 [1,103 kB]                                         
Get:20 file:/var/cuda-repo-ubuntu1804-11-0-local  libnvidia-encode-450 450.51.05-0ubuntu1 [39.4 kB]                                          
Get:21 file:/var/cuda-repo-ubuntu1804-11-0-local  libnvidia-fbc1-450 450.51.05-0ubuntu1 [49.7 kB]                                            
Get:22 file:/var/cuda-repo-ubuntu1804-11-0-local  libnvidia-gl-450 450.51.05-0ubuntu1 [60.4 MB]                                              
Get:23 file:/var/cuda-repo-ubuntu1804-11-0-local  libnvidia-ifr1-450 450.51.05-0ubuntu1 [68.5 kB]                                            
Get:24 file:/var/cuda-repo-ubuntu1804-11-0-local  nvidia-compute-utils-450 450.51.05-0ubuntu1 [123 kB]                                       
Get:25 file:/var/cuda-repo-ubuntu1804-11-0-local  nvidia-kernel-source-450 450.51.05-0ubuntu1 [11.8 MB]                                      
Get:26 file:/var/cuda-repo-ubuntu1804-11-0-local  nvidia-kernel-common-450 450.51.05-0ubuntu1 [9,818 B]                                      
Get:27 file:/var/cuda-repo-ubuntu1804-11-0-local  nvidia-dkms-450 450.51.05-0ubuntu1 [26.7 kB]                                               
Get:28 file:/var/cuda-repo-ubuntu1804-11-0-local  libnvidia-extra-450 450.51.05-0ubuntu1 [39.5 kB]                                           
Get:29 file:/var/cuda-repo-ubuntu1804-11-0-local  nvidia-utils-450 450.51.05-0ubuntu1 [366 kB]                                               
Get:30 file:/var/cuda-repo-ubuntu1804-11-0-local  libnvidia-cfg1-450 450.51.05-0ubuntu1 [75.0 kB]                                            
Get:31 file:/var/cuda-repo-ubuntu1804-11-0-local  xserver-xorg-video-nvidia-450 450.51.05-0ubuntu1 [1,536 kB]                                
Get:32 file:/var/cuda-repo-ubuntu1804-11-0-local  nvidia-driver-450 450.51.05-0ubuntu1 [419 kB]                                              
Get:33 file:/var/cuda-repo-ubuntu1804-11-0-local  nvidia-modprobe 450.51.05-0ubuntu1 [19.7 kB]                                               
Get:34 file:/var/cuda-repo-ubuntu1804-11-0-local  nvidia-settings 450.51.05-0ubuntu1 [920 kB]                                                
Get:35 file:/var/cuda-repo-ubuntu1804-11-0-local  cuda-drivers-450 450.51.05-1 [2,628 B]                                                     
Get:36 file:/var/cuda-repo-ubuntu1804-11-0-local  cuda-drivers 450.51.05-1 [2,504 B]                                                         
Get:37 file:/var/cuda-repo-ubuntu1804-11-0-local  cuda-runtime-11-0 11.0.2-1 [2,424 B]                                                       
Get:38 file:/var/cuda-repo-ubuntu1804-11-0-local  cuda-cuobjdump-11-0 11.0.194-1 [103 kB]                                                    
Get:39 file:/var/cuda-repo-ubuntu1804-11-0-local  cuda-driver-dev-11-0 11.0.194-1 [25.0 kB]                                                  
Get:40 file:/var/cuda-repo-ubuntu1804-11-0-local  cuda-cudart-dev-11-0 11.0.194-1 [1,662 kB]                                                 
Get:41 file:/var/cuda-repo-ubuntu1804-11-0-local  cuda-nvcc-11-0 11.0.194-1 [21.1 MB]                                                        
Get:42 file:/var/cuda-repo-ubuntu1804-11-0-local  cuda-nvprune-11-0 11.0.167-1 [53.1 kB]                                                     
Get:43 file:/var/cuda-repo-ubuntu1804-11-0-local  cuda-compiler-11-0 11.0.2-1 [2,416 B]                                                      
Get:44 file:/var/cuda-repo-ubuntu1804-11-0-local  cuda-nvrtc-dev-11-0 11.0.194-1 [22.1 kB]                                                   
Get:45 file:/var/cuda-repo-ubuntu1804-11-0-local  libcublas-dev-11-0 11.1.0.229-1 [120 MB]                                                   
Get:46 file:/var/cuda-repo-ubuntu1804-11-0-local  libcufft-dev-11-0 10.2.0.218-1 [172 MB]                                                    
Get:47 file:/var/cuda-repo-ubuntu1804-11-0-local  libcurand-dev-11-0 10.2.1.218-1 [39.2 MB]                                                  
Get:48 file:/var/cuda-repo-ubuntu1804-11-0-local  libcusolver-dev-11-0 10.5.0.218-1 [17.6 MB]                                                
Get:49 file:/var/cuda-repo-ubuntu1804-11-0-local  libcusparse-dev-11-0 11.1.0.218-1 [71.4 MB]                                                
Get:50 file:/var/cuda-repo-ubuntu1804-11-0-local  libnpp-dev-11-0 11.1.0.218-1 [57.4 MB]                                                     
Get:51 file:/var/cuda-repo-ubuntu1804-11-0-local  libnvjpeg-dev-11-0 11.1.0.218-1 [1,321 kB]                                                 
Get:52 file:/var/cuda-repo-ubuntu1804-11-0-local  cuda-libraries-dev-11-0 11.0.2-1 [2,514 B]                                                 
Get:53 file:/var/cuda-repo-ubuntu1804-11-0-local  cuda-cupti-11-0 11.0.194-1 [10.5 MB]                                                       
Get:54 file:/var/cuda-repo-ubuntu1804-11-0-local  cuda-cupti-dev-11-0 11.0.194-1 [2,276 kB]                                                  
Get:55 file:/var/cuda-repo-ubuntu1804-11-0-local  cuda-nvdisasm-11-0 11.0.194-1 [27.3 MB]                                                    
Get:56 file:/var/cuda-repo-ubuntu1804-11-0-local  cuda-gdb-11-0 11.0.194-1 [3,891 kB]                                                        
Get:57 file:/var/cuda-repo-ubuntu1804-11-0-local  cuda-memcheck-11-0 11.0.194-1 [144 kB]                                                     
Get:58 file:/var/cuda-repo-ubuntu1804-11-0-local  cuda-nvprof-11-0 11.0.194-1 [1,911 kB]                                                     
Get:59 file:/var/cuda-repo-ubuntu1804-11-0-local  cuda-nvtx-11-0 11.0.167-1 [51.1 kB]                                                        
Get:60 file:/var/cuda-repo-ubuntu1804-11-0-local  cuda-sanitizer-11-0 11.0.194-1 [7,220 kB]                                                  
Get:61 file:/var/cuda-repo-ubuntu1804-11-0-local  cuda-command-line-tools-11-0 11.0.2-1 [2,474 B]                                            
Get:62 file:/var/cuda-repo-ubuntu1804-11-0-local  nsight-compute-2020.1.1 2020.1.1.8-1 [323 MB]                                              
Get:63 file:/var/cuda-repo-ubuntu1804-11-0-local  cuda-nsight-compute-11-0 11.0.2-1 [3,718 B]                                                
Get:64 file:/var/cuda-repo-ubuntu1804-11-0-local  nsight-systems-2020.3.2 2020.3.2.6-87e152c [227 MB]                                        
Get:65 file:/var/cuda-repo-ubuntu1804-11-0-local  cuda-nsight-systems-11-0 11.0.2-1 [3,280 B]                                                
Get:66 file:/var/cuda-repo-ubuntu1804-11-0-local  cuda-nsight-11-0 11.0.194-1 [119 MB]                                                       
Get:67 file:/var/cuda-repo-ubuntu1804-11-0-local  cuda-nvml-dev-11-0 11.0.167-1 [71.9 kB]                                                    
Get:68 file:/var/cuda-repo-ubuntu1804-11-0-local  cuda-nvvp-11-0 11.0.194-1 [115 MB]                                                         
Get:69 file:/var/cuda-repo-ubuntu1804-11-0-local  cuda-visual-tools-11-0 11.0.2-1 [2,942 B]                                                  
Get:70 file:/var/cuda-repo-ubuntu1804-11-0-local  cuda-tools-11-0 11.0.2-1 [2,380 B]                                                         
Get:71 file:/var/cuda-repo-ubuntu1804-11-0-local  cuda-samples-11-0 11.0.194-1 [68.1 MB]                                                     
Get:72 file:/var/cuda-repo-ubuntu1804-11-0-local  cuda-documentation-11-0 11.0.207-1 [59.6 MB]                                               
Get:73 file:/var/cuda-repo-ubuntu1804-11-0-local  cuda-toolkit-11-0 11.0.2-1 [2,728 B]                                                       
Get:74 file:/var/cuda-repo-ubuntu1804-11-0-local  cuda-demo-suite-11-0 11.0.167-1 [3,948 kB]                                                 
Get:75 file:/var/cuda-repo-ubuntu1804-11-0-local  cuda-11-0 11.0.2-1 [2,450 B]                                                               
Get:76 file:/var/cuda-repo-ubuntu1804-11-0-local  cuda 11.0.2-1 [2,392 B]                                                                    
Fetched 37.8 MB in 20s (1,935 kB/s)                                                                                                          
Extracting templates from packages: 100%
(Reading database ... 301650 files and directories currently installed.)


Removing nvidia-driver-440 (440.100-0ubuntu0.18.04.1) ...
Removing xserver-xorg-video-nvidia-440 (440.100-0ubuntu0.18.04.1) ...
Removing libnvidia-cfg1-440:amd64 (440.100-0ubuntu0.18.04.1) ...
Removing libnvidia-encode-440:i386 (440.100-0ubuntu0.18.04.1) ...
Removing libnvidia-decode-440:i386 (440.100-0ubuntu0.18.04.1) ...
Removing libnvidia-compute-440:i386 (440.100-0ubuntu0.18.04.1) ...
Removing libnvidia-encode-440:amd64 (440.100-0ubuntu0.18.04.1) ...
Removing libnvidia-decode-440:amd64 (440.100-0ubuntu0.18.04.1) ...
Removing nvidia-utils-440 (440.100-0ubuntu0.18.04.1) ...


dpkg: libnvidia-compute-440:amd64: dependency problems, but removing anyway as you requested:
 libnvidia-gl-440:amd64 depends on libnvidia-compute-440.
 nvidia-compute-utils-440 depends on libnvidia-compute-440.
 libcuinj64-9.1:amd64 depends on libcuda1 (>= 387.26) | libcuda-9.1-1; however:
  Package libcuda1 is not installed.
  Package libnvidia-compute-435:amd64 which provides libcuda1 is not installed.
  Package libnvidia-compute-440:amd64 which provides libcuda1 is to be removed.
  Package libcuda-9.1-1 is not installed.
  Package libnvidia-compute-435:amd64 which provides libcuda-9.1-1 is not installed.
  Package libnvidia-compute-440:amd64 which provides libcuda-9.1-1 is to be removed.
 libcuinj64-9.1:amd64 depends on libcuda1 (>= 387.26) | libcuda-9.1-1; however:
  Package libcuda1 is not installed.
  Package libnvidia-compute-435:amd64 which provides libcuda1 is not installed.
  Package libnvidia-compute-440:amd64 which provides libcuda1 is to be removed.
  Package libcuda-9.1-1 is not installed.
  Package libnvidia-compute-435:amd64 which provides libcuda-9.1-1 is not installed.
  Package libnvidia-compute-440:amd64 which provides libcuda-9.1-1 is to be removed.

Removing libnvidia-compute-440:amd64 (440.100-0ubuntu0.18.04.1) ...
Selecting previously unselected package libnvidia-compute-450:amd64.
(Reading database ... 301504 files and directories currently installed.)
Preparing to unpack .../libnvidia-compute-450_450.51.05-0ubuntu1_amd64.deb ...
Unpacking libnvidia-compute-450:amd64 (450.51.05-0ubuntu1) ...
(Reading database ... 301518 files and directories currently installed.)
Removing libnvidia-extra-440:amd64 (440.100-0ubuntu0.18.04.1) ...
Removing libnvidia-fbc1-440:i386 (440.100-0ubuntu0.18.04.1) ...
Removing libnvidia-fbc1-440:amd64 (440.100-0ubuntu0.18.04.1) ...
Removing libnvidia-ifr1-440:amd64 (440.100-0ubuntu0.18.04.1) ...
Removing libnvidia-gl-440:amd64 (440.100-0ubuntu0.18.04.1) ...
Removing libnvidia-ifr1-440:i386 (440.100-0ubuntu0.18.04.1) ...
Removing libnvidia-gl-440:i386 (440.100-0ubuntu0.18.04.1) ...
Removing nvidia-compute-utils-440 (440.100-0ubuntu0.18.04.1) ...
Removing nvidia-dkms-440 (440.100-0ubuntu0.18.04.1) ...
Removing all DKMS Modules
Done.
INFO:Disable nvidia

DEBUG:Parsing /usr/share/ubuntu-drivers-common/quirks/lenovo_thinkpad
DEBUG:Parsing /usr/share/ubuntu-drivers-common/quirks/put_your_quirks_here
DEBUG:Parsing /usr/share/ubuntu-drivers-common/quirks/dell_latitude

update-initramfs: deferring update (trigger activated)
Removing nvidia-kernel-common-440 (440.100-0ubuntu0.18.04.1) ...
update-initramfs: deferring update (trigger activated)
Removing nvidia-kernel-source-440 (440.100-0ubuntu0.18.04.1) ...


Selecting previously unselected package cuda-cudart-11-0.
(Reading database ... 301053 files and directories currently installed.)
Preparing to unpack .../00-cuda-cudart-11-0_11.0.194-1_amd64.deb ...
Unpacking cuda-cudart-11-0 (11.0.194-1) ...
Selecting previously unselected package cuda-nvrtc-11-0.
Preparing to unpack .../01-cuda-nvrtc-11-0_11.0.194-1_amd64.deb ...
Unpacking cuda-nvrtc-11-0 (11.0.194-1) ...
Selecting previously unselected package libcublas-11-0.
Preparing to unpack .../02-libcublas-11-0_11.1.0.229-1_amd64.deb ...
Unpacking libcublas-11-0 (11.1.0.229-1) ...
Selecting previously unselected package libcufft-11-0.
Preparing to unpack .../03-libcufft-11-0_10.2.0.218-1_amd64.deb ...
Unpacking libcufft-11-0 (10.2.0.218-1) ...
Selecting previously unselected package libcurand-11-0.
Preparing to unpack .../04-libcurand-11-0_10.2.1.218-1_amd64.deb ...
Unpacking libcurand-11-0 (10.2.1.218-1) ...
Selecting previously unselected package libcusolver-11-0.
Preparing to unpack .../05-libcusolver-11-0_10.5.0.218-1_amd64.deb ...
Unpacking libcusolver-11-0 (10.5.0.218-1) ...
Selecting previously unselected package libcusparse-11-0.
Preparing to unpack .../06-libcusparse-11-0_11.1.0.218-1_amd64.deb ...
Unpacking libcusparse-11-0 (11.1.0.218-1) ...
Selecting previously unselected package libnpp-11-0.
Preparing to unpack .../07-libnpp-11-0_11.1.0.218-1_amd64.deb ...
Unpacking libnpp-11-0 (11.1.0.218-1) ...
Selecting previously unselected package libnvjpeg-11-0.
Preparing to unpack .../08-libnvjpeg-11-0_11.1.0.218-1_amd64.deb ...
Unpacking libnvjpeg-11-0 (11.1.0.218-1) ...
Selecting previously unselected package cuda-libraries-11-0.
Preparing to unpack .../09-cuda-libraries-11-0_11.0.2-1_amd64.deb ...
Unpacking cuda-libraries-11-0 (11.0.2-1) ...
Selecting previously unselected package libnvidia-common-450.
Preparing to unpack .../10-libnvidia-common-450_450.51.05-0ubuntu1_all.deb ...
Unpacking libnvidia-common-450 (450.51.05-0ubuntu1) ...
Selecting previously unselected package libnvidia-decode-450:amd64.
Preparing to unpack .../11-libnvidia-decode-450_450.51.05-0ubuntu1_amd64.deb ...
Unpacking libnvidia-decode-450:amd64 (450.51.05-0ubuntu1) ...
Selecting previously unselected package libnvidia-encode-450:amd64.
Preparing to unpack .../12-libnvidia-encode-450_450.51.05-0ubuntu1_amd64.deb ...
Unpacking libnvidia-encode-450:amd64 (450.51.05-0ubuntu1) ...
Selecting previously unselected package libnvidia-fbc1-450:amd64.
Preparing to unpack .../13-libnvidia-fbc1-450_450.51.05-0ubuntu1_amd64.deb ...
Unpacking libnvidia-fbc1-450:amd64 (450.51.05-0ubuntu1) ...
Selecting previously unselected package libnvidia-gl-450:amd64.
Preparing to unpack .../14-libnvidia-gl-450_450.51.05-0ubuntu1_amd64.deb ...
Unpacking libnvidia-gl-450:amd64 (450.51.05-0ubuntu1) ...
Selecting previously unselected package libnvidia-ifr1-450:amd64.
Preparing to unpack .../15-libnvidia-ifr1-450_450.51.05-0ubuntu1_amd64.deb ...
Unpacking libnvidia-ifr1-450:amd64 (450.51.05-0ubuntu1) ...
Selecting previously unselected package nvidia-compute-utils-450.
Preparing to unpack .../16-nvidia-compute-utils-450_450.51.05-0ubuntu1_amd64.deb ...
Unpacking nvidia-compute-utils-450 (450.51.05-0ubuntu1) ...
Selecting previously unselected package nvidia-kernel-source-450.
Preparing to unpack .../17-nvidia-kernel-source-450_450.51.05-0ubuntu1_amd64.deb ...
Unpacking nvidia-kernel-source-450 (450.51.05-0ubuntu1) ...
Selecting previously unselected package nvidia-kernel-common-450.
Preparing to unpack .../18-nvidia-kernel-common-450_450.51.05-0ubuntu1_amd64.deb ...
Unpacking nvidia-kernel-common-450 (450.51.05-0ubuntu1) ...
Selecting previously unselected package nvidia-dkms-450.
Preparing to unpack .../19-nvidia-dkms-450_450.51.05-0ubuntu1_amd64.deb ...
Unpacking nvidia-dkms-450 (450.51.05-0ubuntu1) ...
Selecting previously unselected package libnvidia-extra-450:amd64.
Preparing to unpack .../20-libnvidia-extra-450_450.51.05-0ubuntu1_amd64.deb ...
Unpacking libnvidia-extra-450:amd64 (450.51.05-0ubuntu1) ...
Selecting previously unselected package nvidia-utils-450.
Preparing to unpack .../21-nvidia-utils-450_450.51.05-0ubuntu1_amd64.deb ...
Unpacking nvidia-utils-450 (450.51.05-0ubuntu1) ...
Selecting previously unselected package libnvidia-cfg1-450:amd64.
Preparing to unpack .../22-libnvidia-cfg1-450_450.51.05-0ubuntu1_amd64.deb ...
Unpacking libnvidia-cfg1-450:amd64 (450.51.05-0ubuntu1) ...
Selecting previously unselected package xserver-xorg-video-nvidia-450.
Preparing to unpack .../23-xserver-xorg-video-nvidia-450_450.51.05-0ubuntu1_amd64.deb ...
Unpacking xserver-xorg-video-nvidia-450 (450.51.05-0ubuntu1) ...
Selecting previously unselected package nvidia-driver-450.
Preparing to unpack .../24-nvidia-driver-450_450.51.05-0ubuntu1_amd64.deb ...
Unpacking nvidia-driver-450 (450.51.05-0ubuntu1) ...
Selecting previously unselected package nvidia-modprobe.
Preparing to unpack .../25-nvidia-modprobe_450.51.05-0ubuntu1_amd64.deb ...
Unpacking nvidia-modprobe (450.51.05-0ubuntu1) ...
Preparing to unpack .../26-nvidia-settings_450.51.05-0ubuntu1_amd64.deb ...
Unpacking nvidia-settings (450.51.05-0ubuntu1) over (440.44-0ubuntu0.18.04.1) ...
Selecting previously unselected package cuda-drivers-450.
Preparing to unpack .../27-cuda-drivers-450_450.51.05-1_amd64.deb ...
Unpacking cuda-drivers-450 (450.51.05-1) ...
Selecting previously unselected package cuda-drivers.
Preparing to unpack .../28-cuda-drivers_450.51.05-1_amd64.deb ...
Unpacking cuda-drivers (450.51.05-1) ...
Selecting previously unselected package cuda-runtime-11-0.
Preparing to unpack .../29-cuda-runtime-11-0_11.0.2-1_amd64.deb ...
Unpacking cuda-runtime-11-0 (11.0.2-1) ...
Selecting previously unselected package cuda-cuobjdump-11-0.
Preparing to unpack .../30-cuda-cuobjdump-11-0_11.0.194-1_amd64.deb ...
Unpacking cuda-cuobjdump-11-0 (11.0.194-1) ...
Selecting previously unselected package cuda-driver-dev-11-0.
Preparing to unpack .../31-cuda-driver-dev-11-0_11.0.194-1_amd64.deb ...
Unpacking cuda-driver-dev-11-0 (11.0.194-1) ...
Selecting previously unselected package cuda-cudart-dev-11-0.
Preparing to unpack .../32-cuda-cudart-dev-11-0_11.0.194-1_amd64.deb ...
Unpacking cuda-cudart-dev-11-0 (11.0.194-1) ...
Selecting previously unselected package cuda-nvcc-11-0.
Preparing to unpack .../33-cuda-nvcc-11-0_11.0.194-1_amd64.deb ...
Unpacking cuda-nvcc-11-0 (11.0.194-1) ...
Selecting previously unselected package cuda-nvprune-11-0.
Preparing to unpack .../34-cuda-nvprune-11-0_11.0.167-1_amd64.deb ...
Unpacking cuda-nvprune-11-0 (11.0.167-1) ...
Selecting previously unselected package cuda-compiler-11-0.
Preparing to unpack .../35-cuda-compiler-11-0_11.0.2-1_amd64.deb ...
Unpacking cuda-compiler-11-0 (11.0.2-1) ...
Selecting previously unselected package cuda-nvrtc-dev-11-0.
Preparing to unpack .../36-cuda-nvrtc-dev-11-0_11.0.194-1_amd64.deb ...
Unpacking cuda-nvrtc-dev-11-0 (11.0.194-1) ...
Selecting previously unselected package libcublas-dev-11-0.
Preparing to unpack .../37-libcublas-dev-11-0_11.1.0.229-1_amd64.deb ...
Unpacking libcublas-dev-11-0 (11.1.0.229-1) ...
Selecting previously unselected package libcufft-dev-11-0.
Preparing to unpack .../38-libcufft-dev-11-0_10.2.0.218-1_amd64.deb ...
Unpacking libcufft-dev-11-0 (10.2.0.218-1) ...
Selecting previously unselected package libcurand-dev-11-0.
Preparing to unpack .../39-libcurand-dev-11-0_10.2.1.218-1_amd64.deb ...
Unpacking libcurand-dev-11-0 (10.2.1.218-1) ...
Selecting previously unselected package libcusolver-dev-11-0.
Preparing to unpack .../40-libcusolver-dev-11-0_10.5.0.218-1_amd64.deb ...
Unpacking libcusolver-dev-11-0 (10.5.0.218-1) ...
Selecting previously unselected package libcusparse-dev-11-0.
Preparing to unpack .../41-libcusparse-dev-11-0_11.1.0.218-1_amd64.deb ...
Unpacking libcusparse-dev-11-0 (11.1.0.218-1) ...
Selecting previously unselected package libnpp-dev-11-0.
Preparing to unpack .../42-libnpp-dev-11-0_11.1.0.218-1_amd64.deb ...
Unpacking libnpp-dev-11-0 (11.1.0.218-1) ...
Selecting previously unselected package libnvjpeg-dev-11-0.
Preparing to unpack .../43-libnvjpeg-dev-11-0_11.1.0.218-1_amd64.deb ...
Unpacking libnvjpeg-dev-11-0 (11.1.0.218-1) ...
Selecting previously unselected package cuda-libraries-dev-11-0.
Preparing to unpack .../44-cuda-libraries-dev-11-0_11.0.2-1_amd64.deb ...
Unpacking cuda-libraries-dev-11-0 (11.0.2-1) ...
Selecting previously unselected package cuda-cupti-11-0.
Preparing to unpack .../45-cuda-cupti-11-0_11.0.194-1_amd64.deb ...
Unpacking cuda-cupti-11-0 (11.0.194-1) ...
Selecting previously unselected package cuda-cupti-dev-11-0.
Preparing to unpack .../46-cuda-cupti-dev-11-0_11.0.194-1_amd64.deb ...
Unpacking cuda-cupti-dev-11-0 (11.0.194-1) ...
Selecting previously unselected package cuda-nvdisasm-11-0.
Preparing to unpack .../47-cuda-nvdisasm-11-0_11.0.194-1_amd64.deb ...
Unpacking cuda-nvdisasm-11-0 (11.0.194-1) ...
Selecting previously unselected package cuda-gdb-11-0.
Preparing to unpack .../48-cuda-gdb-11-0_11.0.194-1_amd64.deb ...
Unpacking cuda-gdb-11-0 (11.0.194-1) ...
Selecting previously unselected package cuda-memcheck-11-0.
Preparing to unpack .../49-cuda-memcheck-11-0_11.0.194-1_amd64.deb ...
Unpacking cuda-memcheck-11-0 (11.0.194-1) ...
Selecting previously unselected package cuda-nvprof-11-0.
Preparing to unpack .../50-cuda-nvprof-11-0_11.0.194-1_amd64.deb ...
Unpacking cuda-nvprof-11-0 (11.0.194-1) ...
Selecting previously unselected package cuda-nvtx-11-0.
Preparing to unpack .../51-cuda-nvtx-11-0_11.0.167-1_amd64.deb ...
Unpacking cuda-nvtx-11-0 (11.0.167-1) ...
Selecting previously unselected package cuda-sanitizer-11-0.
Preparing to unpack .../52-cuda-sanitizer-11-0_11.0.194-1_amd64.deb ...
Unpacking cuda-sanitizer-11-0 (11.0.194-1) ...
Selecting previously unselected package cuda-command-line-tools-11-0.
Preparing to unpack .../53-cuda-command-line-tools-11-0_11.0.2-1_amd64.deb ...
Unpacking cuda-command-line-tools-11-0 (11.0.2-1) ...
Selecting previously unselected package nsight-compute-2020.1.1.
Preparing to unpack .../54-nsight-compute-2020.1.1_2020.1.1.8-1_amd64.deb ...
Unpacking nsight-compute-2020.1.1 (2020.1.1.8-1) ...
Selecting previously unselected package cuda-nsight-compute-11-0.
Preparing to unpack .../55-cuda-nsight-compute-11-0_11.0.2-1_amd64.deb ...
Unpacking cuda-nsight-compute-11-0 (11.0.2-1) ...
Selecting previously unselected package nsight-systems-2020.3.2.
Preparing to unpack .../56-nsight-systems-2020.3.2_2020.3.2.6-1_amd64.deb ...
Unpacking nsight-systems-2020.3.2 (2020.3.2.6-87e152c) ...
Selecting previously unselected package cuda-nsight-systems-11-0.
Preparing to unpack .../57-cuda-nsight-systems-11-0_11.0.2-1_amd64.deb ...
Unpacking cuda-nsight-systems-11-0 (11.0.2-1) ...
Selecting previously unselected package openjdk-11-jre-headless:amd64.
Preparing to unpack .../58-openjdk-11-jre-headless_11.0.8+10-0ubuntu1~18.04.1_amd64.deb ...
Unpacking openjdk-11-jre-headless:amd64 (11.0.8+10-0ubuntu1~18.04.1) ...
Selecting previously unselected package default-jre-headless.
Preparing to unpack .../59-default-jre-headless_2%3a1.11-68ubuntu1~18.04.1_amd64.deb ...
Unpacking default-jre-headless (2:1.11-68ubuntu1~18.04.1) ...
Selecting previously unselected package openjdk-11-jre:amd64.
Preparing to unpack .../60-openjdk-11-jre_11.0.8+10-0ubuntu1~18.04.1_amd64.deb ...
Unpacking openjdk-11-jre:amd64 (11.0.8+10-0ubuntu1~18.04.1) ...
Selecting previously unselected package default-jre.
Preparing to unpack .../61-default-jre_2%3a1.11-68ubuntu1~18.04.1_amd64.deb ...
Unpacking default-jre (2:1.11-68ubuntu1~18.04.1) ...
Selecting previously unselected package cuda-nsight-11-0.
Preparing to unpack .../62-cuda-nsight-11-0_11.0.194-1_amd64.deb ...
Unpacking cuda-nsight-11-0 (11.0.194-1) ...
Selecting previously unselected package cuda-nvml-dev-11-0.
Preparing to unpack .../63-cuda-nvml-dev-11-0_11.0.167-1_amd64.deb ...
Unpacking cuda-nvml-dev-11-0 (11.0.167-1) ...
Selecting previously unselected package cuda-nvvp-11-0.
Preparing to unpack .../64-cuda-nvvp-11-0_11.0.194-1_amd64.deb ...
Unpacking cuda-nvvp-11-0 (11.0.194-1) ...
Selecting previously unselected package cuda-visual-tools-11-0.
Preparing to unpack .../65-cuda-visual-tools-11-0_11.0.2-1_amd64.deb ...
Unpacking cuda-visual-tools-11-0 (11.0.2-1) ...
Selecting previously unselected package cuda-tools-11-0.
Preparing to unpack .../66-cuda-tools-11-0_11.0.2-1_amd64.deb ...
Unpacking cuda-tools-11-0 (11.0.2-1) ...
Selecting previously unselected package freeglut3:amd64.
Preparing to unpack .../67-freeglut3_2.8.1-3_amd64.deb ...
Unpacking freeglut3:amd64 (2.8.1-3) ...
Selecting previously unselected package freeglut3-dev:amd64.
Preparing to unpack .../68-freeglut3-dev_2.8.1-3_amd64.deb ...
Unpacking freeglut3-dev:amd64 (2.8.1-3) ...
Selecting previously unselected package cuda-samples-11-0.
Preparing to unpack .../69-cuda-samples-11-0_11.0.194-1_amd64.deb ...
Unpacking cuda-samples-11-0 (11.0.194-1) ...
Selecting previously unselected package cuda-documentation-11-0.
Preparing to unpack .../70-cuda-documentation-11-0_11.0.207-1_amd64.deb ...
Unpacking cuda-documentation-11-0 (11.0.207-1) ...
Selecting previously unselected package cuda-toolkit-11-0.
Preparing to unpack .../71-cuda-toolkit-11-0_11.0.2-1_amd64.deb ...
Unpacking cuda-toolkit-11-0 (11.0.2-1) ...
Selecting previously unselected package cuda-demo-suite-11-0.
Preparing to unpack .../72-cuda-demo-suite-11-0_11.0.167-1_amd64.deb ...
Unpacking cuda-demo-suite-11-0 (11.0.167-1) ...
Selecting previously unselected package cuda-11-0.
Preparing to unpack .../73-cuda-11-0_11.0.2-1_amd64.deb ...
Unpacking cuda-11-0 (11.0.2-1) ...
Selecting previously unselected package cuda.
Preparing to unpack .../74-cuda_11.0.2-1_amd64.deb ...
Unpacking cuda (11.0.2-1) ...



Setting up freeglut3:amd64 (2.8.1-3) ...
Setting up libnvidia-extra-450:amd64 (450.51.05-0ubuntu1) ...
Setting up nsight-systems-2020.3.2 (2020.3.2.6-87e152c) ...

update-alternatives: using /opt/nvidia/nsight-systems/2020.3.2/target-linux-x64/nsys to provide /usr/local/bin/nsys (nsys) in auto mode
update-alternatives: using /opt/nvidia/nsight-systems/2020.3.2/host-linux-x64/nsight-sys to provide /usr/local/bin/nsight-sys (nsight-sys) in auto mode
update-alternatives: using /opt/nvidia/nsight-systems/2020.3.2/host-linux-x64/nsys-ui to provide /usr/local/bin/nsys-ui (nsys-ui) in auto mode

Setting up libnvidia-compute-450:amd64 (450.51.05-0ubuntu1) ...
Setting up cuda-sanitizer-11-0 (11.0.194-1) ...
Setting up cuda-nsight-systems-11-0 (11.0.2-1) ...
Setting up cuda-memcheck-11-0 (11.0.194-1) ...
Setting up cuda-nvprune-11-0 (11.0.167-1) ...
Setting up openjdk-11-jre-headless:amd64 (11.0.8+10-0ubuntu1~18.04.1) ...
update-alternatives: using /usr/lib/jvm/java-11-openjdk-amd64/bin/rmid to provide /usr/bin/rmid (rmid) in auto mode
update-alternatives: using /usr/lib/jvm/java-11-openjdk-amd64/bin/java to provide /usr/bin/java (java) in auto mode
update-alternatives: using /usr/lib/jvm/java-11-openjdk-amd64/bin/keytool to provide /usr/bin/keytool (keytool) in auto mode
update-alternatives: using /usr/lib/jvm/java-11-openjdk-amd64/bin/jjs to provide /usr/bin/jjs (jjs) in auto mode
update-alternatives: using /usr/lib/jvm/java-11-openjdk-amd64/bin/pack200 to provide /usr/bin/pack200 (pack200) in auto mode
update-alternatives: using /usr/lib/jvm/java-11-openjdk-amd64/bin/rmiregistry to provide /usr/bin/rmiregistry (rmiregistry) in auto mode
update-alternatives: using /usr/lib/jvm/java-11-openjdk-amd64/bin/unpack200 to provide /usr/bin/unpack200 (unpack200) in auto mode
update-alternatives: using /usr/lib/jvm/java-11-openjdk-amd64/bin/jfr to provide /usr/bin/jfr (jfr) in auto mode
update-alternatives: using /usr/lib/jvm/java-11-openjdk-amd64/lib/jexec to provide /usr/bin/jexec (jexec) in auto mode
update-binfmts: warning: current package is openjdk-11, but binary format already installed by openjdk-8
Setting up libcufft-11-0 (10.2.0.218-1) ...
Setting up libnvidia-fbc1-450:amd64 (450.51.05-0ubuntu1) ...
Setting up libcusparse-11-0 (11.1.0.218-1) ...
Setting up libcublas-11-0 (11.1.0.229-1) ...
Setting up nvidia-utils-450 (450.51.05-0ubuntu1) ...
Setting up cuda-nvdisasm-11-0 (11.0.194-1) ...
Setting up nvidia-kernel-common-450 (450.51.05-0ubuntu1) ...
update-initramfs: deferring update (trigger activated)
Setting up libcusolver-11-0 (10.5.0.218-1) ...
Setting up nvidia-settings (450.51.05-0ubuntu1) ...
Setting up cuda-nvrtc-11-0 (11.0.194-1) ...
Setting up cuda-nvprof-11-0 (11.0.194-1) ...
Setting up libcusolver-dev-11-0 (10.5.0.218-1) ...
Setting up cuda-nvtx-11-0 (11.0.167-1) ...
Setting up libnpp-11-0 (11.1.0.218-1) ...
Setting up nvidia-modprobe (450.51.05-0ubuntu1) ...
Setting up nvidia-kernel-source-450 (450.51.05-0ubuntu1) ...
Setting up libcurand-11-0 (10.2.1.218-1) ...
Setting up libnvidia-cfg1-450:amd64 (450.51.05-0ubuntu1) ...
Setting up nvidia-dkms-450 (450.51.05-0ubuntu1) ...
update-initramfs: deferring update (trigger activated)

A modprobe blacklist file has been created at /etc/modprobe.d to prevent Nouveau
from loading. This can be reverted by deleting the following file:
/etc/modprobe.d/nvidia-graphics-drivers.conf

A new initrd image has also been created. To revert, please regenerate your
initrd by running the following command after deleting the modprobe.d file:
`/usr/sbin/initramfs -u`

*****************************************************************************
*** Reboot your computer and verify that the NVIDIA graphics driver can   ***
*** be loaded.                                                            ***
*****************************************************************************

INFO:Enable nvidia
DEBUG:Parsing /usr/share/ubuntu-drivers-common/quirks/lenovo_thinkpad
DEBUG:Parsing /usr/share/ubuntu-drivers-common/quirks/put_your_quirks_here
DEBUG:Parsing /usr/share/ubuntu-drivers-common/quirks/dell_latitude
Loading new nvidia-450.51.05 DKMS files...
Building for 5.4.0-42-generic
Building for architecture x86_64
Building initial module for 5.4.0-42-generic
Done.

nvidia:
Running module version sanity check.
 - Original module
   - No original module exists within this kernel
 - Installation
   - Installing to /lib/modules/5.4.0-42-generic/updates/dkms/

nvidia-modeset.ko:
Running module version sanity check.
 - Original module
   - No original module exists within this kernel
 - Installation
   - Installing to /lib/modules/5.4.0-42-generic/updates/dkms/

nvidia-drm.ko:
Running module version sanity check.
 - Original module
   - No original module exists within this kernel
 - Installation
   - Installing to /lib/modules/5.4.0-42-generic/updates/dkms/

nvidia-uvm.ko:
Running module version sanity check.
 - Original module
   - No original module exists within this kernel
 - Installation
   - Installing to /lib/modules/5.4.0-42-generic/updates/dkms/

depmod...

DKMS: install completed.
Setting up libcublas-dev-11-0 (11.1.0.229-1) ...
Setting up nvidia-compute-utils-450 (450.51.05-0ubuntu1) ...
Warning: The home dir /nonexistent you specified can't be accessed: No such file or directory
Adding system user `nvidia-persistenced' (UID 122) ...
Adding new group `nvidia-persistenced' (GID 127) ...
Adding new user `nvidia-persistenced' (UID 122) with group `nvidia-persistenced' ...
Not creating home directory `/nonexistent'.

Created symlink /etc/systemd/system/multi-user.target.wants/nvidia-persistenced.service → /lib/systemd/system/nvidia-persistenced.service.

Setting up cuda-cuobjdump-11-0 (11.0.194-1) ...
Setting up libcurand-dev-11-0 (10.2.1.218-1) ...
Setting up libnpp-dev-11-0 (11.1.0.218-1) ...
Setting up cuda-nvml-dev-11-0 (11.0.167-1) ...
Setting up libnvjpeg-11-0 (11.1.0.218-1) ...
Setting up libnvidia-common-450 (450.51.05-0ubuntu1) ...
Setting up freeglut3-dev:amd64 (2.8.1-3) ...
Setting up cuda-driver-dev-11-0 (11.0.194-1) ...
Setting up cuda-cudart-11-0 (11.0.194-1) ...
Setting up default-jre-headless (2:1.11-68ubuntu1~18.04.1) ...
Setting up xserver-xorg-video-nvidia-450 (450.51.05-0ubuntu1) ...
Setting up libcufft-dev-11-0 (10.2.0.218-1) ...
Setting up nsight-compute-2020.1.1 (2020.1.1.8-1) ...
Setting up openjdk-11-jre:amd64 (11.0.8+10-0ubuntu1~18.04.1) ...
Setting up libcusparse-dev-11-0 (11.1.0.218-1) ...
Setting up libnvidia-decode-450:amd64 (450.51.05-0ubuntu1) ...
Setting up cuda-gdb-11-0 (11.0.194-1) ...
Setting up libnvidia-encode-450:amd64 (450.51.05-0ubuntu1) ...
Setting up libnvjpeg-dev-11-0 (11.1.0.218-1) ...
Setting up default-jre (2:1.11-68ubuntu1~18.04.1) ...
Setting up cuda-cudart-dev-11-0 (11.0.194-1) ...
Setting up cuda-libraries-11-0 (11.0.2-1) ...
Setting up cuda-nvrtc-dev-11-0 (11.0.194-1) ...
Setting up cuda-nsight-11-0 (11.0.194-1) ...
Setting up libnvidia-gl-450:amd64 (450.51.05-0ubuntu1) ...
Setting up cuda-nvvp-11-0 (11.0.194-1) ...
Setting up cuda-nsight-compute-11-0 (11.0.2-1) ...
Setting up libnvidia-ifr1-450:amd64 (450.51.05-0ubuntu1) ...
Setting up cuda-libraries-dev-11-0 (11.0.2-1) ...
Setting up cuda-nvcc-11-0 (11.0.194-1) ...
Setting up cuda-samples-11-0 (11.0.194-1) ...
Setting up cuda-compiler-11-0 (11.0.2-1) ...
Setting up nvidia-driver-450 (450.51.05-0ubuntu1) ...
Setting up cuda-documentation-11-0 (11.0.207-1) ...
Setting up cuda-visual-tools-11-0 (11.0.2-1) ...
Setting up cuda-cupti-11-0 (11.0.194-1) ...
Setting up cuda-cupti-dev-11-0 (11.0.194-1) ...
Setting up cuda-command-line-tools-11-0 (11.0.2-1) ...
Setting up cuda-drivers-450 (450.51.05-1) ...
Setting up cuda-tools-11-0 (11.0.2-1) ...
Setting up cuda-drivers (450.51.05-1) ...
Setting up cuda-toolkit-11-0 (11.0.2-1) ...
Setting up cuda-runtime-11-0 (11.0.2-1) ...
Setting up cuda-demo-suite-11-0 (11.0.167-1) ...
Setting up cuda-11-0 (11.0.2-1) ...
Setting up cuda (11.0.2-1) ...
Processing triggers for gnome-menus (3.13.3-11ubuntu1.1) ...
Processing triggers for hicolor-icon-theme (0.17-2) ...
Processing triggers for mime-support (3.60ubuntu1) ...
Processing triggers for desktop-file-utils (0.23-1ubuntu3.18.04.2) ...
Processing triggers for initramfs-tools (0.130ubuntu3.9) ...
update-initramfs: Generating /boot/initrd.img-5.4.0-42-generic
W: Possible missing firmware /lib/firmware/rtl_nic/rtl8125a-3.fw for module r8169
Processing triggers for libc-bin (2.27-3ubuntu1.2) ...
Processing triggers for man-db (2.8.3-2ubuntu0.1) ...
(opencv_cuda) dhankar@dhankar-1:~$ 
(opencv_cuda) dhankar@dhankar-1:~$ 

```

#

```
(base) dhankar@dhankar-1:~/_dc_all/cv20/cv2020$ nvidia-smi
Sat Jul 25 17:22:23 2020       
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 450.51.05    Driver Version: 450.51.05    CUDA Version: 11.0     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                               |                      |               MIG M. |
|===============================+======================+======================|
|   0  GeForce GTX 1650    On   | 00000000:01:00.0  On |                  N/A |
|  0%   45C    P8     4W /  75W |    216MiB /  3910MiB |      1%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+
                                                                               
+-----------------------------------------------------------------------------+
| Processes:                                                                  |
|  GPU   GI   CI        PID   Type   Process name                  GPU Memory |
|        ID   ID                                                   Usage      |
|=============================================================================|
|    0   N/A  N/A      1741      G   /usr/lib/xorg/Xorg                 14MiB |
|    0   N/A  N/A      2142      G   /usr/bin/gnome-shell               49MiB |
|    0   N/A  N/A      3868      G   /usr/lib/xorg/Xorg                 86MiB |
|    0   N/A  N/A      4001      G   /usr/bin/gnome-shell               62MiB |
+-----------------------------------------------------------------------------+
(base) dhankar@dhankar-1:~/_dc_all/cv20/cv2020$ 
```
#

