import tkinter as tk
from tkinter import *
from tkinter import ttk
from video_check_functions import *
import sys
import webbrowser

# Defining root to be able to close the window
root = None
def folder_selected_temp():
    print("Folder Option Selected")

def open_log():
    webbrowser.open('log.txt')

def single_video():
    global root
    root.destroy()
    video_check()
    open_log()
    sys.exit()


def folder():
    global root
    root.destroy()
    folder_check()
    open_log()
    sys.exit()

def main_menu():
    global root
    # Create the main window
    root = tk.Tk()
    root.title("Select an Option")
    root.geometry("600x300")

    # Create and place buttons
    folder_button = tk.Button(root, text="Folder", command=folder, width=20, height=2)
    folder_button.pack(pady=10)

    video_button = tk.Button(root, text="Single Video", command=single_video, width=20, height=2)
    video_button.pack(pady=10)

    # Run the application
    root.mainloop()


main_menu()
