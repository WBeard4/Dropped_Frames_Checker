import subprocess
import os
import tkinter
from tkinter import filedialog

def convert_mov_to_mp4(input_file, output_file):
    """
    Convert a .mov file to .mp4 using ffmpeg.
    
    Parameters:
    - input_file: The path to the .mov file.
    - output_file: The path where the .mp4 file should be saved.
    """
    # Specify the full path to ffmpeg if it's not in the system PATH
    ffmpeg_path = 'C:/Users/Study/Documents/Projects/Dropped_Frames_Checker/ffmpeg/ffmpeg.exe'  # Adjust this path accordingly

    command = [
        ffmpeg_path,
        '-i', input_file,
        '-vcodec', 'libx264',
        '-acodec', 'aac',
        output_file
    ]
    
    try:
        subprocess.run(command, check=True)
        print(f"Conversion successful: {input_file} -> {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error during conversion: {e}")

def get_file_path(title, filetypes):
    """
    Open a file dialog to select a file.
    
    Parameters:
    - title: The title of the dialog window.
    - filetypes: The file types to filter.
    
    Returns:
    - The selected file path.
    """
    root = tkinter.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(
        title=title,
        filetypes=filetypes
    )
    return file_path

def get_save_path(title, filetypes):
    """
    Open a file dialog to select a save location for the output file.
    
    Parameters:
    - title: The title of the dialog window.
    - filetypes: The file types to filter.
    
    Returns:
    - The selected save path.
    """
    root = tkinter.Tk()
    root.withdraw()
    file_path = filedialog.asksaveasfilename(
        title=title,
        filetypes=filetypes,
        defaultextension=".mp4"  # Ensure default extension is .mp4
    )
    return file_path

if __name__ == "__main__":
    input_file = get_file_path("Select the .mov file to convert", [("MOV files", "*.mov")])
    if input_file:
        output_file = get_save_path("Save the converted .mp4 file as", [("MP4 files", "*.mp4")])
        if output_file:
            convert_mov_to_mp4(input_file, output_file)
        else:
            print("No output file selected.")
    else:
        print("No input file selected.")
