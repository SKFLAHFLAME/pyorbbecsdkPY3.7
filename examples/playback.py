from pyorbbecsdk import *
import time
import cv2
import numpy as np

from queue import Queue

depth_frames_queue = Queue()
MAX_QUEUE_SIZE = 5
ESC_KEY = 27


def playback_state_callback(state):
    if state == OBMediaState.OB_MEDIA_BEGIN:
        print("Bag player stopped")
    elif state == OBMediaState.OB_MEDIA_END:
        print("Bag player playing")
    elif state == OBMediaState.OB_MEDIA_PAUSED:
        print("Bag player paused")


def frame_playback_callback(frame):
    global depth_frames_queue
    depth_frame = frame.as_depth_frame()
    if depth_frame is None:
        return
    if depth_frames_queue.qsize() >= MAX_QUEUE_SIZE:
        depth_frames_queue.get()
    depth_frames_queue.put(depth_frame)


def rendering_frames():
    global depth_frames_queue
    while True:
        depth_frame = None
        if not depth_frames_queue.empty():
            depth_frame = depth_frames_queue.get()
        if depth_frame is None:
            continue
        depth_data = np.asanyarray(depth_frame.get_data())
        depth_width, depth_height = depth_frame.get_width(), depth_frame.get_height()
        scale = depth_frame.get_depth_scale()
        depth_data = np.resize(depth_data, (depth_height, depth_width, 2))
        depth_data = depth_data * scale
        channel0 = depth_data[:, :, 0]
        channel1 = depth_data[:, :, 1]
        channel0_norm = cv2.normalize(channel0, None, 0, 255, cv2.NORM_MINMAX)
        channel1_norm = cv2.normalize(channel1, None, 0, 255, cv2.NORM_MINMAX)
        depth_image = np.zeros((depth_height, depth_width, 3), dtype=np.uint8)
        depth_image[:, :, 0] = channel0_norm
        depth_image[:, :, 1] = channel1_norm
        depth_image = cv2.applyColorMap(depth_image, cv2.COLORMAP_JET)
        cv2.imshow("Depth Viewer", depth_image)
        key = cv2.waitKey(1)
        if key == ord('q') or key == ESC_KEY:
            break


def main():
    pipeline = Pipeline("./test.bag")
    playback = pipeline.get_playback()
    playback.set_playback_state_callback(playback_state_callback)
    device_info = playback.get_device_info()
    print("Device info: ", device_info)
    camera_param = pipeline.get_camera_param()
    print("Camera param: ", camera_param)
    playback.start(frame_playback_callback)
    try:
        rendering_frames()
    except KeyboardInterrupt:
        pass
    pipeline.stop()


if __name__ == "__main__":
    main()
