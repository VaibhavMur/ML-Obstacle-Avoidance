from ultralytics import YOLO

model = YOLO("yolov8l.pt")

model.train(
  data="data.yaml",
  epochs=25,
  imgsz=640,
  batch=10,
  name="obstacle-avoidance-model",
  augment=True)