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

  # model = YOLO("runs/detect/obstacle-avoidance-model/weights/best.pt")
  model = YOLO("yolov8l.pt")
  img = cv2.imread(latestImage)

  results = model(img)

  obstacle_boxes = []

  for box in results[0].boxes:
      obstacle_boxes.append(box.xyxy[0])

  # draw obstacles
  for x1, y1, x2, y2 in obstacle_boxes:
      cv2.rectangle(img,
                    (int(x1), int(y1)),
                    (int(x2), int(y2)),
                    (0, 0, 255),
                    2)
  cv2.imshow("Detections", img)
  cv2.waitKey(0)

if __name__ == "__main__":
  imageProcessing()