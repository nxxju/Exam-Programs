import cv2

x = "Path of image"
y = cv2.imread(x)

cv2.imshow("My Picture", y)
cv2.waitkey(0)
