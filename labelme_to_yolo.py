import json
import os

classes = ["obstacle", "fall zone"]

def convertImage(json_path, label_out):

  with open(json_path) as f:
      data = json.load(f)
  w = data['imageWidth']
  h = data['imageHeight']

  yolo_lines = []

  for shape in data["shapes"]:
    label = shape["label"]
    if label not in classes:
        continue

    points = shape["points"]
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]

    xmin, xmax = min(xs), max(xs)
    ymin, ymax = min(ys), max(ys)

    x_center = ((xmin + xmax) / 2) / w
    y_center = ((ymin + ymax) / 2) / h
    bw = (xmax - xmin) / w
    bh = (ymax - ymin) / h

    class_id = classes.index(label)
    yolo_lines.append(
        f"{class_id} {x_center} {y_center} {bw} {bh}"
    )

    with open(label_out, "w") as f:
        f.write("\n".join(yolo_lines))

# convertImage(
#    "dataset/images/train/image1.json",
#    "dataset/labels/train/image1.txt"
# )

convertImage("dataset/images/test/1767697042.json", "dataset/label/test/1767697042.txt")