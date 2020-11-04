from .PidImage import PidImage
from .Processor import Processor
import time
import base64
import numpy as np
import logging 
from PIL import Image
from io import BytesIO
import cv2 


class PidImageProcessor():

    pidImage: PidImage = None

    def __init__(self, pidImage: PidImage,max_hough_circles:int=500):
        self.pidImage = pidImage
         
    def process__image(self):
        start_time = time.time()
        circles = self.__contour_match() # Retrieve Hough Circles    
        logging.info("Contour Match--- %s seconds ---" % (time.time() - start_time))
        
        
    def __contour_match(self):    
        img2 = self.pidImage.image.copy()    
        kernel = np.ones((2,2), np.uint8) 

        img2 = cv2.GaussianBlur(img2, (5, 5), 5)

        img2 = cv2.dilate(img2, kernel, iterations=2)
        ret, img2 = cv2.threshold(img2, 220, 255, cv2.THRESH_TOZERO)
        gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

        circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, dp=3, minDist=10,
                                param1=50, param2=90,
                                minRadius=10, maxRadius=20)

        if circles is not None:
            circles = np.uint16(np.around(circles))

        return circles  
  
    
    def ocr_circles(img, circles):

        kernel = np.ones((3,3), np.uint8) 
        kernel_sharpening=np.array([[-1,-1,-1], [-1, 15,-1],[-1,-1,-1]])

        text = ""
        buffer=0
        i = 0

        for c1 in circles[0, :]:     
            r = c1[2]+buffer
            x = c1[0]-r
            y= c1[1]-r
            x2= c1[0]+r
            y2= c1[1]+r
            src_cp = img[y:y2, x:x2]    

    
            h_ratio = 110/src_cp.shape[0]
            w_ratio=110/src_cp.shape[1]

            src_cp = cv2.resize(src_cp,(int(src_cp.shape[1] * w_ratio),int(src_cp.shape[0] * h_ratio)))

            src_cp = cleancircle(src_cp)
            src_cp = cv2.dilate(src_cp, kernel, iterations=1)

            ret, src_cp = cv2.threshold(src_cp, 210, 255, cv2.THRESH_TOZERO)
            src_cp = cv2.fastNlMeansDenoisingColored(src_cp,None,6,6,7,21)
            sharpened=cv2.filter2D(src_cp,-1,kernel_sharpening)
            sharpened = remove_horizontal_lines(sharpened)
            
            text = text + " " + get_text_from_img(sharpened) 
            
            i = i + 1
        
        return text