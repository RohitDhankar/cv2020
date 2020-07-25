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
(base) dhankar@dhankar-1:~/opencv_cuda/cudNN_installers$ tar -zxf libcudnn8_8.0.1.13-1+cuda11.0_amd64.deb

gzip: stdin: not in gzip format
tar: Child returned status 1
tar: Error is not recoverable: exiting now
(base) dhankar@dhankar-1:~/opencv_cuda/cudNN_installers$ 
(base) dhankar@dhankar-1:~/opencv_cuda/cudNN_installers$ dpkg -l | grep cudnn
ii  libcudnn7                                  7.6.4.38-1+cuda10.1                              amd64        cuDNN runtime libraries
(base) dhankar@dhankar-1:~/opencv_cuda/cudNN_installers$ 

##### Before install of the new compatible versions of - cudnn -  need to remove using - dpkg - the old version seen above. 

(base) dhankar@dhankar-1:~/opencv_cuda/cudNN_installers$ sudo dpkg -r libcudnn7
[sudo] password for dhankar: 
(Reading database ... 314041 files and directories currently installed.)
Removing libcudnn7 (7.6.4.38-1+cuda10.1) ...
Processing triggers for libc-bin (2.27-3ubuntu1.2) ...

(base) dhankar@dhankar-1:~/opencv_cuda/cudNN_installers$ dpkg -l | grep cudnn
(base) dhankar@dhankar-1:~/opencv_cuda/cudNN_installers$ 

```
#

```

```
#

> Now within the - CmakeCache.txt file - we will need to provide the DIR PATH for the - cudnn - installed. 
//location of the cuDNN library
CUDNN_LIBRARY:FILEPATH=CUDA_cudnn_LIBRARY-NOTFOUND

