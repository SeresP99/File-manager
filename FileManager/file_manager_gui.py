import tkinter as tk


class FileManagerGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("800x500")
        #self.root.resizable(False, False)

        self.grid = tk.Frame(self.root)
        #rows and columns must be configured
        self.grid.columnconfigure(0, weight=1)
        self.grid.columnconfigure(1, weight=1)
        self.grid.columnconfigure(2, weight=1)

        self.grid.rowconfigure(0, weight=2)
        self.grid.rowconfigure(1, weight=1)

        self.textBox = tk.Text(self.grid, height=5, font=("Arial", 18))
        self.textBox.grid(padx=10, pady=10, columnspan=3, row=0, column=0)

        self.previousButton = tk.Button(self.grid, font=("Arial", 18), text="Previous")
        self.previousButton.grid(padx=10, pady=10, row=1, column=0)

        self.openButton = tk.Button(self.grid, font=("Arial", 18), text="Open")
        self.openButton.grid(padx=10, pady=10, row=1, column=1)

        self.nextButton = tk.Button(self.grid, font=("Arial", 18), text="Next")
        self.nextButton.grid(padx=10, pady=10, row=1, column=2)

        self.grid.pack(padx=10, pady=10)

        self.root.mainloop()
