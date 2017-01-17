import cv2
import numpy as np
from matplotlib import pyplot as plt

path = "/home/damien/Documents/digitalimaging"
name = "beachgirl"#raw_input("Name of the image : ")
extension = ".jpg"#raw_input("Extension of the image : ")

img = cv2.imread(path+"/pic/"+name+extension)

mask = np.zeros(img.shape[:2],np.uint8)

bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)

rect = (400,150,800,500)
cv2.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)

mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
img = img*mask2[:,:,np.newaxis]

cv2.imwrite(path+"/silouhetted/"+name+extension, img)