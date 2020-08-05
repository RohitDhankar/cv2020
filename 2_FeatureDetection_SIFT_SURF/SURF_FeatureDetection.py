#Source = https://github.com/opencv/opencv/blob/3.4/samples/python/tutorial_code/features2D/feature_detection/SURF_detection_Demo.py

from __future__ import print_function
import cv2 as cv
import numpy as np
import argparse

parser = argparse.ArgumentParser(description='Code for Feature Detection tutorial.')
parser.add_argument('--img_in', help='Path to input image.', default='box.png')
args = parser.parse_args()

# path to image Own DIR = /home/dhankar/_dc_all/cv20/cv2020/2_Feature Detection_SIFT_SURF/Input_Images/box.png
# python SURF_FeatureDetection.py --img_in ./Input_Images/box.png

src = cv.imread(cv.samples.findFile(args.img_in), cv.IMREAD_GRAYSCALE)
if src is None:
    print('Could not open or find the image:', args.img_in)
    exit(0)

#-- Step 1: Detect the keypoints using SURF Detector
minHessian = 400
detector = cv.xfeatures2d_SURF.create(hessianThreshold=minHessian)
keypoints = detector.detect(src)

#-- Draw keypoints
img_keypoints = np.empty((src.shape[0], src.shape[1], 3), dtype=np.uint8)
cv.drawKeypoints(src, keypoints, img_keypoints)

#-- Show detected (drawn) keypoints
cv.imshow('SURF Keypoints', img_keypoints)

cv.waitKey()


"""
# If we do not have OpenCV compiled from source - then we will not have access to SIFT / SURF and other Patented Algo

(tensorflow_gpuenv) dhankar@dhankar-1:~/_dc_all/cv20/cv2020/2_Feature Detection_SIFT_SURF$ python SURF_FeatureDetection.py --img_in ./Input_Images/box.png
Traceback (most recent call last):
  File "SURF_FeatureDetection.py", line 21, in <module>
    detector = cv.xfeatures2d_SURF.create(hessianThreshold=minHessian)
AttributeError: module 'cv2.cv2' has no attribute 'xfeatures2d_SURF'

To use SIFT or SURF - "must compile OpenCV from sources" 
# REFER HERE -- https://github.com/skvark/opencv-python
# ROS  also restricts SIFT and SURF from OpenCV - https://answers.ros.org/question/34557/opencv-patent/
"must compile OpenCV from sources" https://github.com/skvark/opencv-python/issues/126
"""
