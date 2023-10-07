import pyrealsense2 as rs
import numpy as np
import cv2
from apriltag import apriltag
import sys

K = np.array([[386.08, 0, 328.197],
                [0, 386.08, 235.751],
                [0, 0, 1]])
qr_code_size = 0.0541  # 二维码边长(m)

def out_position(path=""):
    img =cv2.imread(path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    detector = apriltag("tag36h11")
    tags = detector.detect(gray)
    longs = len(tags)
    if longs > 0 :
        print("%d apriltags have been detected."%len(tags))
        # print(tags)
        # arr = np.array(tags[0]["lb-rb-rt-lt"],np.int).reshape(1,4,2)
        # Img = cv2.polylines(img,arr,True,(0,0,255),2)
        # Img = cv2.circle(img,tuple(map(int,tags[0]["center"])), 4, (2,180,200), 2)
        # cv2.imwrite("apriltag_test.jpg",Img)
        
        center = tags[0]["center"]
        locations = [tags[0]["lb-rb-rt-lt"][3], tags[0]["lb-rb-rt-lt"][2], tags[0]["lb-rb-rt-lt"][1], tags[0]["lb-rb-rt-lt"][0]]
        center_pixel = np.array(center)
        corner_pixels = np.array(locations)
        object_points = np.array([[-qr_code_size / 2, qr_code_size / 2, 0],
                                [qr_code_size / 2, qr_code_size / 2, 0],
                                [qr_code_size / 2, -qr_code_size / 2, 0],
                                [-qr_code_size / 2, -qr_code_size / 2, 0]])

        image_points = np.array(corner_pixels, dtype=np.float32)
        # 解决透视问题
        retval, rvec, tvec = cv2.solvePnP(object_points, image_points, K, None)
        # 计算相机与二维码的距离
        distance_camera_qr = np.linalg.norm(tvec)
        rvec_degrees = np.degrees(rvec)
        # 打印结果
        print(tags[0]["id"])
        print("相机与二维码的距离（米）：", distance_camera_qr)
        print("相机到二维码的平移向量（米）：", tvec)
        print("相机到二维码的旋转向量（角度）：", rvec_degrees)

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
