
##/home/dhankar/_dc_all/20_8/cv20/cv2020
# Source = https://docs.opencv.org/3.4/d3/d96/tutorial_basic_geometric_drawing.html

import cv2
import numpy as np
from matplotlib import pyplot as plt
import argparse

# Construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,help="path to the input image")
## cv2.GaussianBlur -- width_Kernel(Positive and ODD )
ap.add_argument("-wK","--width_Kernel",type=int, required=False,help=" _width_Kernel -- cv2.GaussianBlur")
ap.add_argument("-lK","--length_Kernel",type=int, required=False,help=" _length_Kernel -- cv2.GaussianBlur")
args = vars(ap.parse_args()) #print(type(args)) #<class 'dict'>

def png_to_jpg(img_in):
    """
    $ python 1_Image_InputOutPut.py -i tsukuba_l.png
    """
    img_png = cv2.imread(img_in)
    cv2.imshow("imshow_from_cv2",img_png)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    #plt.imshow(img_png)#,'gray') #Color image loaded by OpenCV is in BGR mode. But Matplotlib displays in RGB mode.
    #plt.show()
    cv2.imwrite('MyPic.jpg', img_png)


def cropImage(img_in):
    """
    $ python 1_Image_InputOutPut.py -i tsukuba_l.png
    # grab dimensions of image and calculate - Center
    """
    img_in = cv2.imread(img_in) # <class 'numpy.ndarray'>
    # img_in -- is a 3D Numpy Array the - 3Dimensions of this image can be read as below -- (HEIGHT , WIDTH , DEPTH )
    #h = img_in.shape[:1] #- HEIGHT Only 
    #(h, w) = img_in.shape[:2] #- (HEIGHT , WIDTH)
    img_dim = img_in.shape[:3] #- (HEIGHT , WIDTH , DEPTH )
    #print(type(img_dim)) #<class 'tuple'>
    print("3Dimensions of this image are =>\n",img_dim) #(288, 384, 3)
    print("Image Size - all image pixels accounted for = ",img_in.size) #331776
    print("Image datatype =",img_in.dtype) # uint8 -  Unsigned integer (0 to 255)

def imgROI(img_in):
    """
    Region of Interest - ROI 
    """
    img_in = cv2.imread(img_in) # <class 'numpy.ndarray'>
    (h, w) = img_in.shape[:2] 
    center = (h/2, w/2)
    print("Got--H and W =",h,w)
    print("Got Center  = ",center)   
    # get center with - moments 
    # convert image to grayscale image
    gray_image = cv2.cvtColor(img_in, cv2.COLOR_BGR2GRAY)
    #print(type(gray_image)) #<class 'numpy.ndarray'>
    ret,thresh = cv2.threshold(gray_image,127,255,0)
    # calculate moments of binary image
    #TODO __Further Reads Required --- Convex Hull + Second Order Moments 
    # Udacity Video -- Image Moments - https://www.youtube.com/watch?v=AAbUfZD_09s
    # Video --  zedstatistics -   https://www.youtube.com/watch?v=ISaVvSO_3Sg&t=380s
    moments_dict = cv2.moments(thresh)
    #print(moments_dict) # <class 'dict'>
    """
    {'m00': 2770830.0, 'm10': 430124820.0, 'm01': 533346015.0, 'm20': 72156806850.0, 'm11': 83238526215.0,
     'm02': 112292708055.0, 'm30': 12979334400450.0, 'm21': 13709938313625.0, 'm12': 17450831157195.0, 
     'm03': 25023631206675.0, 'mu20': 5387152710.253998, 'mu11': 445515204.006073, 'mu02': 9631060925.302322,
      'mu30': 105672090690.0918, 'mu21': -317555138673.75354, 'mu12': -152236644448.01904, 
      'mu03': -298833283805.1328, 'nu20': 0.0007016806890122321, 'nu11': 5.802869013113001e-05, 
      'nu02': 0.0012544529233637209, 'nu30': 8.268668807049767e-06, 'nu21': -2.4848171854294823e-05, 
      'nu12': -1.1912269219021805e-05, 'nu03': -2.338321723523388e-05}

    """

    # calculate x,y coordinate of center
    cX = int(moments_dict["m10"] / moments_dict["m00"])
    print("--COORD-X-Center-->>\n",cX) # 155
    cY = int(moments_dict["m01"] / moments_dict["m00"])
    print("--COORD-Y-Center-->>\n",cY) # 192 

    #
    # w1 = int(w/2:w/2 + 50)
    # h1 = int(h/2:h/2 + 50)
    # print(w1)
    #print("GOT h1 ---AAA----------",h1)
    # w2 = int(w/2)
    got_roi_1 = img_in[1:190,1:190]
    got_roi_2 = img_in[60:390,60:390]
    got_roi_3 = img_in[155:390,192:390]

    cv2.imshow("sample_roi_1",got_roi_1)
    cv2.imshow("sample_roi_2",got_roi_2)
    cv2.imshow("sample_roi_3",got_roi_3)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    #print("Large 3XD_Array is printed Dont Not reqd--\n",got_roi) #(288, 384, 3)
    cv2.imwrite('roi_1.png',got_roi_1)
    cv2.imwrite('roi_2.png',got_roi_2)
    cv2.imwrite('roi_3.png',got_roi_3)
    
    img_dim_1 = got_roi_1.shape[:3] #- (HEIGHT , WIDTH , DEPTH )
    img_dim_2 = got_roi_2.shape[:3] #- (HEIGHT , WIDTH , DEPTH )
    print("roi_img_1 Dimensions are = ",img_dim_1) #(288, 384, 3)
    print("roi_img_2 Dimensions are = ",img_dim_2) #(288, 384, 3)

def getIndlPixels(img_in):
    crop_px = img_in[100,100]
    print("  " *90)
    print(type(crop_px))
    plt.imshow(crop_px)#,'gray')
    #plt.show()


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

if __name__ == '__main__':
    #png_to_jpg('tsukuba_l.png')
    png_to_jpg(args["image"])
    cropImage(args["image"])
    imgROI(args["image"])    

