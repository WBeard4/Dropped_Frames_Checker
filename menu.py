import tkinter as tk
from tkinter import *
from tkinter import ttk
from video_check import *

def folder_selected_temp():
    print("Folder Option Selected")

def main_menu():
    # Create the main window
    root = tk.Tk()
    root.title("Select an Option")
    root.geometry("300x150")

    # Create and place buttons
    folder_button = tk.Button(root, text="Folder", command=folder_selected_temp, width=20, height=2)
    folder_button.pack(pady=10)

    video_button = tk.Button(root, text="Single Video", command=get_video_path, width=20, height=2)
    video_button.pack(pady=10)

    # Run the application
    root.mainloop()

main_menu()