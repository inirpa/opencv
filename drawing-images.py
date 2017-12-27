import numpy as np
import cv2

img = cv2.imread('watch.jpg', cv2.IMREAD_COLOR)

cv2.line(img,(0,0),(150,150),(255,255,255),5)
cv2.rectangle(img,(15,15),(200,150),(0,255,0),5)
cv2.circle(img,(50,50),50,(0,0,255),1)

pts = np.array([[10,5],[45,90],[90,50],[8,70],[19,67],],np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img, [pts], True, (0,255,255),3)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'Open CV Font',(0,130), font, 1, (200,200,200), 1, cv2.LINE_AA)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()