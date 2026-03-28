import tkinter as tk

root = tk.Tk()

lb = tk.Listbox(root)
lb.pack(side="left")

lb.insert(1, "Item 1")
lb.insert(2, "Item 2")
lb.insert(3, "Item 3")

sb = tk.Scrollbar(root)
sb.pack(side="right", fill="y")

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

root.mainloop()