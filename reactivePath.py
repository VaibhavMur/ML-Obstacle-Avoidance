import cv2
import os

import imageProcessing  # Getting detected obstacles

# Current start_pt = (W/2, H/2) but as a tuple.
# Similarly, end_pt = (W/2, 0) but as a tuple.

def reactivePoint():
  obstacle_boxes = imageProcessing.imageProcessing()

  # Resolution
  W = 1920
  H = 1080

  y_axis = H // 2 - 200 # Reactive point y-axis fixed at 200 pixels above center (can be changed)

  files = [
      os.path.join("images", f)
      for f in os.listdir("images")
      if f.endswith((".png", ".jpg", ".jpeg"))
  ]
  latestImage = max(
    files, 
    key=lambda f: int(os.path.splitext(os.path.basename(f))[0])
  )

  
if __name__ == "__main__":
  reactivePoint()