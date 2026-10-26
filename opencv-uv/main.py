import cv2
import numpy as np

img = np.zeros((300, 300, 3), dtype=np.uint8)
img[:] = (0, 255, 0)

cv2.putText(
    img,
    "Hello Robotics!",
    (20, 150),
    cv2.FONT_HERSHEY_SIMPLEX,
    0.8,
    (255, 255, 255),
    2,
    cv2.LINE_AA
)

cv2.imwrite("output.png", img)
print("成功生成图片！当前 OpenCV 版本:", cv2.__version__)