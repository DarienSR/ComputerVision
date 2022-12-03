import cv2 as cv
import numpy as np

def Segmentation(screenshot, gui):
  screenshot = cv.cvtColor(screenshot, cv.COLOR_GRAY2RGB)
  twoDimage = screenshot.reshape((-1,3))
  twoDimage = np.float32(twoDimage)
  criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 10, 1.0)
  K = gui.get_kVal() 
  attempts = 10

  ret, label, center = cv.kmeans(twoDimage, K, None, criteria, attempts, cv.KMEANS_PP_CENTERS)
  center = np.uint8(center)
  res = center[label.flatten()]
  result_image = res.reshape((screenshot.shape))
  return result_image