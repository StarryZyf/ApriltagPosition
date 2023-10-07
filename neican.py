import pyrealsense2 as rs

# 初始化相机
pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)
config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)

# 启动相机
pipeline.start(config)

# 获取相机内参矩阵
profile = pipeline.get_active_profile()
depth_profile = profile.get_stream(rs.stream.depth)
intrinsics = depth_profile.as_video_stream_profile().get_intrinsics()

# 打印内参矩阵
print("内参矩阵:")
print(f"宽度: {intrinsics.width}")
print(f"高度: {intrinsics.height}")
print(f"焦距: ({intrinsics.fx}, {intrinsics.fy})")
print(f"主点: ({intrinsics.ppx}, {intrinsics.ppy})")
print(f"畸变参数: {intrinsics.coeffs}")

# 关闭相机
pipeline.stop()

