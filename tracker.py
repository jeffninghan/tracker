import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0)

HUE_SCALE_FROM_PAINT_TO_PYTHON = 0.75

_, line_frame = cap.read()
start_time = time.time()

cx = 0
cy = 0
lastx = 0
lasty = 0
start_plot = 0

# parameters for denoising

def denoise(mask, bitmask_array, start_plot):
    # parameters
    num_frames = 5
    denoising_threshold = 255

    # initialize array
    if start_plot == 0:
        bitmask_array = np.empty([num_frames,len(mask),len(mask[0])]) # initialize bitmask_array

    # shift frames/elements in bitmask_array
    bitmask_array[0:num_frames-1] = bitmask_array[1:num_frames]
    bitmask_array[num_frames-1] = mask # last element is most recent
    
    # calculate avg bitmask value in past num_frames frames
    bitmask_avg = bitmask_array.sum(axis= 0)
    bitmask_avg = bitmask_avg.__div__(num_frames)
    mask = bitmask_avg.__ge__(denoising_threshold)*255
    mask = np.uint8(mask)

    # if start_plot == 0:
        # print 'bitmask_avg should have 255.5/10'
        # print bitmask_avg[num_frames-1]
        # print type(bitmask_avg)
        # print 'mask:'
        # print mask
        # print 'bitmask_array:'
        # print bitmask_array[num_frames-1]
        # print 'bitmask array lengths:'
        # print len(bitmask_array)
        # print len(bitmask_array[0])
        # print len(bitmask_array[0][0])
        # print 'mask lengths:'
        # print len(mask)
        # print len(mask[0])
        # print 'bitmask_avg true/false:'
        # print bitmask_avg.__ge__(denoising_threshold)
        # print 'bitmask_avg true/false * 255:'
        # print bitmask_avg.__ge__(denoising_threshold)*255

    return (bitmask_array, mask)

bitmask_array = None
while(1):
    # Convert BGR to HSV
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    LOWER_BLUE = [110,50,50]
    UPPER_BLUE = [130,255,255]
    LOWER_GREEN = [50, 50, 50] # LOWER_GREEN = [50, 50, 50]
    UPPER_GREEN = [110, 255, 255] # UPPER_GREEN = [110, 255, 255]
    lower_color = np.array(LOWER_GREEN, dtype=np.uint8)
    upper_color = np.array(UPPER_GREEN, dtype=np.uint8)

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_color, upper_color)

    bitmask_array, mask = denoise(mask, bitmask_array, start_plot)
    
    mm = cv2.moments(mask)
    if mm['m00'] != 0:
        cx = int(mm['m10']/mm['m00'])
        cy = int(mm['m01']/mm['m00'])
        # print (cx, cy)
    	if lastx > 0 and lasty > 0 and cx > 0 and cy > 0 and start_plot:
	        cv2.line(line_frame,(lastx,lasty),(cx,cy),(0,255,255),3)
    	lastx = cx
        lasty = cy

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
        # cv2.imwrite('line_frames.png', line_frame)

    start_plot = 1

