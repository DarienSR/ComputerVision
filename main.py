# Read in video/screen data
import cv2 as cv
from Shapes import DefineShapes
from Segmentation import Segmentation
from window_capture import WindowCapture
from GUI import GUI
import testing

# initialize WindowCapture
wincapture = WindowCapture('Untitled - Paint') # name of the actual application we want to read in 
loop_time = testing.GetTime() # start timer

gui = GUI() # create gui class
gui.create_window() # create the actual window

while(True):
  # If  user presses the 'q' key, terminate loop
  if cv.waitKey(1) == ord('q'):
    cv.destroyAllWindows() # close all windows
    break

  screenshot = wincapture.get_screenshot() # continually get screenshots
  screenshot = cv.cvtColor(screenshot, cv.COLOR_BGR2GRAY) # convert screenshot into grayscale

  DefineShapes(screenshot) # determine and label shapes
  result_image = Segmentation(screenshot, gui) # segment shapes based on pixel color

  cv.imshow('Main', result_image) # output result and continue redrawing on the same window. 

  testing.PrintTime(loop_time) # print the amount of time elapsed
  loop_time = testing.GetTime() # reset timer


