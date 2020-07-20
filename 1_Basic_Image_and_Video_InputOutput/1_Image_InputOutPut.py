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
##
#
args = vars(ap.parse_args())
print(args)


def png_to_jpg(img_in):
    #
    img_png = cv2.imread(img_in)
    plt.imshow(img_png)#,'gray')
    plt.show()

    cv2.imwrite('MyPic.jpg', img_png)
    # plt.imshow(img_png)#,'gray')
    # plt.show()


png_to_jpg('tsukuba_l.png')




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

