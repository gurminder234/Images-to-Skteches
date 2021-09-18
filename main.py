import cv2
img = cv2.imread('1.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
invert = 255 - gray
blur = cv2.GaussianBlur(invert,(21,21),0)
inverted = 255 - blur
pencil = cv2.divide(gray,inverted,scale = 256.0)
cv2.imshow("original",img)
cv2.imshow('New',pencil)
cv2.waitKey(0)