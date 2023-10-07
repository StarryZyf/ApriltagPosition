import pyrealsense2 as rs
import numpy as np
import cv2
from apriltag import apriltag
import sys

def out_position(path=""):
    img =cv2.imread(path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    detector = apriltag("tag36h11")
    tags = detector.detect(gray)
    longs = len(tags)
    if longs > 0 :
        print("%d apriltags have been detected."%len(tags))
        print(tags)
        arr = np.array(tags[0]["lb-rb-rt-lt"],np.int).reshape(1,4,2)
        Img = cv2.polylines(img,arr,True,(0,0,255),2)
        Img = cv2.circle(img,tuple(map(int,tags[0]["center"])), 4, (2,180,200), 2)
        cv2.imwrite("apriltag_test.jpg",Img)
    else:
        print("%d apriltags have been detected."%len(tags))

pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)
pipeline.start(config)
while True:
    # 获取图像帧
    frames = pipeline.wait_for_frames()
    color_frame = frames.get_color_frame()
    # 将图像帧转换为numpy数组
    color_image = np.asanyarray(color_frame.get_data())
    cv2.imwrite('image.jpg', color_image)
    out_position('image.jpg')

    # 按下 'q' 键退出循环
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 清理资源
pipeline.stop()
