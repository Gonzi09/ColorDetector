# Color Detection

import numpy as np
import cv2


# Color in BGR
yellow = [0, 255, 255]

def getlimits(color):
  c = np.uint8([[color]])

  hsvC = cv2.cvt(c, cv2.COLOR_BGR2HSV)

  lowerlimit = hsvC[0][0][0] -10, 255, 255
  upperLimit = hsvC[0][0][0] +10, 255, 255

  lowerLimit = np.array(lowerLimit, dtype=np.uint8)
  upperLimit = np.array(upperLimit, dtype=np.uint8)

  return lowerLimit, upperLimit



# Open Camera
cap = cv2.VideoCapture(0)

while True:
  ret, frame = cap.read()

  hsv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
  
  getlimits(color= yellow)

  lowerLimit, upperLimit = getlimits(color= yellow)
  mask = cv2.inRange(hsv_img, lowerLimit, upperLimit)

  cv2.imshow('frame', mask)

  if cv2.waitKey(1) & 0xFF == ord('q'):
    break


cv2.release()
cv2.destroyAllWindows()












