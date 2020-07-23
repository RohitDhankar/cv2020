#### This has terminal dumps while Compiling OpenCV using CMAKE .

#
```
(tensorflow_gpuenv) dhankar@dhankar-1:~/_dc_all/cv20/cv2020/2_Feature Detection_SIFT_SURF$ python SURF_FeatureDetection.py --img_in ./Input_Images/box.png
Traceback (most recent call last):
  File "SURF_FeatureDetection.py", line 21, in <module>
    detector = cv.xfeatures2d_SURF.create(hessianThreshold=minHessian)
AttributeError: module 'cv2.cv2' has no attribute 'xfeatures2d_SURF'

#
Own version of OpenCV Installed == opencv-python==4.2.0.34

As not done CMAKE for CV2 - certain Functionality NOT AVAILABLE for FREE 
To use SIFT or SURF - "must compile OpenCV from sources" - CMAKE as was done back in 2017.  

export CMAKE_ARGS="-DOPENCV_ENABLE_NONFREE=ON -DWITH_TBB=ON -DWITH_CUDA=ON -DWITH_CUDNN=ON 
-DOPENCV_DNN_CUDA=ON -DCUDA_ARCH_BIN=7.5 -DBUILD_opencv_cudacodec=OFF -DENABLE_FAST_MATH=1 
-DCUDA_FAST_MATH=1 -DWITH_CUBLAS=1 -DWITH_V4L=ON -DWITH_QT=OFF -DWITH_OPENGL=ON -DWITH_GSTREAMER=ON 
-DOPENCV_GENERATE_PKGCONFIG=ON -DOPENCV_ENABLE_NONFREE=ON 
-DOPENCV_EXTRA_MODULES_PATH=/tmp/opencv-python/opencv_contrib/modules"
python3 setup.py bdist_wheel
cd dist
pip3 install opencv_python-4.3.0+3073e9e-cp36-cp36m-linux_x86_64.whl


# REFER HERE -- 
# REFER HERE -- https://github.com/skvark/opencv-python

# Even ROS restricts use of SIFT and SURF from OpenCV - https://answers.ros.org/question/34557/opencv-patent/

As suggested by the Maintainers of - opencv-python --- "must compile OpenCV from sources" https://github.com/skvark/opencv-python/issues/126
```

#


```
(base) dhankar@dhankar-1:~/_dc_all/cv20$ mkdir cmake_opencv
(base) dhankar@dhankar-1:~/_dc_all/cv20$ cd cmake_opencv

(base) dhankar@dhankar-1:~/_dc_all/cv20/cmake_opencv$ git clone --recursive https://github.com/skvark/opencv-python.git
Cloning into 'opencv-python'...
remote: Enumerating objects: 136, done.
remote: Counting objects: 100% (136/136), done.
remote: Compressing objects: 100% (96/96), done.
remote: Total 2045 (delta 83), reused 90 (delta 39), pack-reused 1909
Receiving objects: 100% (2045/2045), 1.48 MiB | 963.00 KiB/s, done.
Resolving deltas: 100% (1266/1266), done.
Submodule 'multibuild' (https://github.com/matthew-brett/multibuild.git) registered for path 'multibuild'
Submodule 'opencv' (https://github.com/opencv/opencv.git) registered for path 'opencv'
Submodule 'opencv_contrib' (https://github.com/opencv/opencv_contrib.git) registered for path 'opencv_contrib'
Cloning into '/home/dhankar/_dc_all/cv20/cmake_opencv/opencv-python/multibuild'...
remote: Enumerating objects: 5, done.        
remote: Counting objects: 100% (5/5), done.        
remote: Compressing objects: 100% (5/5), done.        
remote: Total 2544 (delta 0), reused 1 (delta 0), pack-reused 2539        
Receiving objects: 100% (2544/2544), 1.35 MiB | 827.00 KiB/s, done.
Resolving deltas: 100% (1663/1663), done.
Cloning into '/home/dhankar/_dc_all/cv20/cmake_opencv/opencv-python/opencv'...
remote: Enumerating objects: 5, done.        
remote: Counting objects: 100% (5/5), done.        
remote: Compressing objects: 100% (5/5), done.        
remote: Total 277040 (delta 0), reused 1 (delta 0), pack-reused 277035        
Receiving objects: 100% (277040/277040), 470.20 MiB | 1.25 MiB/s, done.
Resolving deltas: 100% (193581/193581), done.
Cloning into '/home/dhankar/_dc_all/cv20/cmake_opencv/opencv-python/opencv_contrib'...
remote: Enumerating objects: 9, done.        
remote: Counting objects: 100% (9/9), done.        
remote: Compressing objects: 100% (9/9), done.        
remote: Total 32622 (delta 0), reused 2 (delta 0), pack-reused 32613        
Receiving objects: 100% (32622/32622), 129.17 MiB | 2.60 MiB/s, done.
Resolving deltas: 100% (20169/20169), done.
Submodule path 'multibuild': checked out 'c2890dc8dc93f99b0eadd76f87aa181f6aea42da'
Submodule path 'opencv': checked out '01b2c5a77ca6dbef3baef24ebc0a5984579231d9'
Submodule path 'opencv_contrib': checked out 'e6f32c6a69043456a806a4e802ee3ce7b7059c93'

(base) dhankar@dhankar-1:~/_dc_all/cv20/cmake_opencv$ cd opencv-python
(base) dhankar@dhankar-1:~/_dc_all/cv20/cmake_opencv/opencv-python$ ls -ltr
total 232
-rw-r--r--  1 dhankar dhankar 113621 Jul 23 12:07 LICENSE-3RD-PARTY.txt
-rw-r--r--  1 dhankar dhankar    846 Jul 23 12:07 CONTRIBUTING.md
-rw-r--r--  1 dhankar dhankar  15677 Jul 23 12:07 setup.py
-rw-r--r--  1 dhankar dhankar  13652 Jul 23 12:07 README.md
-rw-r--r--  1 dhankar dhankar    253 Jul 23 12:07 pyproject.toml
drwxr-xr-x  2 dhankar dhankar   4096 Jul 23 12:07 patches
-rw-r--r--  1 dhankar dhankar    273 Jul 23 12:07 MANIFEST.in
-rw-r--r--  1 dhankar dhankar   1070 Jul 23 12:07 LICENSE.txt
-rw-r--r--  1 dhankar dhankar   2097 Jul 23 12:07 find_version.py
drwxr-xr-x  4 dhankar dhankar   4096 Jul 23 12:07 docker
drwxr-xr-x  3 dhankar dhankar   4096 Jul 23 12:07 cv2
-rw-r--r--  1 dhankar dhankar   4594 Jul 23 12:07 appveyor.yml
-rw-r--r--  1 dhankar dhankar  17648 Jul 23 12:07 travis_osx_brew_cache.sh
-rw-r--r--  1 dhankar dhankar    277 Jul 23 12:07 travis_multibuild_customize.sh
-rw-r--r--  1 dhankar dhankar   4941 Jul 23 12:07 travis_config.sh
drwxr-xr-x  2 dhankar dhankar   4096 Jul 23 12:07 tests
drwxr-xr-x  4 dhankar dhankar   4096 Jul 23 12:14 multibuild
drwxr-xr-x 12 dhankar dhankar   4096 Jul 23 12:14 opencv
drwxr-xr-x  6 dhankar dhankar   4096 Jul 23 12:14 opencv_contrib

(base) dhankar@dhankar-1:~/_dc_all/cv20/cmake_opencv/opencv-python$ which cmake
/usr/bin/cmake
(base) dhankar@dhankar-1:~/_dc_all/cv20/cmake_opencv/opencv-python$ cmake --version
cmake version 3.10.2

CMake suite maintained and supported by Kitware (kitware.com/cmake).
```

#


