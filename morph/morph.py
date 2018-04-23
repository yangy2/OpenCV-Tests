import numpy as np
import cv2

##img = cv2.imread("noise.png")
##ret, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
##
##kernel = np.ones((9,9), np.uint8)
##
##erosion = cv2.erode(img, kernel, iterations = 1)
##dilation = cv2.dilate(img, kernel, iterations = 1)
##
##cv2.imshow("erode.png", erosion)
##cv2.imshow("dilate.png", dilation)

img = cv2.imread("people.png")
ret, thresh1 = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY)

kernel = np.ones((1,1), np.uint8)

opening = cv2.morphologyEx(thresh1, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(thresh1, cv2.MORPH_CLOSE, kernel)

cv2.imshow("frame", img)
cv2.imshow("opening", opening)
cv2.imshow("closing", closing)

#wait for key press
cv2.waitKey(0)
cv2.destroyAllWindows()
