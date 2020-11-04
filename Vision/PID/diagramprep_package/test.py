from diagramprep.PidImage import PidImage
from diagramprep.PidImageProcessor import PidImageProcessor
import logging

logging.basicConfig(level=logging.DEBUG)


f = open(r"C:\Users\\Downloads\testfile.txt",'r')
image_bytes_str = f.read()

pidImage = PidImage(image_bytes_str)

imageProcessor = PidImageProcessor(pidImage)
imageProcessor.process__image()
