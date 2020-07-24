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
####

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

#
```
2020-05-04 18:35:20 install libcudart9.1:amd64 <none> 9.1.85-3ubuntu1
2020-05-04 18:35:20 status half-installed libcudart9.1:amd64 9.1.85-3ubuntu1
```
#
