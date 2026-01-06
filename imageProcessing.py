from ultralytics import YOLO
import cv2
import os

# Download latest version

# List all image filenames (specifically the time) in the images directory
def imageProcessing(): 
  files = [
      os.path.join("images", f)
      for f in os.listdir("images")
      if f.endswith((".png", ".jpg", ".jpeg"))
  ]
  latestImage = max(
      files, 
      key=lambda f: int(os.path.splitext(os.path.basename(f))[0])
  )

  model = YOLO("runs/detect/obstacle-avoidance-model/weights/best.pt")

  img = cv2.imread(latestImage)
  # img = cv2.imread("750316.jpg")

  results = model(img)

  annotated = results[0].plot()
  cv2.imshow("Detections", annotated)
  cv2.waitKey(0)

if __name__ == "__main__":
  imageProcessing()