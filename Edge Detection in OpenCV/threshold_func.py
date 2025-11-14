import cv2

img = cv2.imread("Edge Detection in OpenCV/man.png", cv2.IMREAD_GRAYSCALE)

ret, thresh_img = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)

cv2.imshow("Original Image", img)
cv2.imshow("Thresholded Image", thresh_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""
90 - 0 black
130 - 255 white
180 - 255 white
50 - 0 black

100, 120, 150
best
"""