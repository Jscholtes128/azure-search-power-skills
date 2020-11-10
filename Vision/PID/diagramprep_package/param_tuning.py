from diagramprep.PidImage import PidImage
from diagramprep.PidImageProcessor import PidImageProcessor
import logging
import itertools
from skimage.measure import compare_ssim, compare_mse
import cv2 

logging.basicConfig(level=logging.DEBUG)


params = {
    'hough_blurLevel': range(5,15,2),
    'hough_minDist': range(20,100,5),
    'hough_param2': range(110,120,1),
    'hough_param1': range(30,100,2)
}

def myfunc(**args):
    print(args)

f = open(r"C:\Users\\Downloads\testfile.txt",'r')
image_bytes_str = f.read()

pidImage = PidImage(image_bytes_str)
imageProcessor = PidImageProcessor(pidImage,max_hough_circles=40,min_hough_circles=20, debug=True)

filename = r"C:\Users\\Documents\image_processing_test\tune\test"
testing_files = r"C:\Users\\Documents\image_processing_test\baseline.jpg"
orig_img =  cv2.imread(testing_files)
scores = []

keys = list(params)
for values in itertools.product(*map(params.get, keys)):
    print(dict(zip(keys, values)))
    imageProcessor.process__image(hough_maxRadius=50,**dict(zip(keys, values)))

    if len(pidImage.diagramCircles) > 20 and len(pidImage.diagramCircles) < 40:
        (score, diff) = compare_ssim(orig_img, pidImage.debugImages[0], full=True,multichannel=True)
        print("SSIM Score: {}".format(score))
        scores.append(score)
        if score > .998:
            pidImage.save_image(filename+"_{}_{}_{}_{}.jpg".format(*values),debug_index=0)
            


print("Max score {} Min score {} Scores {}".format(max(scores),min(scores),len(scores)))

print('DONE..')

