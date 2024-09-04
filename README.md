# Dropped Frames Checker

## Overview

The **Dropped Frames Checker** is a Python-based tool designed to identify dropped frames in video files. This application can scan a single video or all videos within a specified folder, comparing each frame for duplicates using image hashing and Mean Squared Error (MSE) techniques. Any detected duplicates are logged to a file named `log.txt`.

## Features

- **Single Video Processing:** Select and scan a single video file for dropped frames.
- **Batch Processing:** Scan all video files in a chosen folder.
- **Frame Comparison:** Detects dropped frames by comparing image hashes and pixel-level data.
- **Logging:** Results are logged with timestamps to `log.txt`.

## Requirements

The application requires the following Python packages, which are listed in the `requirements.txt` file:

- `ImageHash==4.3.1`
- `numpy==2.1.1`
- `opencv-python==4.10.0.84`
- `pillow==10.4.0`
- `PyWavelets==1.7.0`
- `scipy==1.14.1`
- `tk==0.1.0`

To install the required packages, use:

`pip install -r requirements.txt`


## Usage

1. **Clone the Repository:**
`git clone https://github.com/yourusername/dropped-frames-checker.git cd dropped-frames-checker`


2. **Install Dependencies:**

After navigating to the project directory, install the required Python packages:

`pip install -r requirements.txt`


3. **Run the Application:**

Execute the application with:
`python menu.py`


Upon running, you will be prompted to choose either a single video file or a folder containing multiple videos.

**Choose Processing Mode:**
- **Single Video:** Select a single video file to analyze.
- **Folder Processing:** Select a folder to analyze all videos within it.

4. **Review the Results:**

After processing, results will be printed to the console and logged in `log.txt` in the same directory.

## How It Works

- **Video Selection:** The app uses Tkinter's file dialog to allow users to select a video file or a folder.
- **Frame Hashing:** Each frame is converted to an image hash using `imagehash` to detect duplicates efficiently.
- **Similarity Check:** For `.mov` files, the app uses MSE to compare frames more accurately, allowing for controlled tolerance levels.
- **Logging:** The results, including any detected duplicates and processing time, are logged to `log.txt`.

## Logging Details

The `log.txt` file will include:

- The path of the processed video.
- Timestamps indicating when the processing started and ended.
- A list of duplicate frames found, including the frame number and the time in seconds where the duplicate occurs.

### Example Logs

Here’s a sample log entry:

```
2024-09-04 13:10:56 - C:/Users/Will/Videos/1.mp4

2024-09-04 13:11:01 - Video fully processed: No duplicates found 

2024-09-04 13:11:14 - C:/Users/Will/Videos/Fury vs Ngannou - Director： Seb Edwards.mp4

2024-09-04 13:14:09 - C:/Users/Will/Videos/The Fastest Way To Find Waldo.mp4

Duplicate found at frame 490 at 16.35 seconds
Duplicate found at frame 491 at 16.38 seconds
Duplicate found at frame 502 at 16.75 seconds
Duplicate found at frame 503 at 16.78 seconds
Duplicate found at frame 504 at 16.82 seconds
Duplicate found at frame 505 at 16.85 seconds
Duplicate found at frame 506 at 16.88 seconds
Duplicate found at frame 507 at 16.92 seconds
Duplicate found at frame 508 at 16.95 seconds
Duplicate found at frame 509 at 16.98 seconds
Duplicate found at frame 510 at 17.02 seconds
Duplicate found at frame 511 at 17.05 seconds
Duplicate found at frame 514 at 17.15 seconds
Duplicate found at frame 518 at 17.28 seconds
2024-09-04 13:14:44 - Video fully processed: 14 duplicates found
```


## Future Enhancements

- **GUI Version:** Developing a more user-friendly GUI interface for the app.
- **Extended Format Support:** Adding support for more video formats and codecs.
- **Real-time Monitoring:** Implementing real-time video monitoring to detect dropped frames during live streams.

## Contributing

Feel free to fork this repository, submit pull requests, or open issues if you encounter any bugs or have suggestions for improvement.

## License

Copyright 2024 William Beard

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to use the Software for personal, educational, or non-commercial purposes only.

Commercial use, including any use in an enterprise environment, requires a separate paid license. Please contact `wmb6598@gmail.com` for commercial licensing.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT, OR OTHERWISE, ARISING FROM, OUT OF, OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Acknowledgments

- The application leverages powerful libraries such as OpenCV, NumPy, ImageHash, and Pillow for video processing and image analysis.
- Special thanks to the open-source community for providing these tools.
