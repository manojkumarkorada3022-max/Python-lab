import tkinter as tk

root = tk.Tk()

tk.Label(root, text="Enter Name:").pack()

entry = tk.Entry(root)
entry.pack()

tk.Button(root, text="Submit").pack()

root.mainloop()