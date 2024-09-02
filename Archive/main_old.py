import tkinter
from tkinter import filedialog
import subprocess
import os
import json
import numpy as np
from PIL import Image
import imagehash
import re
from concurrent.futures import ThreadPoolExecutor, as_completed
import shutil

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

# This is used to make sure that the files are sorted in numerical order
def extract_number(filename):
    """ Extract the first numerical value found in the filename. """
    match = re.search(r'(\d+)', filename)
    if match:
        return int(match.group(1))
    return float('inf')  # Return a large number if no number is found

def compute_image_hash(filepath):
    # Compute the average hash of an image
    try:
        with Image.open(filepath) as img:
            return imagehash.average_hash(img)
    except Exception as e:
        print(f'Error opening file {filepath}: {e}')
        return None
# Create a loop that runs through each frame, if frame(n) == frame(n+1), then flags it if True
def duplicate_check():
    directory = 'C:\\tmp'
    
    files = [f for f in os.listdir(directory) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif'))]
    files.sort(key=extract_number)

    duplicates = 0
    total_comparisons = len(files) - 1
    last_percentage = -1
    hashes = {} # Preparing for parallel processing

    # Threshold for the hamming distance. How similar pictures are. a higher number means that the images are unique. Small hamming number means it will flag images as duplicates, when they are just similar
    # Compute hashes in parallel
    print("Creating image hashes for comparison")
    with ThreadPoolExecutor() as executor:
        futures = {executor.submit(compute_image_hash, os.path.join(directory, file)): file for file in files}
        for future in as_completed(futures):
            file = futures[future]
            hash_value = future.result()
            if hash_value is not None:
                hashes[file] = hash_value
    
    # Compare Hashes
    for i in range(len(files) - 1):
        file1 = files[i]
        file2 = files[i + 1]

        hash1 = hashes.get(file1)
        hash2 = hashes.get(file2)

        if hash1 and hash2:
            hamming_distance = hash1 - hash2
            if hamming_distance == 0:
                # Adding pixel by pixel comparison for exact matches
                img1 = Image.open(os.path.join(directory, file1))
                img2 = Image.open(os.path.join(directory, file2))
                np_img1 = np.array(img1)
                np_img2 = np.array(img2)

                if np.array_equal(np_img1, np_img2):
                    print(f'Duplicate found: {file1} and {file2} with Hamming distance: {hamming_distance}')
                    duplicates += 1
        


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
        return duplicates
# Potentiall provide information on what exact frames are dropped, find out if needed

def cleanup(duplicates):
    temp_folder = 'C:\\tmp'
    if duplicates < 0:
        choice = input(f"See frames in {temp_folder}. Press 1 to cleanup once frames have been checked manually")
        if choice == 1:
            if os.path.exists(temp_folder):
                try:
                    shutil.rmtree(temp_folder)
                    print("Temp folder has been cleaned up")
                except Exception as e:
                    print(f"Cleanup error: {e}")

def main():
    video_path = get_video_path()
    fps = get_fps_accurate(video_path)
    video_to_images(video_path, fps)
    duplicates = duplicate_check()
    #cleanup(duplicates)

ffmpeg_path = 'C:\\Users\\Study\\Documents\\Projects\\Dropped_Frames_Checker\\ffmpeg\\ffmpeg.exe'
main()