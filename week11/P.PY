import tkinter as tk

root = tk.Tk()

frame1 = tk.Frame(root)
frame1.pack()

tk.Label(frame1, text="Pack Method").pack()

frame2 = tk.Frame(root)
frame2.pack()

tk.Label(frame2, text="Grid Method").grid(row=0, column=0)

tk.Label(root, text="Place Method").place(x=50, y=50)

root.mainloop()