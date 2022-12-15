import cv2 as cv
class GUI:
  PARAMETER_WINDOW = "Edit Parameters"
  kVal = None

  def get_kVal(self):
    print("Getting K Valuue")
    return cv.getTrackbarPos('K value', self.PARAMETER_WINDOW)

  def create_window(self):
    cv.namedWindow(self.PARAMETER_WINDOW, cv.WINDOW_NORMAL)
    cv.resizeWindow(self.PARAMETER_WINDOW, 350, 700)
    cv.createTrackbar('K value', self.PARAMETER_WINDOW, 2, 8, self.nothing)
  # need a callback function, doesnt have to do anything. Each time trackbar is changed, it calls this function.
  def nothing(position):
    pass
