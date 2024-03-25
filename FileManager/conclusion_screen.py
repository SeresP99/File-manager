import tkinter as tk
from PIL import ImageTk, Image
from file import File
import os


class ConclusionScreen:
    def __init__(self, file_array, directory):
        self.file_array = file_array
        self.directory = directory

        # self.root = tk.Toplevel()
        self.root = tk.Tk()
        self.root.geometry("500x1000")
        self.root.resizable(True, True)

        # self.root.columnconfigure(0, weight=1)
        # self.root.rowconfigure(0, weight=1)

        recycle_view_array = []
        for item in self.file_array:
            print(str(item))
            temp_label = tk.Label(self.root, text=str(item))
            temp_label.pack(padx=10, pady=10, anchor="nw")
            recycle_view_array.append(temp_label)

        path = "x.jpg"
        img = Image.open(path)
        img = img.resize((15, 15))
        bitmap = ImageTk.PhotoImage(img)
        panel = tk.Label(self.root, image=bitmap)
        panel.pack(side="left")

        self.root.mainloop()
