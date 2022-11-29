# Read in video/screen data
import cv2 as cv
import numpy as np
from Shapes import DefineShapes
from window_capture import WindowCapture
import testing

# initialize WindowCapture
wincapture = WindowCapture('Untitled - Paint') # name of the actual application we want to read in 
wincapture.list_window_names()
loop_time = testing.GetTime() # start timer

screenshot = wincapture.get_screenshot() # get first screenshot to setup window for interaction
cv.imshow('Main',   screenshot) # continue redrawing on the same window. 

while(True):
  screenshot = wincapture.get_screenshot() # continually get screenshots
  #screenshot = cv.imread("Super Hexagon.png", cv.IMREAD_GRAYSCALE)
  screenshot = cv.cvtColor(screenshot, cv.COLOR_BGR2GRAY)
  if cv.waitKey(1) == ord('r'):
    DefineShapes(screenshot)
    cv.imshow('Main',   screenshot) # continue redrawing on the same window. 
    
  testing.PrintTime(loop_time) # print the amount of time elapsed
  loop_time = testing.GetTime() # reset timer

  # If  user presses the 'q' key, terminate loop
  if cv.waitKey(1) == ord('q'):
    cv.destroyAllWindows() # close all windows
    break

