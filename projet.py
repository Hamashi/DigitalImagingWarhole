import cv2
import numpy as np
from matplotlib import pyplot as plt
import random
from PIL import Image

path = "/home/damien/Documents/digitalimaging"
name = "beachgirl" #raw_input("Name of the image : ")
extension = ".jpg" #raw_input("Extension of the image : ")
img = cv2.imread(path+"/pic/"+name+extension)

#################Background Cutter##################

mask = np.zeros(img.shape[:2],np.uint8)

bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)

rect = (400,150,800,500)
cv2.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)

mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
img = img*mask2[:,:,np.newaxis]

#########Changing the colors of the image###########

im = []
img_hls = cv2.cvtColor(img, cv2.cv.CV_BGR2HLS)

i=0

while i < 4:
	#extracting H L S from the image
	im.append(img_hls)
	h, l, s = cv2.split(im[i])	
	
	#Processing the foreground
	#s[np.where((img != [0,0,0]).all(axis = 2))] = 255
	h[np.where((img != [0,0,0]).all(axis = 2))] += random.randint(0,360)
	#l[np.where((img != [0,0,0]).all(axis = 2))] = random.randint(100, 200)

	#Processing for the background
	s[np.where((img == [0,0,0]).all(axis = 2))] = 255
	h[np.where((img == [0,0,0]).all(axis = 2))] = random.randint(0,360)
	l[np.where((img == [0,0,0]).all(axis = 2))] = random.randint(120, 180)

	#Merging hls
	im[i] = cv2.merge([h, l, s])
	im[i] = cv2.cvtColor(im[i], cv2.cv.CV_HLS2BGR)
	
	#Save image
	cv2.imwrite(path+"/four/%d"%i+name+extension, im[i])

	i+=1

#####################Merging the 4 images################################

while i < 4:
	im[i] = Image.open(path+name+extension)


im_size = im[1].size
new_im = Image.new('RGB', (2*im_size[0],2*im_size[1]))
new_im.paste(im[0], (0,0))
new_im.paste(im[1], (0,im_size[1]))
new_im.paste(im[2], (im_size[0],0))
new_im.paste(im[3], (im_size[0],im_size[1]))

####################Save Work###########################
new_im.save(path+"/final/"+name+extension, "PNG")
cv2.imwrite(path+"/"+name+extension, new_im)

cv2.imwrite(path+"/silouhetted/"+name+extension, img)
