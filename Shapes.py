import cv2 as cv
def DefineShapes(screenshot):
  ret , thrash = cv.threshold(screenshot, 240 , 255, cv.CHAIN_APPROX_NONE)
  contours , hierarchy = cv.findContours(thrash, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

  for contour in contours:
      approx = cv.approxPolyDP(contour, 0.01* cv.arcLength(contour, True), True)
      cv.drawContours(screenshot, [approx], 0, (0, 255, 0), 5)
      x = approx.ravel()[0]
      y = approx.ravel()[1] - 5
      if len(approx) == 3:
          cv.putText( screenshot, "Triangle", (x, y), cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 255, 0) )
      elif len(approx) == 4 :
          x, y , w, h = cv.boundingRect(approx)
          aspectRatio = float(w)/h
          print(aspectRatio)
          if aspectRatio >= 0.95 and aspectRatio < 1.05:
              cv.putText(screenshot, "square", (x, y), cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 255, 0))
          else:
              cv.putText(screenshot, "rectangle", (x, y), cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 255, 0))
      elif len(approx) == 5 :
          cv.putText(screenshot, "pentagon", (x, y), cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 255, 0))
      elif len(approx) == 10 :
          cv.putText(screenshot, "star", (x, y), cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 255, 0))
      else:
          cv.putText(screenshot, "circle", (x, y), cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 255, 0))