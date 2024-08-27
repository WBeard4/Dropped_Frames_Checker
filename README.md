# Dropped_Frames_Checker

# Update:
I have added no_temp_files, which will soon be the main script once it is up and running. Uses CV2 to check the frames while streaming the video, so no need to break the video down into images. 
This is faster and mean that there are no temp files to take up storage space

# Original:
The idea of this program will be to break a video down into a series of images, then see if any images have an idential image next to them, which shows a dropped frame.

So if Frame(n) is the same as Frame(n+1) then that will be a dropped frame

This is being created at request, as we work with a lot of redered footage at work, and this will speed up QA
