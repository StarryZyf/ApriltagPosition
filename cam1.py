import pyrealsense2 as rs
pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
config.enable_stream(rs.stream.color, 640, 480, rs.format.rgb8, 30)
cfg = pipeline.start(config)
time.sleep(1)
profile = cfg.get_stream(rs.stream.depth) # 获取深度流的配置文件
intr = profile.as_video_stream_profile().get_intrinsics() # 向下播放到视频流并获取内在信息
print(intr)  # 获取内参 width: 640, height: 480, ppx: 319.115, ppy: 234.382, fx: 597.267, fy: 597.267, model: Brown Conrady, coeffs: [0, 0, 0, 0, 0] 319.1151428222656
print(intr.ppx)  # 获取指定某个内参
