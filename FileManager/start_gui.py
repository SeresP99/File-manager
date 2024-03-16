class StartGUI:
    def __init__(self):
        self.fileList = []
        self.directory = ""
        self.root = tk.Tk()
        self.grid = tk.Frame(self.root)
        self.browseButton = tk.Button(self.grid, text="Look into folder", font=("Arial", 18), command=self.browse_for_directory)
        self.browseButton.grid(padx=10, pady=10, row=1, column=0, sticky=tk.W+tk.E)
        self.grid.pack()
        self.root.mainloop()
    def browse_for_directory(self):
        self.directory = filedialog.askdirectory()
        messagebox.showinfo(message=str(os.listdir(self.directory)))
        self.fileList = os.listdir(self.directory)
