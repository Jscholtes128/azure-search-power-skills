from .DiagramCircle import DiagramCircle
from typing import List
from PIL import Image
from io import BytesIO
import cv2
import time
import base64
import numpy as np
import logging 

class PidImage():
    
    circles: List[DiagramCircle] = []
    image: [] = []

    def __init__(self,image_bytes_str: str,encoding:str='utf-8'):

        start_time = time.time()   
        image_string_b = image_bytes_str.encode(encoding)       
        image_bytes = base64.b64decode(image_string_b)
        logging.info("Image Bytes Len: " + str(len(image_bytes)))

        pil_image = Image.open(BytesIO(image_bytes))
        open_cv_image = np.array(pil_image)	        
        self.image = open_cv_image[:, :, ::-1].copy() 
        logging.info("Image Read--- %s seconds ---" % (time.time() - start_time)) 

    #@property
    #def circles(self) -> List[DiagramCircle]:
    #    return this.circles