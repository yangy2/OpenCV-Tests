import cv2

print("here we go")

#create new image (referencing file)
image = cv2.imread("clouds.jpg")

#create new image (convert existing RGB image to greyscale)
image2 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#create new image (i have no idea what this does)
ret,image3 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

#show images
cv2.imshow("Clouds", image)
cv2.imshow("Grey Clouds", image2)
cv2.imshow("Binary Clouds", image3)

#save images
cv2.imwrite('greyclouds.jpg', image2)
cv2.imwrite('binaryclouds.jpg', image3)

#wait for key press
cv2.waitKey(0)
cv2.destroyAllWindows()
