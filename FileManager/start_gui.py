import tkinter
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image, ImageTk

import os


class StartGUI:
    def __init__(self):
        self.fileList = []
        self.directory = ""
        self.root = tk.Tk()
        self.root.geometry("500x500")
        self.root.resizable(True, True)

        # you have to configure the window columns and rows in order to center, then add the grid
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)

        # rows and columns must be configured no matter what, if you want to center, or anchor, or sticky
        self.grid = tk.Frame(self.root)
        self.grid.columnconfigure(0, weight=1)
        self.grid.rowconfigure(0, weight=3)
        self.grid.rowconfigure(1, weight=1)
        self.grid.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        self.introLabel = tk.Label(self.grid, text="Welcome to Peter's file manager! \nPress the button below to get "
                                                   "started on looking for files you don't need.", font=("Arial", 18))
        self.introLabel.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        self.browseButton = tk.Button(self.grid, text="Look into folder", font=("Arial", 18),
                                      command=self.browse_for_directory, bg="#5ee03a")
        self.browseButton.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

        self.root.mainloop()

    def browse_for_directory(self):
        self.directory = filedialog.askdirectory()
        messagebox.showinfo(message=str(os.listdir(self.directory)))
        self.fileList = os.listdir(self.directory)
