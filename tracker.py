import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0)

HUE_SCALE_FROM_PAINT_TO_PYTHON = 0.75

# s, img = cam.read()
# if s:
#     cv2.namedWindow('cam-test', cv2.CV_WINDOW_AUTOSIZE)
#     cv2.imshow('cam-test', img)
#     cv2.waitKey(0)
#     cv2.destroyWindow('cam-test')
# def get_filtered_images(cap):

#     # Take each frame
#     _, frame = cap.read()

#     # Convert BGR to HSV
#     hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

#     # define range of blue color in HSV
#     LOWER_BLUE = [110,50,50]
#     UPPER_BLUE = [130,255,255]
#     LOWER_GREEN = [50, 50, 50]
#     UPPER_GREEN = [110, 255, 255]
#     lower_color = np.array(LOWER_GREEN, dtype=np.uint8)
#     upper_color = np.array(UPPER_GREEN, dtype=np.uint8)

#     # Threshold the HSV image to get only blue colors
#     mask = cv2.inRange(hsv, lower_color, upper_color)

#     # Bitwise-AND mask and original image
#     res = cv2.bitwise_and(frame,frame, mask= mask)
#     return res

#     # cv2.imshow('frame',frame)
#     # cv2.imshow('mask',mask)
#     # cv2.imshow('res',res)
    # k = cv2.waitKey(5) & 0xFF
_, line_frame = cap.read()
start_time = time.time()

cx = 0
cy = 0
lastx = 0
lasty = 0
start_plot = 0
while(1):

    # Convert BGR to HSV
    _, frame = cap.read()
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
    
    mm = cv2.moments(mask)
    if mm['m00'] != 0:
        cx = int(mm['m10']/mm['m00'])
        cy = int(mm['m01']/mm['m00'])
	    print (cx, cy)
    	if lastx > 0 and lasty > 0 and cx > 0 and cy > 0 and start_plot:
	        cv2.line(line_frame,(lastx,lasty),(cx,cy),(0,255,255),3)
    	lastx = cx
	    lasty = cy
	    start_plot = 1
        
    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
    if int(time.time()-start_time) > 5:
        cv2.imshow('line', line_frame)
        cv2.imwrite('line_frames.png', line_frame)

#cv2.destroyAllWindows()

#for i in xrange(0, 10):
# while True:
#     res = get_filtered_images(cap)
#     cv2.imshow('res',res)
#     time.sleep(1)
