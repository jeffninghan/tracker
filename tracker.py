if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

import cv2
import numpy as np
import time

def is_marker_present(mask, center, threshold):
    average_mask_value = 0.0
    for row in xrange(0, len(mask)):
        for col in xrange(0, len(mask[0])):
            average_mask_value += mask[row][col]
    elements = len(mask) * len(mask[0])
    if elements != 0:
        average_mask_value /= float(255 * elements)
    else:
        average_mask_value = 0
    return (average_mask_value > threshold, average_mask_value)

# given the command image file, give to ocr and text result.
def recognize_command(filename):

    return

# given a command, execute the corresponding function.
def execute_command(command):

    return

def append_point_to_command_image(command_image, mm, lastx, lasty, start_plot):
    cx, cy = get_moment_center(mm)
    if cx is not None:
        if start_plot:
            cv2.line(command_image, (lastx,lasty),(cx,cy),(0,255,255),3)
            lastx = cx
            lasty = cy
        else:
            start_plot = 1
    return command_image, cx, cy, start_plot

def get_moment_center(mm):
    if mm['m00'] != 0:
        cx = int(mm['m10']/mm['m00'])
        cy = int(mm['m01']/mm['m00'])
        if cx == 0 or cy == 0:
            return (None, None)
        return (cx, cy)
    else:
        return (None, None)

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

    return (bitmask_array, mask)

def calibrate():

    # define range of blue color in HSV
    LOWER_BLUE = [110,50,50]
    UPPER_BLUE = [130,255,255]
    LOWER_GREEN = [50, 50, 50] # LOWER_GREEN = [50, 50, 50]
    UPPER_GREEN = [110, 255, 255] # UPPER_GREEN = [110, 255, 255]
    lower_color = np.array(LOWER_GREEN, dtype=np.uint8)
    upper_color = np.array(UPPER_GREEN, dtype=np.uint8)

    # Threshold the HSV image to get only blue colors
<<<<<<< HEAD
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

=======
    start_time = time.time()
    while True:
        _, frame = cap.read()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, lower_color, upper_color)
        mm = cv2.moments(mask)
        cv2.imshow('frame',frame)
        if (time.time() - start_time) > 3:
            break

    present, threshold = is_marker_present(mask, mm, 0)
    cv2.destroyAllWindows()
    return threshold

def run(cx, cy, lastx, lasty, start_plot, threshold):
    reading = False
    start_time = time.time()
    line_frame = None
    bitmask_array = None
    while True:
        # Convert BGR to HSV
        _, frame = cap.read()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # define range of blue color in HSV
        LOWER_BLUE = [110,50,50]
        UPPER_BLUE = [130,255,255]
        LOWER_GREEN = [50, 50, 50] # LOWER_GREEN = [50, 50, 50]
        UPPER_GREEN = [100, 255, 255]
        lower_color = np.array(LOWER_GREEN, dtype=np.uint8)
        upper_color = np.array(UPPER_GREEN, dtype=np.uint8)

        # Threshold the HSV image to get only blue colors
        mask = cv2.inRange(hsv, lower_color, upper_color)
        
        bitmask_array, mask = denoise(mask, bitmask_array, start_plot)
        mm = cv2.moments(mask)

        present, value = is_marker_present(mask, mm, threshold)
        if present and not reading:
            print 'present but not reading with image value: ' + str(value)
            reading = True
            _, line_frame = cap.read()
            line_frame, lastx, lasty, start_plot = append_point_to_command_image(line_frame, mm, lastx, lasty, start_plot)
            # continue reading

        elif present and reading:
            print 'present and reading with image value: ' + str(value)
            reading = True
            line_frame, lastx, lasty, start_plot = append_point_to_command_image(line_frame, mm, lastx, lasty, start_plot)
            # start reading
        elif not present and reading:
            print 'not present and reading with image value: ' + str(value)
            start_plot = 0
            reading = False
            # stop reading and save file
            # run tesseract and get output
        else:
            print 'not present and not reading with image value: ' + str(value)
            start_plot = 0
            reading = False
            # dont do anything

        time.sleep(0.1)

        res = cv2.bitwise_and(frame,frame, mask= mask)

        cv2.imshow('frame',frame)
        cv2.imshow('mask',mask)
        cv2.imshow('res',res)
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break

        if line_frame is not None:
            cv2.imshow('line', line_frame)
        if int(time.time()-start_time) > 10:
            break

        time.sleep(0.1)

if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    HUE_SCALE_FROM_PAINT_TO_PYTHON = 0.75

    cx = 0
    cy = 0
    lastx = 0
    lasty = 0
    start_plot = 0

    print 'starting calibration'
    threshold = calibrate()   # calibration should also find optimal hsv values for marker (maybe do background without marker and then with marker)
    print 'ending calibration with threshold set to: ' + str(threshold)
    run(cx, cy, lastx, lasty, start_plot, threshold)


    # calibration
    # run
        # sense the color and only read if it is there
        # be able to start and stop reading points
        # save command files and remove once command is written
        # give command files to tesseract and get output 
>>>>>>> origin/master
