import cv2 as cv
def DefineShapes(screenshot):
  thrash = cv.threshold(screenshot, 240 , 255, cv.CHAIN_APPROX_NONE)[1] # returns two values, we want the second
  contours = cv.findContours(thrash, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)[0] # returns two values, we want the first

  for contour in contours:
      approx = cv.approxPolyDP(contour, 0.01* cv.arcLength(contour, True), True) # sides of the shape
      cv.drawContours(screenshot, [approx], 0, (0, 255, 0), 1)
      x = approx.ravel()[0]
      y = (approx.ravel()[1] - 5)
      if len(approx) == 3:
          cv.putText(screenshot, "Triangle", (x, y), cv.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0))
      elif len(approx) == 4 : # 4 sides, either a square or rectnagle. If all four sides are somewhat equal, then it is a square.
          x, y, w, h = cv.boundingRect(approx)
          aspectRatio = float(w)/h
          if aspectRatio >= 0.95 and aspectRatio < 1.05:
              cv.putText(screenshot, "Square", (x, y), cv.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0))
          else:
              cv.putText(screenshot, "Rectangle", (x, y), cv.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0))
      elif len(approx) == 5 :
          cv.putText(screenshot, "Pentagon", (x, y), cv.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0))
      elif len(approx) == 10 :
          cv.putText(screenshot, "Star", (x, y), cv.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0))
      else:
          cv.putText(screenshot, "Circle", (x, y), cv.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0))