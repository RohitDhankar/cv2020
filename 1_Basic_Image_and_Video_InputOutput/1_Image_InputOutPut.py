# Source = https://docs.opencv.org/3.4/d3/d96/tutorial_basic_geometric_drawing.html

import cv2
import numpy as np
from matplotlib import pyplot as plt
#
import argparse

# Construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,help="path to the input image")
## cv2.GaussianBlur -- width_Kernel(Positive and ODD )
ap.add_argument("-wK","--width_Kernel",type=int, required=False,help=" _width_Kernel -- cv2.GaussianBlur")
ap.add_argument("-lK","--length_Kernel",type=int, required=False,help=" _length_Kernel -- cv2.GaussianBlur")
args = vars(ap.parse_args())
#print(type(args)) #<class 'dict'>

def png_to_jpg(img_in):
    """
    $ python 1_Image_InputOutPut.py -i tsukuba_l.png
    """
    img_png = cv2.imread(img_in)
    plt.imshow(img_png)#,'gray')
    #plt.show()
    cv2.imwrite('MyPic.jpg', img_png)
#png_to_jpg('tsukuba_l.png')
png_to_jpg(args["image"])

def cropImage(img_in):
    """
    $ python 1_Image_InputOutPut.py -i tsukuba_l.png
    # grab dimensions of image and calculate - Center
    """
    img_in = cv2.imread(img_in) # <class 'numpy.ndarray'>
    #h = img_in.shape[:1] #- HEIGHT Only 
    #(h, w) = img_in.shape[:2] #- (HEIGHT , WIDTH)
    img_dim = img_in.shape[:3] #- (HEIGHT , WIDTH , DEPTH )
    #print(type(img_dim)) #<class 'tuple'>
    print("Dimensions of Image are = ",img_dim) #(288, 384, 3)
cropImage(args["image"])


####

W = 400

def my_ellipse(img, angle):
    thickness = 2
    line_type = 8
    cv2.ellipse(img,
                (W // 2, W // 2),
                (W // 4, W // 16),
                angle,
                0,
                360,
                (255, 0, 0),
                thickness,
                line_type)

#my_ellipse()

def my_filled_circle(img, center):
    thickness = -1
    line_type = 8
    cv2.circle(img,
               center,
               W // 32,
               (0, 0, 255),
               thickness,
               line_type)

