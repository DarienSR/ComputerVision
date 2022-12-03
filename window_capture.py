import numpy as np
import win32gui, win32ui, win32con

# Code taken from: https://github.com/learncodebygaming/opencv_tutorials/blob/master/004_window_capture/windowcapture.py

# Take continuous screenshots of a specified window to mimic video stream
class WindowCapture:
  height = 0
  width = 0
  hwnd = None # window
  cropped_x = 0
  cropped_y = 0
  offset_x = 0
  offset_y = 0

  def __init__(self, window_name):
    self.hwnd = win32gui.FindWindow(None, window_name) # we are selecting the window to capture based on it's name (what appears in the upper left corner)
    if not self.hwnd:
      self.list_window_names()
      raise Exception('Window could not be found: {}'.format(window_name))

    # get the window dimensions
    window_rect = win32gui.GetWindowRect(self.hwnd)
    self.width = window_rect[2] - window_rect[0]
    self.height = window_rect[3] - window_rect[1]

    # remove the window border and titlebar from the output
    border_pixels = 8
    titlebar_pixels = 30 * 5 # * 5 gets rid of the menu on paint
    self.width = self.width - (border_pixels * 2)
    self.height = self.height - titlebar_pixels - border_pixels
    self.cropped_x = border_pixels
    self.cropped_y = titlebar_pixels

    # set the cropped coordinates offset so we can translate screenshot
    # images into actual screen positions
    self.offset_x = window_rect[0] + self.cropped_x
    self.offset_y = window_rect[1] + self.cropped_y

  def get_screenshot(self):
    # get the window image data
    wDC = win32gui.GetWindowDC(self.hwnd)
    dcObj = win32ui.CreateDCFromHandle(wDC)
    cDC = dcObj.CreateCompatibleDC()
    dataBitMap = win32ui.CreateBitmap()
    dataBitMap.CreateCompatibleBitmap(dcObj, self.width, self.height)
    cDC.SelectObject(dataBitMap)
    cDC.BitBlt((0, 0), (self.width, self.height), dcObj, (self.cropped_x, self.cropped_y), win32con.SRCCOPY)

    # convert the raw data into a format opencv can read
    #dataBitMap.SaveBitmapFile(cDC, 'debug.bmp')
    signedIntsArray = dataBitMap.GetBitmapBits(True)
    img = np.fromstring(signedIntsArray, dtype='uint8')
    img.shape = (self.height, self.width, 4)

    # free resources
    dcObj.DeleteDC()
    cDC.DeleteDC()
    win32gui.ReleaseDC(self.hwnd, wDC)
    win32gui.DeleteObject(dataBitMap.GetHandle())

    # drop the alpha channel, or cv.matchTemplate() will throw an error like:
    #   error: (-215:Assertion failed) (depth == CV_8U || depth == CV_32F) && type == _templ.type() 
    #   && _img.dims() <= 2 in function 'cv::matchTemplate'
    img = img[...,:3]

    # make image C_CONTIGUOUS to avoid errors that look like:
    #   File ... in draw_rectangles
    #   TypeError: an integer is required (got type tuple)
    # see the discussion here:
    # https://github.com/opencv/opencv/issues/14866#issuecomment-580207109
    img = np.ascontiguousarray(img)
    return img

  # Helper function to list all the open window names
  def list_window_names(self):
    def winEnumHandler(hwnd, ctx):
        if win32gui.IsWindowVisible(hwnd):
            print(hex(hwnd), win32gui.GetWindowText(hwnd))
    win32gui.EnumWindows(winEnumHandler, None)

  # translate a pixel position on a screenshot image to a pixel position on the screen.
  # pos = (x, y)
  # WARNING: if you move the window being captured after execution is started, this will
  # return incorrect coordinates, because the window position is only calculated in
  # the __init__ constructor.
  def get_screen_position(self, pos):
      return (pos[0] + self.offset_x, pos[1] + self.offset_y)
