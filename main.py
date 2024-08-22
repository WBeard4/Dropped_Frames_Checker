import ffmpeg
import tkinter
from tkinter import filedialog
import subprocess
import os
import cv2
import json




# Use tkinter to open a dialog box, and allow the user to choose a video file
def get_video_path():
    root = tkinter.Tk()
    root.withdraw()
    video_name = filedialog.askopenfile(parent=root,initialdir="/",title='Please select a file')
    if video_name is not None:
        video_path = video_name.name
        return video_path
    
# This function is to get the fps of the video, so we know how many images will be needed
def get_fps_accurate(video_path):
    ffprobe_path = 'C:\\Users\\Study\\Documents\\Projects\\Dropped_Frames_Checker\\ffmpeg\\ffprobe.exe'
    command = [
        ffprobe_path,
        '-v', 'error',
        '-select_streams', 'v:0',
        '-show_entries', 'stream=r_frame_rate',
        '-of', 'json',
        video_path
    ]

    # Run the command and capture the output
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    if result.returncode == 0:
        # Parse the JSON output
        output = json.loads(result.stdout)
        frame_rate = output['streams'][0]['r_frame_rate']

        # Convert frame rate to FPS
        numerator, denominator = map(int, frame_rate.split('/'))
        fps = int(numerator / denominator)
        print(f"FPS: {fps}")
        return fps
    else:
        print('Error retrieving FPS:')
        print(result.stderr)

# Create a temp file, and use ffmpeg to break the video down into its frames
def video_to_images(video_path, fps):


    temp_folder = 'C:\\tmp'
    if not os.path.exists(temp_folder):
        os.makedirs(temp_folder)
    output_pattern = os.path.join(temp_folder, 'test-%d.jpg')

    command = [
        ffmpeg_path,
        '-i', video_path,  # Use the selected file as input
        '-vf', f'fps={fps}',  # FPS filter
        output_pattern,  # Output files
        '-start_number', '0',  # Start numbering at 0
        '-y'  # Overwrite output files without asking
    ]
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode == 0:
        print('Process completed successfully.')
        print(result.stdout)
    else:
        print('Process failed.')
        print(command)
        print('Error output:', result.stderr)


# Create a loop that runs through each frame, if frame(n) == frame(n+1), then flags it if True

# Potentiall provide information on what exact frames are dropped, find out if needed

'''
Could potentially see if doing 60 frames at a time is faster, rather than breaking the entire video down at once
    This means that frames 60 61 might be seperate, so would need to account for that'''

def main():
    video_path = get_video_path()
    fps = get_fps_accurate(video_path)
    video_to_images(video_path, fps)

ffmpeg_path = 'C:\\Users\\Study\\Documents\\Projects\\Dropped_Frames_Checker\\ffmpeg\\ffmpeg.exe'
main()