# Read in video/screen data
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from Shapes import DefineShapes
from Segmentation import Segmentation
from window_capture import WindowCapture
import testing

# initialize WindowCapture
wincapture = WindowCapture('Untitled - Paint') # name of the actual application we want to read in 
wincapture.list_window_names()
loop_time = testing.GetTime() # start timer



while(True):
  screenshot = wincapture.get_screenshot() # continually get screenshots
  #screenshot = cv.imread("Super Hexagon.png", cv.IMREAD_GRAYSCALE)
  screenshot = cv.cvtColor(screenshot, cv.COLOR_BGR2GRAY)

  DefineShapes(screenshot)
  result_image = Segmentation(screenshot)

  #testing.PrintTime(loop_time) # print the amount of time elapsed
  #loop_time = testing.GetTime() # reset timer

  cv.imshow('Main',   result_image) # continue redrawing on the same window. 
  # If  user presses the 'q' key, terminate loop
  if cv.waitKey(1) == ord('q'):
    cv.destroyAllWindows() # close all windows
    break

