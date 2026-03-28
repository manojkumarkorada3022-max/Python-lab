import tkinter as tk

root = tk.Tk()

var1 = tk.IntVar()
tk.Checkbutton(root, text="Option 1", variable=var1).pack()

var2 = tk.StringVar()
tk.Radiobutton(root, text="Male", variable=var2, value="Male").pack()
tk.Radiobutton(root, text="Female", variable=var2, value="Female").pack()

root.mainloop()