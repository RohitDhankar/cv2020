##### Issue solved - see at end of this file == FOOBAR_BestInstall_CMAKE

- Further trouble was created ROS packages were deleted - FOOBAR_ROS_Destroyed 

#

##### CMAKE installed and upgraded to latest version according to instructions on their official site here - 

#

- https://cmake.org/download/

>  Seem to have missed critical warning - remove previous installations of CMAKE  == If there is no existing CMake installation, a bootstrap script is provided:

- https://cmake.org/install/

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
Use ``` sudo checkinstall ``` inplace of ```sudo make install ``` as probably done by me earlier - i seem to have followed ( probably incorrectly some tutorial ) 

#

> Also as recommended in the official site - https://cmake.org/download/ , we need to Remove the earlier installed CMAKE before we run the ``` bootstrap ``` script . I probably did not remove the earlier CMAKE . 
#

##### CMAKE Uninstall removes my ROS Packages ? Seems totally wrong - this will surely break a lot of things for my ROS ? 

```
(base) dhankar@dhankar-1:~/_dc_all/cv20/cv2020$ sudo apt-get remove cmake
[sudo] password for dhankar: 
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following packages were automatically installed and are no longer required:
  cmake-data efibootmgr fonts-wine gconf-service gconf-service-backend gconf2 gconf2-common gir1.2-geocodeglib-1.0 google-mock googletest
  libappindicator1 libapr1 libapr1-dev libaprutil1 libaprutil1-dev libassuan-dev libavdevice57 libboost-all-dev libboost-atomic-dev
  libboost-chrono-dev libboost-container-dev libboost-context-dev libboost-coroutine-dev libboost-date-time-dev libboost-exception-dev
  libboost-fiber-dev libboost-filesystem-dev libboost-graph-dev libboost-graph-parallel-dev libboost-iostreams-dev libboost-locale-dev
  libboost-log-dev libboost-math-dev libboost-mpi-dev libboost-mpi-python-dev libboost-numpy-dev libboost-program-options-dev
  libboost-python-dev libboost-random-dev libboost-regex-dev libboost-serialization-dev libboost-signals-dev libboost-stacktrace-dev
  libboost-system-dev libboost-test-dev libboost-thread-dev libboost-timer-dev libboost-tools-dev libboost-type-erasure-dev
  libboost-wave-dev libconsole-bridge-dev libconsole-bridge0.4 libfwup1 libgconf-2-4 libgeos-3.6.2 libgeotiff2 libgpg-error-dev libgpgme-dev
  libgtest-dev libindicator7 libjsoncpp1 libllvm8 libllvm8:i386 libllvm9 libllvm9:i386 liblo7 liblog4cxx-dev liblog4cxx10v5 liblz4-dev
  libmxml-bin libmxml-dev libmxml1 libnvidia-common-435 libnvidia-common-440 libpoco-dev libpococrypto50 libpocodata50 libpocodatamysql50
  libpocodataodbc50 libpocodatasqlite50 libpocofoundation50 libpocojson50 libpocomongodb50 libpoconet50 libpoconetssl50 libpocoredis50
  libpocoutil50 libpocoxml50 libpocozip50 libproj12 libproj13 libqgis-3d3.12.3 libqgis-analysis3.12.3 libqgis-app3.12.3 libqgis-core3.12.3
  libqgis-gui3.12.3 libqgis-native3.12.3 libqgis-server3.12.3 libqgisgrass7-3.12.3 libqgispython3.12.3 librhash0 libsctp-dev libsctp1
  libtinyxml-dev libtinyxml2-dev libuv1 libwine:i386 libwxbase3.0-0v5 libwxgtk3.0-gtk3-0v5 pyqt5-dev python-defusedxml python-empy
  python-gnupg python-netifaces python-nose python-numpy python-pycryptodome python-pydot python-pyqt5 python-pyqt5.qtsvg python-sip
  python-sip-dev python-wxgtk3.0 python-wxtools python-wxversion python3-sip-dev ros-melodic-class-loader ros-melodic-cmake-modules
  ros-melodic-cpp-common ros-melodic-ros-environment ros-melodic-rosbag-migration-rule ros-melodic-rosboost-cfg ros-melodic-rosclean
  ros-melodic-roscpp-core ros-melodic-roscpp-serialization ros-melodic-roscpp-traits ros-melodic-rosgraph ros-melodic-roslz4
  ros-melodic-rosmaster ros-melodic-rospack ros-melodic-rosparam ros-melodic-rostime ros-melodic-smclib ros-melodic-xmlrpcpp sbcl sip-dev
  ubuntu-web-launchers wine32:i386
Use 'sudo apt autoremove' to remove them.
The following packages will be REMOVED:
  cmake ros-melodic-actionlib ros-melodic-actionlib-msgs ros-melodic-bond ros-melodic-bond-core ros-melodic-bondcpp ros-melodic-bondpy
  ros-melodic-catkin ros-melodic-common-msgs ros-melodic-diagnostic-msgs ros-melodic-dynamic-reconfigure ros-melodic-gencpp
  ros-melodic-geneus ros-melodic-genlisp ros-melodic-genmsg ros-melodic-gennodejs ros-melodic-genpy ros-melodic-geometry-msgs
  ros-melodic-message-filters ros-melodic-message-generation ros-melodic-message-runtime ros-melodic-mk ros-melodic-nav-msgs
  ros-melodic-nodelet ros-melodic-nodelet-core ros-melodic-nodelet-topic-tools ros-melodic-pluginlib ros-melodic-python-qt-binding
  ros-melodic-qt-dotgraph ros-melodic-qt-gui ros-melodic-qt-gui-cpp ros-melodic-ros ros-melodic-ros-base ros-melodic-ros-comm
  ros-melodic-ros-core ros-melodic-ros-tutorials ros-melodic-rosbag ros-melodic-rosbag-storage ros-melodic-rosbash ros-melodic-rosbuild
  ros-melodic-rosconsole ros-melodic-rosconsole-bridge ros-melodic-roscpp ros-melodic-roscpp-tutorials ros-melodic-roscreate
  ros-melodic-rosgraph-msgs ros-melodic-roslang ros-melodic-roslaunch ros-melodic-roslib ros-melodic-roslisp ros-melodic-rosmake
  ros-melodic-rosmsg ros-melodic-rosnode ros-melodic-rosout ros-melodic-rospy ros-melodic-rospy-tutorials ros-melodic-rosservice
  ros-melodic-rostest ros-melodic-rostopic ros-melodic-rosunit ros-melodic-roswtf ros-melodic-rqt ros-melodic-rqt-graph ros-melodic-rqt-gui
  ros-melodic-rqt-gui-cpp ros-melodic-rqt-gui-py ros-melodic-sensor-msgs ros-melodic-shape-msgs ros-melodic-std-msgs ros-melodic-std-srvs
  ros-melodic-stereo-msgs ros-melodic-topic-tools ros-melodic-trajectory-msgs ros-melodic-turtlesim ros-melodic-visualization-msgs
0 upgraded, 0 newly installed, 75 to remove and 36 not upgraded.
After this operation, 47.6 MB disk space will be freed.
Do you want to continue? [Y/n] y
(Reading database ... 314458 files and directories currently installed.)
Removing ros-melodic-rqt-graph (0.4.11-1bionic.20200613.045147) ...
Removing ros-melodic-ros-base (1.4.1-0bionic.20200530.140017) ...
Removing ros-melodic-ros-core (1.4.1-0bionic.20200530.134357) ...
Removing ros-melodic-ros-comm (1.14.6-1bionic.20200530.082644) ...
Removing ros-melodic-roswtf (1.14.6-1bionic.20200530.081019) ...
Removing ros-melodic-ros (1.14.9-1bionic.20200529.234812) ...
Removing ros-melodic-rosmake (1.14.9-1bionic.20200529.213712) ...
Removing ros-melodic-actionlib (1.12.0-1bionic.20200530.075505) ...
Removing ros-melodic-common-msgs (1.12.7-0bionic.20200530.133110) ...
Removing ros-melodic-nav-msgs (1.12.7-0bionic.20200530.013349) ...
Removing ros-melodic-actionlib-msgs (1.12.7-0bionic.20200530.012008) ...
Removing ros-melodic-bond-core (1.8.5-1bionic.20200530.022416) ...
Removing ros-melodic-rqt (0.5.2-1bionic.20200613.045030) ...
Removing ros-melodic-rqt-gui-cpp (0.5.2-1bionic.20200613.044617) ...
Removing ros-melodic-bondpy (1.8.5-1bionic.20200530.021055) ...
Removing ros-melodic-diagnostic-msgs (1.12.7-0bionic.20200529.234037) ...
Removing ros-melodic-nodelet-core (1.9.16-0bionic.20200530.104855) ...
Removing ros-melodic-nodelet-topic-tools (1.9.16-0bionic.20200530.103359) ...
Removing ros-melodic-dynamic-reconfigure (1.6.3-1bionic.20200530.093111) ...
Removing ros-melodic-mk (1.14.9-1bionic.20200529.232356) ...
Removing ros-melodic-ros-tutorials (0.9.2-1bionic.20200530.030942) ...
Removing ros-melodic-turtlesim (0.9.2-1bionic.20200530.020039) ...
Removing ros-melodic-roslisp (1.9.24-1bionic.20200530.013541) ...
Removing ros-melodic-roslang (1.14.9-1bionic.20200529.220402) ...
Removing ros-melodic-rosnode (1.14.6-1bionic.20200530.033051) ...
Removing ros-melodic-rostopic (1.14.6-1bionic.20200530.031535) ...
Removing ros-melodic-rqt-gui-py (0.5.2-1bionic.20200613.044501) ...
Removing ros-melodic-visualization-msgs (1.12.7-0bionic.20200530.000922) ...
Removing ros-melodic-trajectory-msgs (1.12.7-0bionic.20200530.000654) ...
Removing ros-melodic-message-filters (1.14.6-1bionic.20200530.024328) ...
Removing ros-melodic-qt-gui-cpp (0.4.1-1bionic.20200613.044041) ...
Removing ros-melodic-rqt-gui (0.5.2-1bionic.20200613.043903) ...
Removing ros-melodic-qt-dotgraph (0.4.1-1bionic.20200613.043538) ...
Removing ros-melodic-qt-gui (0.4.1-1bionic.20200613.043620) ...
Removing ros-melodic-rosbash (1.14.9-1bionic.20200529.223006) ...
Removing ros-melodic-rosconsole-bridge (0.5.3-0bionic.20200530.001213) ...
Removing ros-melodic-rostest (1.14.6-1bionic.20200530.022337) ...
Removing ros-melodic-roslaunch (1.14.6-1bionic.20200530.020940) ...
Removing ros-melodic-rosout (1.14.6-1bionic.20200530.015741) ...
Removing ros-melodic-roscpp-tutorials (0.9.2-1bionic.20200530.015711) ...
Removing ros-melodic-roscreate (1.14.9-1bionic.20200529.224230) ...
Removing ros-melodic-rosunit (1.14.9-1bionic.20200529.224236) ...
Removing ros-melodic-rospy-tutorials (0.9.2-1bionic.20200530.025151) ...
Removing ros-melodic-stereo-msgs (1.12.7-0bionic.20200530.131201) ...
Removing ros-melodic-sensor-msgs (1.12.7-0bionic.20200530.031753) ...
Removing ros-melodic-shape-msgs (1.12.7-0bionic.20200530.000546) ...
Removing ros-melodic-rosservice (1.14.6-1bionic.20200530.075342) ...
Removing ros-melodic-rosmsg (1.14.6-1bionic.20200530.031608) ...
Removing ros-melodic-nodelet (1.9.16-0bionic.20200530.020959) ...
Removing ros-melodic-bondcpp (1.8.5-1bionic.20200530.014946) ...
Removing ros-melodic-bond (1.8.5-1bionic.20200529.232913) ...
Removing ros-melodic-rosbag (1.14.6-1bionic.20200530.030003) ...
Removing ros-melodic-rospy (1.14.6-1bionic.20200530.015841) ...
Removing ros-melodic-geometry-msgs (1.12.7-0bionic.20200529.232546) ...
Removing ros-melodic-topic-tools (1.14.6-1bionic.20200530.024331) ...
Removing ros-melodic-rosbag-storage (1.14.6-1bionic.20200530.024308) ...
Removing ros-melodic-pluginlib (1.12.1-0bionic.20200529.235012) ...
Removing ros-melodic-python-qt-binding (0.4.3-1bionic.20200613.042131) ...
Removing ros-melodic-roscpp (1.14.6-1bionic.20200530.013156) ...
Removing ros-melodic-rosgraph-msgs (1.11.2-0bionic.20200530.012010) ...
Removing ros-melodic-roslib (1.14.9-1bionic.20200529.222958) ...
Removing ros-melodic-std-msgs (0.5.12-0bionic.20200529.231145) ...
Removing ros-melodic-std-srvs (1.11.2-0bionic.20200529.231244) ...
Removing ros-melodic-rosconsole (1.13.11-1bionic.20200529.232409) ...
Removing ros-melodic-rosbuild (1.14.9-1bionic.20200529.231006) ...
Removing ros-melodic-message-generation (0.4.1-1bionic.20200529.221414) ...
Removing ros-melodic-gencpp (0.6.5-1bionic.20200529.220139) ...
Removing ros-melodic-geneus (2.2.6-0bionic.20200529.220145) ...
Removing ros-melodic-genlisp (0.4.16-0bionic.20200529.220206) ...
Removing ros-melodic-gennodejs (2.0.1-0bionic.20200529.220157) ...
Removing ros-melodic-message-runtime (0.4.12-0bionic.20200529.225821) ...
Removing ros-melodic-genpy (0.6.12-1bionic.20200529.220208) ...
Removing ros-melodic-genmsg (0.5.16-1bionic.20200529.214901) ...
Removing ros-melodic-catkin (0.7.26-1bionic.20200529.204155) ...
Removing cmake (3.10.2-1ubuntu2.18.04.1) ...
Processing triggers for man-db (2.8.3-2ubuntu0.1) ...
(base) dhankar@dhankar-1:~/_dc_all/cv20/cv2020$ 

```

###### Worst Fears Confirmed --- FOOBAR_ROS_Destroyed -- ROS destroyed while updating System CMAKE 

- https://answers.ros.org/question/293119/how-can-i-updateremove-cmake-without-partially-deleting-my-ros-distribution/

> I don't think you should remove the system cmake. This will only lead to the problems you described. Instead, you could simply install your own version of cmake and let it override the system cmake.   

```
cd ~/Downloads/cmake-3.12.0-rc3/   # or wherever you downloaded cmake
./bootstrap --prefix=$HOME/cmake-install
make 
make install
export PATH=$HOME/cmake-install/bin:$PATH
export CMAKE_PREFIX_PATH=$HOME/cmake-install:$CMAKE_PREFIX_PATH
```


###### Make Uninstall - sudo make uninstall- to remove Latest CMAKE - cmake-3.18.1

- https://askubuntu.com/a/942740/958183

```
base) dhankar@dhankar-1:~/CMAKE_latest_Aug2020/cmake-3.18.1$ 
(base) dhankar@dhankar-1:~/CMAKE_latest_Aug2020/cmake-3.18.1$ sudo make uninstall
Scanning dependencies of target uninstall
-- Uninstalling "/usr/local/doc/cmake-3.18/cmsys/Copyright.txt"
-- Uninstalling "/usr/local/doc/cmake-3.18/cmlibrhash/COPYING"
-- Uninstalling "/usr/local/doc/cmake-3.18/cmzlib/Copyright.txt"
-- Uninstalling "/usr/local/doc/cmake-3.18/cmcurl/COPYING"
-- Uninstalling "/usr/local/doc/cmake-3.18/cmnghttp2/COPYING"
-- Uninstalling "/usr/local/doc/cmake-3.18/cmzstd/LICENSE"
-- Uninstalling "/usr/local/doc/cmake-3.18/cmliblzma/COPYING"
-- Uninstalling "/usr/local/doc/cmake-3.18/cmlibarchive/COPYING"
-- Uninstalling "/usr/local/doc/cmake-3.18/cmlibuv/LICENSE"
-- Uninstalling "/usr/local/bin/ccmake"
-- Uninstalling "/usr/local/bin/cmake"
-- Uninstalling "/usr/local/bin/ctest"
-- Uninstalling "/usr/local/bin/cpack"
-- Uninstalling "/usr/local/share/cmake-3.18/include/cmCPluginAPI.h"
-- Uninstalling "/usr/local/doc/cmake-3.18/Copyright.txt"
-- Uninstalling "/usr/local/share/cmake-3.18/Help/prop_gbl/AUTOMOC_SOURCE_GROUP.rst"
-- Uninstalling "/usr/local/share/cmake-3.18/Help/prop_gbl/FIND_LIBRARY_USE_OPENBSD_VERSIONING.rst"
-- Uninstalling "/usr/local/share/cmake-3.18/Help/prop_gbl/AUTOGEN_TARGETS_FOLDER.rst"
-- Uninstalling "/usr/local/share/cmake-3.18/Help/prop_gbl/PACKAGES_FOUND.rst"
-- Uninstalling "/usr/local/share/cmake-3.18/Help/prop_gbl/ENABLED_LANGUAGES.rst"
-- Uninstalling "/usr/local/share/cmake-3.18/Help/prop_gbl/FIND_LIBRARY_USE_LIB64_PATHS.rst"
...................................
-- Uninstalling "/usr/local/share/cmake-3.18/Templates/MSBuild/FlagTables/v11_CL.json"
-- Uninstalling "/usr/local/share/cmake-3.18/Templates/MSBuild/FlagTables/v10_CSharp.json"
-- Uninstalling "/usr/local/share/cmake-3.18/Templates/MSBuild/FlagTables/v10_NASM.json"
-- Uninstalling "/usr/local/share/cmake-3.18/Templates/MSBuild/FlagTables/v11_LIB.json"
-- Uninstalling "/usr/local/share/cmake-3.18/Templates/MSBuild/nasm.xml"
-- Uninstalling "/usr/local/share/cmake-3.18/Templates/MSBuild/nasm.targets"
-- Uninstalling "/usr/local/share/cmake-3.18/Templates/MSBuild/nasm.props.in"
-- Uninstalling "/usr/local/share/vim/vimfiles/indent/cmake.vim"
-- Uninstalling "/usr/local/share/vim/vimfiles/syntax/cmake.vim"
-- Uninstalling "/usr/local/share/emacs/site-lisp/cmake-mode.el"
-- Uninstalling "/usr/local/share/aclocal/cmake.m4"
-- Uninstalling "/usr/local/share/bash-completion/completions/cmake"
-- Uninstalling "/usr/local/share/bash-completion/completions/cpack"
-- Uninstalling "/usr/local/share/bash-completion/completions/ctest"
Built target uninstall
(base) dhankar@dhankar-1:~/CMAKE_latest_Aug2020/cmake-3.18.1$ 
(base) dhankar@dhankar-1:~/CMAKE_latest_Aug2020/cmake-3.18.1$ 

```

##### Ubuntu  - apt package manager offers old versions of CMAKE --- 

```
dhankar@dhankar-1:~/CMAKE_latest_Aug2020/cmake-3.18.1$ apt search cmake 
Sorting... Done
Full Text Search... Done
bear/bionic,bionic 2.3.11-1 all
  generate compilation database for Clang tooling

catkin/bionic,bionic 0.7.8-1 all
  Low-level build system macros and infrastructure for Robot OS

cmake/bionic-updates 3.10.2-1ubuntu2.18.04.1 amd64
  cross-platform, open-source make system

cmake-curses-gui/bionic-updates 3.10.2-1ubuntu2.18.04.1 amd64
  curses based user interface for CMake (ccmake)

cmake-data/bionic-updates,bionic-updates,now 3.10.2-1ubuntu2.18.04.1 all [installed,auto-removable]
  CMake data files (modules, templates and documentation)

cmake-doc/bionic-updates,bionic-updates 3.10.2-1ubuntu2.18.04.1 all
  extended documentation in various formats for CMake

cmake-extras/bionic,bionic 1.3+17.04.20170310-1ubuntu4 all
  Extra CMake utility modules

```

#

##### Install CMAKE from the - shell script -- FOOBAR_BestInstall_CMAKE

> Followed instructions from this excellent YouTube tutorial - this is by vector-of-bool - the initial maintainer of CMAKE Tools for VS COde 

```
(base) dhankar@dhankar-1:~/CMAKE_latest_Aug2020/CMAKE_ShellScript_Install$ sh cmake-3.18.1-Linux-x86_64.sh -h
CMake Installer Version: 3.18.1, Copyright (c) Kitware
This is a self-extracting archive.
The archive will be extracted to: /home/dhankar/CMAKE_latest_Aug2020/CMAKE_ShellScript_Install

If you want to stop extracting, please press <ctrl-C>.
CMake - Cross Platform Makefile Generator
Copyright 2000-2020 Kitware, Inc. and Contributors
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions
are met:

* Redistributions of source code must retain the above copyright
  notice, this list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright
  notice, this list of conditions and the following disclaimer in the
  documentation and/or other materials provided with the distribution.

* Neither the name of Kitware, Inc. nor the names of Contributors
  may be used to endorse or promote products derived from this
  software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

------------------------------------------------------------------------------

The following individuals and institutions are among the Contributors:

* Aaron C. Meadows <cmake@shadowguarddev.com>
* Adriaan de Groot <groot@kde.org>
* Aleksey Avdeev <solo@altlinux.ru>
* Alexander Neundorf <neundorf@kde.org>
* Alexander Smorkalov <alexander.smorkalov@itseez.com>
* Alexey Sokolov <sokolov@google.com>
* Alex Merry <alex.merry@kde.org>
* Alex Turbov <i.zaufi@gmail.com>
* Andreas Pakulat <apaku@gmx.de>
* Andreas Schneider <asn@cryptomilk.org>
* André Rigland Brodtkorb <Andre.Brodtkorb@ifi.uio.no>
* Axel Huebl, Helmholtz-Zentrum Dresden - Rossendorf
* Benjamin Eikel
* Bjoern Ricks <bjoern.ricks@gmail.com>
* Brad Hards <bradh@kde.org>
* Christopher Harvey
* Christoph Grüninger <foss@grueninger.de>
* Clement Creusot <creusot@cs.york.ac.uk>
* Daniel Blezek <blezek@gmail.com>
* Daniel Pfeifer <daniel@pfeifer-mail.de>
* Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de>
* Eran Ifrah <eran.ifrah@gmail.com>
* Esben Mose Hansen, Ange Optimization ApS
* Geoffrey Viola <geoffrey.viola@asirobots.com>
* Google Inc
* Gregor Jasny
* Helio Chissini de Castro <helio@kde.org>
* Ilya Lavrenov <ilya.lavrenov@itseez.com>
* Insight Software Consortium <insightsoftwareconsortium.org>
* Jan Woetzel
* Julien Schueller
* Kelly Thompson <kgt@lanl.gov>
* Laurent Montel <montel@kde.org>
* Konstantin Podsvirov <konstantin@podsvirov.pro>
* Mario Bensi <mbensi@ipsquad.net>
* Martin Gräßlin <mgraesslin@kde.org>
* Mathieu Malaterre <mathieu.malaterre@gmail.com>
* Matthaeus G. Chajdas
* Matthias Kretz <kretz@kde.org>
* Matthias Maennich <matthias@maennich.net>
* Michael Hirsch, Ph.D. <www.scivision.co>
* Michael Stürmer
* Miguel A. Figueroa-Villanueva
* Mike Jackson
* Mike McQuaid <mike@mikemcquaid.com>
* Nicolas Bock <nicolasbock@gmail.com>
* Nicolas Despres <nicolas.despres@gmail.com>
* Nikita Krupen'ko <krnekit@gmail.com>
* NVIDIA Corporation <www.nvidia.com>
* OpenGamma Ltd. <opengamma.com>
* Patrick Stotko <stotko@cs.uni-bonn.de>
* Per Øyvind Karlsen <peroyvind@mandriva.org>
* Peter Collingbourne <peter@pcc.me.uk>
* Petr Gotthard <gotthard@honeywell.com>
* Philip Lowman <philip@yhbt.com>
* Philippe Proulx <pproulx@efficios.com>
* Raffi Enficiaud, Max Planck Society
* Raumfeld <raumfeld.com>
* Roger Leigh <rleigh@codelibre.net>
* Rolf Eike Beer <eike@sf-mail.de>
* Roman Donchenko <roman.donchenko@itseez.com>
* Roman Kharitonov <roman.kharitonov@itseez.com>
* Ruslan Baratov
* Sebastian Holtermann <sebholt@xwmw.org>
* Stephen Kelly <steveire@gmail.com>
* Sylvain Joubert <joubert.sy@gmail.com>
* The Qt Company Ltd.
* Thomas Sondergaard <ts@medical-insight.com>
* Tobias Hunger <tobias.hunger@qt.io>
* Todd Gamblin <tgamblin@llnl.gov>
* Tristan Carel
* University of Dundee
* Vadim Zhukov
* Will Dicharry <wdicharry@stellarscience.com>

See version control history for details of individual contributions.

The above copyright and license notice applies to distributions of
CMake in source and binary form.  Third-party software packages supplied
with CMake under compatible licenses provide their own copyright notices
documented in corresponding subdirectories or source files.

------------------------------------------------------------------------------

CMake was initially developed by Kitware with the following sponsorship:

 * National Library of Medicine at the National Institutes of Health
   as part of the Insight Segmentation and Registration Toolkit (ITK).

 * US National Labs (Los Alamos, Livermore, Sandia) ASC Parallel
   Visualization Initiative.

 * National Alliance for Medical Image Computing (NAMIC) is funded by the
   National Institutes of Health through the NIH Roadmap for Medical Research,
   Grant U54 EB005149.

 * Kitware, Inc.

Do you accept the license? [yn]: 
y
By default the CMake will be installed in:
  "/home/dhankar/CMAKE_latest_Aug2020/CMAKE_ShellScript_Install/cmake-3.18.1-Linux-x86_64"
Do you want to include the subdirectory cmake-3.18.1-Linux-x86_64?
Saying no will install in: "/home/dhankar/CMAKE_latest_Aug2020/CMAKE_ShellScript_Install" [Yn]: 
y

Using target directory: /home/dhankar/CMAKE_latest_Aug2020/CMAKE_ShellScript_Install/cmake-3.18.1-Linux-x86_64
Extracting, please wait...

Unpacking finished successfully
(base) dhankar@dhankar-1:~/CMAKE_latest_Aug2020/CMAKE_ShellScript_Install$ ls
cmake-3.18.1-Linux-x86_64  cmake-3.18.1-Linux-x86_64.sh
(base) dhankar@dhankar-1:~/CMAKE_latest_Aug2020/CMAKE_ShellScript_Install$ sudo sh cmake-3.18.1-Linux-x86_64.sh --prefix=/usr/local/ --exclude-subdir
[sudo] password for dhankar: 
CMake Installer Version: 3.18.1, Copyright (c) Kitware
This is a self-extracting archive.
The archive will be extracted to: /usr/local/

Using target directory: /usr/local/
Extracting, please wait...

Unpacking finished successfully

(base) dhankar@dhankar-1:~/CMAKE_latest_Aug2020/CMAKE_ShellScript_Install$ which cmake
/usr/local/bin/cmake
(base) dhankar@dhankar-1:~/CMAKE_latest_Aug2020/CMAKE_ShellScript_Install$ cmake --version
cmake version 3.18.1

CMake suite maintained and supported by Kitware (kitware.com/cmake).
```
#

