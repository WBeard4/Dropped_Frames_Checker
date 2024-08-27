import cv2
import numpy as np
import imagehash
from PIL import Image
from concurrent.futures import ThreadPoolExecutor, as_completed
import tkinter
from tkinter import filedialog
import time

# Use tkinter to open a dialog box, and allow the user to choose a video file
def get_video_path():
    root = tkinter.Tk()
    root.withdraw()
    video_name = filedialog.askopenfile(parent=root,initialdir="/",title='Please select a file')
    if video_name is not None:
        video_path = video_name.name
        return video_path
    
# Using CV2 to open each frame and generate an image hash, without needed to turn the video into images    
def compute_frame_hash(frame):
    try:
        frame_img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        return imagehash.average_hash(frame_img)
    except Exception as e:
        print(f"Compute_frame_hash error: {e}")
        return None

def duplicate_check(video_path):
    # Open the video using CV2, rather than creating temp images
    video = cv2.VideoCapture(video_path)
    if not video.isOpened():
        print(f"Error: Could not open video {video_path}")
        return

    duplicates = 0
    last_hash = None
    last_frame = None
    frame_number = 0

    # Read the frames from the video
   
    while True:

        ret, frame = video.read()
        if not ret:
            break # End of video

        # Compute has for the frame we are on currently
        current_hash = compute_frame_hash(frame)

            # Get the current frame timestamp in milliseconds
        frame_time_ms = video.get(cv2.CAP_PROP_POS_MSEC)
        frame_time_s = frame_time_ms / 1000  # Convert milliseconds to seconds

        # Compare the current frame with the last frame hash
        if last_hash is not None and current_hash is not None:
            hamming_distance = last_hash - current_hash
            if hamming_distance == 0:
                # Check pixel by pixel
                if last_frame is not None and np.array_equal(last_frame, frame):
                    print(f'Duplicate found at frame {frame_number} at {frame_time_s:.2f} seconds')
                    duplicates += 1

        last_hash = current_hash
        last_frame = frame
        frame_number += 1
    video.release()

    if duplicates == 0:
        print("No duplicates found")
    else:
        print(f"{duplicates} duplicates found")
    return duplicates

def main():
    # Added a start and end time, to see how long the program took to run
    start = time.time()
    video_path = get_video_path()
    if video_path:
        duplicate_check(video_path)
    end = time.time()
    length = end - start
    print(f"Script took {int(length)} seconds")
main()