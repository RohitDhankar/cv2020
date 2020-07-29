##### Learning CMAKE 

```
(base) dhankar@dhankar-1:~/_dc_all/cv20/cv2020/learning_CMAKE/cmake_test_1$ touch CMakeLists.txt
(base) dhankar@dhankar-1:~/_dc_all/cv20/cv2020/learning_CMAKE/cmake_test_1$ gedit CMakeLists.txt
(base) dhankar@dhankar-1:~/_dc_all/cv20/cv2020/learning_CMAKE/cmake_test_1$ cmake --version
cmake version 3.10.2

CMake suite maintained and supported by Kitware (kitware.com/cmake).
(base) dhankar@dhankar-1:~/_dc_all/cv20/cv2020/learning_CMAKE/cmake_test_1$ ls -ltr
total 4
-rw-r--r-- 1 dhankar dhankar 73 Jul 29 21:48 CMakeLists.txt
(base) dhankar@dhankar-1:~/_dc_all/cv20/cv2020/learning_CMAKE/cmake_test_1$ mkdir build
(base) dhankar@dhankar-1:~/_dc_all/cv20/cv2020/learning_CMAKE/cmake_test_1$ ls -ltr
total 8
-rw-r--r-- 1 dhankar dhankar   73 Jul 29 21:48 CMakeLists.txt
drwxr-xr-x 2 dhankar dhankar 4096 Jul 29 21:49 build
(base) dhankar@dhankar-1:~/_dc_all/cv20/cv2020/learning_CMAKE/cmake_test_1$ cd build
(base) dhankar@dhankar-1:~/_dc_all/cv20/cv2020/learning_CMAKE/cmake_test_1/build$ # now give - cmake -- path to source directory
(base) dhankar@dhankar-1:~/_dc_all/cv20/cv2020/learning_CMAKE/cmake_test_1/build$ # cmake ..
(base) dhankar@dhankar-1:~/_dc_all/cv20/cv2020/learning_CMAKE/cmake_test_1/build$ cmake ..
-- The C compiler identification is GNU 7.5.0
-- The CXX compiler identification is GNU 7.5.0
-- Check for working C compiler: /usr/lib/ccache/cc
-- Check for working C compiler: /usr/lib/ccache/cc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting C compile features - done
-- Check for working CXX compiler: /usr/lib/ccache/c++
-- Check for working CXX compiler: /usr/lib/ccache/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Configuring done
-- Generating done
-- Build files have been written to: /home/dhankar/_dc_all/cv20/cv2020/learning_CMAKE/cmake_test_1/build
(base) dhankar@dhankar-1:~/_dc_all/cv20/cv2020/learning_CMAKE/cmake_test_1/build$ 
(base) dhankar@dhankar-1:~/_dc_all/cv20/cv2020/learning_CMAKE/cmake_test_1/build$ ls -ltr
total 28
-rw-r--r-- 1 dhankar dhankar  3909 Jul 29 21:50 Makefile
-rw-r--r-- 1 dhankar dhankar  1574 Jul 29 21:50 cmake_install.cmake
drwxr-xr-x 4 dhankar dhankar  4096 Jul 29 21:50 CMakeFiles
-rw-r--r-- 1 dhankar dhankar 12785 Jul 29 21:50 CMakeCache.txt
(base) dhankar@dhankar-1:~/_dc_all/cv20/cv2020/learning_CMAKE/cmake_test_1/build$ 

```
