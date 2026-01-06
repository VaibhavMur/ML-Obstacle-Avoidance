# This program will take pictures from the webcam that will then be used by the algorithm to determine obstacle from landscape
# import numpy as np

import cv2
import time
import os

def camFeed():
  cap = cv2.VideoCapture(0)
  ret, frame = cap.read()

  foldername = "images"
  os.makedirs(foldername, exist_ok=True)
  cv2.imshow("Camera Feed", frame)
  filename = f"{int(time.time())}.png"
  fullPath = os.path.join(foldername, filename)
  cv2.imwrite(fullPath, frame)
  if cv2.waitKey(0) & 0xFF == ord('q') :
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
  camFeed()