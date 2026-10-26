import cv2
import numpy as np

# 创建一个 300x300 的绿色背景图像
img = np.zeros((300, 300, 3), dtype=np.uint8)
img[:] = (0, 255, 0)

# 在图像上写入文字
cv2.putText(
    img,
    "Hello OpenCV!",
    (20, 150),
    cv2.FONT_HERSHEY_SIMPLEX,
    0.8,
    (255, 255, 255),
    2,
    cv2.LINE_AA
)

# 保存图像
cv2.imwrite("output.png", img)

print("成功生成图片！当前 OpenCV 版本:", cv2.__version__)