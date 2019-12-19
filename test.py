import cv2
import numpy as np
import matplotlib

def showImage():
    imgfile = 'D:/paintings/cave1_bg3.png'
    img = cv2.imread(imgfile,cv2.IMREAD_COLOR)

    cv2.imshow('background',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

showImage()

print(1000000000000)