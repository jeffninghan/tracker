import cv2
import numpy as np

cap = cv2.VideoCapture(0)

HUE_SCALE_FROM_PAINT_TO_PYTHON = 0.75

while(1):

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    LOWER_BLUE = [110,50,50]
    UPPER_BLUE = [130,255,255]
    LOWER_GREEN = [50, 50, 50]
    UPPER_GREEN = [110, 255, 255]
    lower_color = np.array(LOWER_GREEN, dtype=np.uint8)
    upper_color = np.array(UPPER_GREEN, dtype=np.uint8)

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_color, upper_color)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()