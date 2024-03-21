import tkinter as tk


class FileManagerGUI:
    def __init__(self, fileList, directory):
        self.fileList = fileList
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

    def previous_button_command(self):
        self.textBox.delete("1.0", 'end-1c')
        self.currentFileIndex = self.currentFileIndex - 1
        self.textBox.insert("1.0", str(self.fileList[self.currentFileIndex]))
        self.nextButton["state"] = "normal"

        if self.currentFileIndex == 0:
            self.previousButton["state"] = "disabled"

        print(self.currentFileIndex)

    def open_file_button_command(self):
        os.startfile(self.directory + "/" + self.fileList[self.currentFileIndex])
