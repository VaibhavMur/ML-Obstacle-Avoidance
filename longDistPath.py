from CV_cam import camFeed
import cv2

W = 1920
H = 1080
start_pt = (W // 2, H//2)
end_pt = (W// 2, 0)
color = (0, 255, 0)

image_path = "images/1768551558.png"

def longDistPath():
  img = cv2.imread(image_path)
  cv2.line(img, start_pt, end_pt, color, 2)
  cv2.imshow("Long Distance Path", img)
  cv2.waitKey(0)

if __name__ == "__main__":
  longDistPath()

longDistPath()
