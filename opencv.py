import cv2 as cv

img = cv.imread("assert/LightShader.png")
cv.imshow("LightShader", img)

cv.waitKey(0)