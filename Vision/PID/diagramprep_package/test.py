from diagramprep.PidImage import PidImage
from diagramprep.PidImageProcessor import PidImageProcessor
import logging

logging.basicConfig(level=logging.DEBUG)


f = open(r"C:\Users\\Downloads\testfile.txt",'r')
image_bytes_str = f.read()

pidImage = PidImage(image_bytes_str)
imageProcessor = PidImageProcessor(pidImage, debug=True)
imageProcessor.process__image(circle_index=1,ocr_image=False)

filename = r"C:\Users\\Documents\image_processing_test\testfiles\test"

for i in range(0,len(pidImage.debugImages)):
    pidImage.save_image(filename+"_{}.jpg".format(i),debug_index=i)

pidImage.save_image(filename+".jpg")

print('DONE..')