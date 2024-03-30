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


class FileRowRecycleView:
    def __init__(self, root, file_name):
        self.parentGrid = tk.Frame(root, background="green")
        self.Grid = tk.Frame(self.parentGrid)

        self.Grid.columnconfigure(0, weight=3)
        self.Grid.columnconfigure(1, weight=1)

        self.Grid.rowconfigure(0, weight=1)

        self.FileLabel = tk.Label(self.Grid, text=file_name, font=("Arial", 15))
        self.FileLabel.grid(row=0, column=0, sticky="nsw")

        self.UndoButton = tk.Button(self.Grid, text="Undo", font=("Arial", 12))
        self.UndoButton.grid(row=0, column=1, sticky="nsew")

        self.Grid.pack(padx=10, pady=10, fill="x")
        self.parentGrid.pack(anchor="n", fill="y")


