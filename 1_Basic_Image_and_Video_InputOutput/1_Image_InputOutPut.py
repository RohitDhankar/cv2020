# Source = https://docs.opencv.org/3.4/d3/d96/tutorial_basic_geometric_drawing.html

import cv2
import numpy as np
from matplotlib import pyplot as plt


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

