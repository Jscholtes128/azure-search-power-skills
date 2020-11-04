import re
import time
import pytesseract


def get_text_from_img(img):

    #--oem 1 --psm 3 -l eng --oem 1 ''
    txt = pytesseract.image_to_string(img,lang='eng',config='--psm 6')

    ### old if re.search("^[a-zA-Z]+\\n[0-9_]+$",txt) != None:
    txt = txt.replace("\n","-") ## set-up tags from instrument contours
    removeSpecialChars = txt.translate({ord(c): " " for c in "!@#$%^&*()[]{};:,./<>?\|`~=_+\"\\"})

    return removeSpecialChars