import customtkinter as ctk
import tkinter as tk
import pandas as pd

root = tk.Tk()
root.geometry("800x700")
root.title("Rotten Tomatoes Top Movies")
but1 = tk.IntVar()

def buttonpress():
    if but1.get() == 1:
        print("Box is checked.")
    else:
        print("Box is unchecked.")

button1 = ctk.CTkCheckBox(root, text="Title",variable = but1,command=buttonpress)
button1.pack(padx = 20, pady = 20)
root.mainloop()
 