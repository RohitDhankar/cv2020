##### Ubuntu - xrandr - resolution 640x480 - desktop looks zoomed in

> Been updating (basically messing around with)- CUDA , Display Drivers for the NVIDIA-GPU . Probbaly ended up breaking something . Resulting in screen display becoming == 640X480 . The ususal display was == 1366x768 OR 1280x720.   
Issue now solved - may occur again - needs to be documented. 

- Link to own YouTubeVideo - https://www.youtube.com/watch?v=ABIVvn93ido&feature=youtu.be
- Links Refered for Solution - https://askubuntu.com/a/1175928/958183

> I read through link above and realized - that maybe NVIDIA drivers need an Install . After the fresh install rebooted system - all ok as of now need to read through CRASH reports .    
Bottom of this file - apport retrace of the crash reports.   
#

> Seen below output of - xrandr , now and earlier - am checking on the crash reports - may update this README. 

```
(base) dhankar@dhankar-1:~$ cd /var/crash/
(base) dhankar@dhankar-1:/var/crash$ ls -ltr
total 180524
-rw-r----- 1 dhankar whoopsie 177635135 Jul 17 22:16 _usr_bin_qgis.bin.1000.crash
-rw-r--r-- 1 root    whoopsie    354227 Jul 24 19:02 nvidia-kernel-source-435.0.crash
-rw-r----- 1 dhankar whoopsie   6861308 Jul 25 10:36 _usr_bin_gnome-control-center.1000.crash
(base) dhankar@dhankar-1:/var/crash$ 
(base) dhankar@dhankar-1:/var/crash$ xrandr
Screen 0: minimum 8 x 8, current 1366 x 768, maximum 32767 x 32767
DP-0 disconnected (normal left inverted right x axis y axis)
DP-1 disconnected (normal left inverted right x axis y axis)
HDMI-0 disconnected (normal left inverted right x axis y axis)
HDMI-1 connected primary 1366x768+0+0 (normal left inverted right x axis y axis) 410mm x 230mm
   1366x768      59.79*+
   1280x720      60.00    59.94    50.00  
   1024x768      75.03    60.00  
   800x600       75.00    60.32    56.25  
   720x576       50.00  
   720x480       59.94  
   640x480       75.00    59.94    59.93  
(base) dhankar@dhankar-1:/var/crash$ 
```
#####

- Source - http://manpages.ubuntu.com/manpages/focal/en/man1/apport-retrace.1.html

#
```
$apport-retrace --stdout /var/crash/_usr_bin_gnome-control-center.1000.crash
ERROR: report file does not contain one of the required fields: Package
#
$apport-retrace --stdout /var/crash/nvidia-kernel-source-435.0.crash
ERROR: report file does not contain one of the required fields: CoreDump DistroRelease Architecture ExecutablePath
#

```
###### apport-retrace --gdb    -- sandbox-dir sys_crash_retrace

- Further Reads -- 
- https://askubuntu.com/questions/1160113/system-program-problem-detected
- https://askubuntu.com/questions/348790/apport-retrace-fails-with-error-report-file-does-not-contain-one-of-the-require
- https://askubuntu.com/a/348789/958183
- https://wiki.ubuntu.com/Apport?action=AttachFile&do=view&target=data-format.pdf


