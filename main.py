import tkinter
from tkinter import filedialog
import subprocess
import os
import json
import numpy as np
from PIL import Image
import imagehash
import re



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
    output_pattern = os.path.join(temp_folder, '%d.jpg')

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


def extract_number(filename):
    """ Extract the first numerical value found in the filename. """
    match = re.search(r'(\d+)', filename)
    if match:
        return int(match.group(1))
    return float('inf')  # Return a large number if no number is found

# Create a loop that runs through each frame, if frame(n) == frame(n+1), then flags it if True
def duplicate_check():
    directory = 'C:\\tmp'
    
    files = os.listdir(directory)
    files.sort(key=extract_number)

    duplicates = 0
    total_comparisons = len(files) - 1
    last_percentage = -1
    hashes = {}

    for i in range(len(files) - 1):
        file1 = os.path.join(directory, files[i])
        file2 = os.path.join(directory, files[i+1])

        try:

            with Image.open(file1) as img1, Image.open(file2) as img2:
                # Convert images to numpy arrays
                arr1 = np.array(img1)
                arr2 = np.array(img2)
                

                
                # Check if the images are identical
                if arr1.shape == arr2.shape and np.array_equal(arr1, arr2):
                    print(f'Duplicate frame found: {files[i]} and {files[i + 1]}')
                    duplicates += 1

        except Exception as e:
            print(f'Error opening files {file1} or {file2}: {e}')
        
                # Calculate the current percentage complete
        percent_complete = int((i + 1) / total_comparisons * 100)
        
        # Print the percentage only if it has changed
        if percent_complete > last_percentage:
            print(f'Progress: {percent_complete}% complete')
            last_percentage = percent_complete

    if duplicates == 0:
        print('No duplicates found')
    else:
        print(f'{duplicates} duplicates found')        
# Potentiall provide information on what exact frames are dropped, find out if needed

'''
Could potentially see if doing 60 frames at a time is faster, rather than breaking the entire video down at once
    This means that frames 60 61 might be seperate, so would need to account for that'''

def main():
    video_path = get_video_path()
    fps = get_fps_accurate(video_path)
    video_to_images(video_path, fps)
    duplicate_check()

ffmpeg_path = 'C:\\Users\\Study\\Documents\\Projects\\Dropped_Frames_Checker\\ffmpeg\\ffmpeg.exe'
main()