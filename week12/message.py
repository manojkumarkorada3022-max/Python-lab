import tkinter as tk
from tkinter import messagebox, filedialog

root = tk.Tk()

def show_msg():
    messagebox.showinfo("Message", "Hello World")

def open_file():
    filedialog.askopenfilename()

# Buttons
tk.Button(root, text="Show Message", command=show_msg).pack()
tk.Button(root, text="Open File", command=open_file).pack()

root.mainloop()