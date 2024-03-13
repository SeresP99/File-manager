import tkinter as tk

root = tk.Tk()
root.title("File Manager")
root.wm_resizable(False, False)
root.geometry("800x600")

label = tk.Label(root, text="Hello World", font=("Arial", 18), justify="left")
label.pack(padx=20, pady=20)

textBox = tk.Text(root, height=3, font=("Arial", 16))
textBox.pack(padx=10, pady=20)

# entryWidget = tk.Entry(root)
# entryWidget.pack()

buttonFrame = tk.Frame(root)
buttonFrame.columnconfigure(0, weight=1)
buttonFrame.columnconfigure(1, weight=1)
buttonFrame.columnconfigure(2, weight=1)

btn1 = tk.Button(buttonFrame, text="1", font=("Arial", 18))
btn1.grid(padx=5, pady=10, row=0, column=0, sticky=tk.W+tk.E)
btn2 = tk.Button(buttonFrame, text="2", font=("Arial", 18))
btn2.grid(padx=5, pady=10, row=0, column=1, sticky=tk.W+tk.E)
btn3 = tk.Button(buttonFrame, text="3", font=("Arial", 18))
btn3.grid(padx=5, pady=10, row=0, column=2, sticky=tk.W+tk.E)

buttonFrame.pack(fill="x")

root.mainloop()
