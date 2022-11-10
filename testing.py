from time import time
def GetTime():
  return time()

def PrintTime(t):
  print('FPS: {}'.format(1 / (time() - t)))
