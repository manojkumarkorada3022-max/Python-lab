import tkinter as tk

root = tk.Tk()

menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open")
file_menu.add_command(label="Exit")

mb = tk.Menubutton(root, text="Options")
mb.menu = tk.Menu(mb)
mb["menu"] = mb.menu

mb.menu.add_command(label="Option 1")
mb.menu.add_command(label="Option 2")
mb.pack()
root.mainloop()