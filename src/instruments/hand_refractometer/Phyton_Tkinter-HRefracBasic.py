import tkinter as tk
from tkinter import ttk
import value_generator as vg

# Can we make this def as a external modukle file? 
def peek():
    label2.config(text=f"You got the number {vg.random_value()}")

def calibration():
    label2.config(text=f"Refractomater calibrated succesfully! \nvalue returned to 0 !")

# Windows
root = tk.Tk()

# Window Title
root.title("HandRefractometer Tkinter Example")

# ttk Style
style = ttk.Style()
style.configure("BW.TLabel", foreground="black", background="white")

# Texts
label2 = ttk.Label(root, text="What Value do you got?")

# Lay out the Label in the window using the "pack" geometry manager.
# - pack() places the widget sequentially (top to bottom by default).
# - Tkinter has three geometry managers: pack, grid, and place.
label2.pack(side='right')

# Buttons.

button2 = ttk.Button(root, text="Peek", command=peek)

button3 = ttk.Button(root, text="Calibrate", command=calibration)

# Button Layouts
button3.pack()
button2.pack()


# Keeps the window responsive until the user closes it or the program exits.
root.mainloop()
