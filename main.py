# Read in video/screen data
import cv2 as cv
import numpy as np
from window_capture import WindowCapture
import testing

# initialize WindowCapture
wincapture = WindowCapture('Super Hexagon') # name of the actual application we want to read in 
loop_time = testing.GetTime() # start timer
while(True):
  screenshot = wincapture.get_screenshot()
  cv.imshow('SuperHexagon AI', screenshot) # continue redrawing on the same window. 
  
  testing.PrintTime(loop_time) # print the amount of time elapsed
  loop_time = testing.GetTime() # reset timer

  # If  user presses the 'q' key, terminate loop
  if cv.waitKey(1) == ord('q'):
    cv.destroyAllWindows() # close all windows
    break

