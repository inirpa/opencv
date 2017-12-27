import cv2
import numpy as np

cap = cv2.VideoCapture('H:\python\sentdex\opencv\sample.mp4')

# red = np.uint8([[[0,0,255]]])
# hsv_red = cv2.cvtColor(red,cv2.COLOR_BGR2HSV)
# print(hsv_red)

while True:
	_, frame = cap.read()
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	lower_red = np.array([0,100,100])
	upper_red = np.array([10,240,240])

	mask = cv2.inRange(hsv, lower_red, upper_red)
	res = cv2.bitwise_and(frame, frame, mask=mask)

	kernel = np.ones((5,5), np.uint8)
	erosion = cv2.erode(mask, kernel, iterations=1)
	dilation = cv2.dilate(mask, kernel, iterations=1)

	opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
	closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
	# kernel = np.ones((15,15), np.float32)/225
	# smoothed = cv2.filter2D(res, -1,kernel)
	# blur = cv2.GaussianBlur(res, (15,15) ,0)
	# median = cv2.medianBlur(res, 15)
	# bilateral = cv2.bilateralFilter(res, 15, 75, 75)

	# cv2.imshow('Orginal', frame)
	# cv2.imshow('masked', mask)
	cv2.imshow('result', res)
	# cv2.imshow('blured', smoothed)
	# cv2.imshow('gaussian blured', blur)
	# cv2.imshow('median blured', median)
	# cv2.imshow('bilateral blured', bilateral)
	# k = cv2.waitKey(1) & 0xFF
	# if k == 27:
	# 	break

	cv2.imshow('opening', opening)
	cv2.imshow('closing', closing)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cv2.destroyAllWindows()			
cap.release()

