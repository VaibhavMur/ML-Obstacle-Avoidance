import cv2
import os

import imageProcessing  # Getting detected obstacles

# Current start_pt = (W/2, H/2) but as a tuple.
# Similarly, end_pt = (W/2, 0) but as a tuple.


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

img = cv2.imread(latestImage)

gaps = []
space = []
cost = []

# costFormula = spaceBetween * 0.9 + (W/2 - distanceFromCenter) * 1.5
# Finding gaps between osbtacles:

gaps.append(abs((obstacle_boxes[0][0] - 0)) / 2)
space.append(gaps[0] - 0)
distFromCenter = abs(960 - space[0])
spaceBetween = gaps[0] * 2
cost.append(int(spaceBetween * 0.9 + distFromCenter * 1.5))
i = 1

# Go through all obstacles and calculate gaps, space, cost
while(i < len(obstacle_boxes) ):
  gaps.append(abs((obstacle_boxes[i][0] - obstacle_boxes[i-1][2])) / 2)
  space.append(gaps[i] - obstacle_boxes[i-1][2])
  distFromCenter = abs(960 - space[i])
  spaceBetween = gaps[i] * 2
  cost.append(int(spaceBetween * 0.9 + distFromCenter * 1.5))
  i=i+1
intList = [int(e) for e in cost]
maxCost = intList.index(max(intList))
print("MAXIMUM:",max(cost))
print("Max Cost:", maxCost)
print("Gaps:", gaps)
x_axis = gaps[maxCost]
print("Reactive Point X-axis:", x_axis)

cv2.circle(img, (int(x_axis), int(y_axis)), 10, (255, 0, 0), -1)

cv2.imshow("Reactive Point", img)
cv2.waitKey(0)
