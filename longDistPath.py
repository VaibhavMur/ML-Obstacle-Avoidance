from CV_cam import camFeed
import cv2
import os

W = 1920
H = 1080
start_pt = (W // 2, H)
end_pt = (W//2, H//2)
color = (0, 255, 0)

image_path = "images/1768551558.png"

def longDistPath():

  files = [
      os.path.join("images", f)
      for f in os.listdir("images")
      if f.endswith((".png", ".jpg", ".jpeg"))
  ]
  latestImage = max( files, 
    key=lambda f: int(os.path.splitext(os.path.basename(f))[0])
  )

  img = cv2.imread(latestImage)
  cv2.line(img, start_pt, end_pt, color, 2)
  cv2.imwrite(latestImage, img)
  cv2.imshow("Long Distance Path", img)
  cv2.waitKey(0)

if __name__ == "__main__":
  longDistPath()


