import cv2
# to use system call so u can use call the chosen image with the sript
import sys
from PIL import Image


# Get user supplied values
imagePath = 'hugo.jpg'
cascPath = 'haarcascade_frontalface_default.xml'

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)

# Read the image
image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30)
    #flags = cv2.CV_HAAR_SCALE_IMAGE
)

print("Found {0} faces!".format(len(faces)))

# x,y en haut a gauche
# h height going down
# w longuer going East
i=Image.open("hugo.jpg")

(column, line) = i.size

list_tuple = []


# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    print "################"
    print "x is %d" %x
    print "y is %d" %y
    print "wight is %d" %w
    print "height is %d" %h
    print "\n\n"
    xhalf = x/3
    yhalf = y/2
    cv2.rectangle(image, (x, y), (x+w+10, y+h+20), (0, 255, 0), 2)
    list_tuple.append((x,y,w,h))


for a in range (0,line):
	for b in range (0,column):
		i.putpixel((b,a),(0,0,0))

for tuples in list_tuple:
	xx=tuples[0]
	yy=tuples[1]
	wight=tuples[2]
	height=tuples[3]
	for temp1 in range (yy+20,yy+height-20):
		for temp2 in range (xx+20,xx+wight-20):
			i.putpixel((temp2,temp1),(255,255,255))



cv2.imshow("Faces found", image)
cv2.waitKey(0)
i.show()

