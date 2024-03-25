import os
import tkinter as tk

from conclusion_screen import ConclusionScreen
from file import File

class FileManagerGUI:
    def __init__(self, fileList, directory):
        self.fileList = fileList
        self.file_array = create_file_array(self.fileList)
        self.directory = directory
        self.currentFileIndex = 0

        self.root = tk.Tk()
        self.root.geometry("800x500")
        # self.root.resizable(False, False)

        self.grid = tk.Frame(self.root)
        # rows and columns must be configured
        self.grid.columnconfigure(0, weight=1)
        self.grid.columnconfigure(1, weight=1)
        self.grid.columnconfigure(2, weight=1)

        self.grid.rowconfigure(0, weight=2)
        self.grid.rowconfigure(1, weight=1)

        self.textBox = tk.Text(self.grid, height=10, font=("Arial", 18))
        self.textBox.grid(padx=10, pady=10, columnspan=3, row=0, column=0)
        self.textBox.insert("1.0", str(self.fileList[0]))

        self.previousButton = tk.Button(self.grid, font=("Arial", 18), text="Previous", state="disabled",
                                        command=self.previous_button_command)
        self.previousButton.grid(padx=10, pady=10, row=1, column=0, sticky="EW")

        self.openButton = tk.Button(self.grid, font=("Arial", 18), text="Open", command=self.open_file_button_command)
        self.openButton.grid(padx=10, pady=10, row=1, column=1, sticky="EW")

        self.nextButton = tk.Button(self.grid, font=("Arial", 18), text="Next", command=self.next_button_command)
        self.nextButton.grid(padx=10, pady=10, row=1, column=2, sticky="EW")

        self.grid.pack(padx=10, pady=10)

        self.markForDeletionButton = tk.Button(self.root, font=("Arial", 18), text="Mark for Deletion",
                                               command=self.toggle_mark_for_deletion)
        self.markForDeletionButton.pack(padx=10, pady=10)

        self.doneButton = tk.Button(self.root, font=("Arial", 18), text="Done",
                                    command=self.continue_to_conclusion)
        self.doneButton.pack(padx=10, pady=10)

        print(len(self.fileList))
        print(self.currentFileIndex)

        self.root.mainloop()

    def next_button_command(self):
        # "end-1c": the last index
        self.textBox.delete("1.0", 'end-1c')
        self.currentFileIndex = self.currentFileIndex + 1
        self.textBox.insert("1.0", str(self.fileList[self.currentFileIndex]))
        self.previousButton["state"] = "normal"

        if self.currentFileIndex == len(self.fileList) - 1:
            self.nextButton["state"] = "disabled"

        print(self.currentFileIndex)
        self.update_mark_for_deletion_button()

    def previous_button_command(self):
        self.textBox.delete("1.0", 'end-1c')
        self.currentFileIndex = self.currentFileIndex - 1
        self.textBox.insert("1.0", str(self.fileList[self.currentFileIndex]))
        self.nextButton["state"] = "normal"

        if self.currentFileIndex == 0:
            self.previousButton["state"] = "disabled"

        print(self.currentFileIndex)
        self.update_mark_for_deletion_button()

    def open_file_button_command(self):
        os.startfile(self.directory + "/" + self.fileList[self.currentFileIndex])
        with open(self.directory + "/" + self.fileList[self.currentFileIndex], 'r') as file:
            file_string = file.read()
            self.textBox.delete("1.0", 'end-1c')
            self.textBox.insert("1.0", file_string)

    def toggle_mark_for_deletion(self):
        self.file_array[self.currentFileIndex].marked_for_deletion = not (self.file_array[self.currentFileIndex].
                                                                          marked_for_deletion)
        self.update_mark_for_deletion_button()
        print(self.file_array)

    def update_mark_for_deletion_button(self):
        if self.file_array[self.currentFileIndex].marked_for_deletion:
            self.markForDeletionButton["background"] = "red"
        else:
            self.markForDeletionButton["background"] = "SystemButtonFace"  # default background color

    def continue_to_conclusion(self):
        ConclusionScreen(self.file_array, self.directory)


def create_file_array(file_list):
    file_array = []
    for item in file_list:
        file_array.append(File(item))
    return file_array
