import ffmpeg
import Tkinter, tkFileDialog

# Use tkinter to open a dialog box, and allow the user to choose a video file


root = Tkinter.Tk()
root.withdraw()
dirname = tkFileDialog.askdirectory(parent=root,initialdir="/",title='Please select a directory')
# Check the video quality and fps if poosible, though this will mostly be used for 4k60

# Create a temp file, and use ffmpeg to break the video down into its frames

# Create a loop that runs through each frame, if frame(n) == frame(n+1), then flags it if True

# Potentiall provide information on what exact frames are dropped, find out if needed

'''
Could potentially see if doing 60 frames at a time is faster, rather than breaking the entire video down at once
    This means that frames 60 61 might be seperate, so would need to account for that'''