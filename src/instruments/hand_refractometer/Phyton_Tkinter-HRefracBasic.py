import tkinter as tk
import value_generator as vg

def greet():
    label.config(text=f"Hello, {entry.get()}!")

def peek():
    label2.config(text=f"You got the number {vg.random_value()}")

def calibration():
    label2.config(text=f"Refractomater calibrated succesfully! value returned to 0 !")

# Windows
root = tk.Tk()

# Window Title
root.title("HandRefractometer Tkinter Example")

# Texts
label = tk.Label(root, text="Enter your name:")
label2 = tk.Label(root, text="What Value do you got?")

# Lay out the Label in the window using the "pack" geometry manager.
# - pack() places the widget sequentially (top to bottom by default).
# - Tkinter has three geometry managers: pack, grid, and place.
label.pack()
label2.pack(side='right')

# Create an Entry widget to accept user input (single line text field).
# - Parent is "root".
entry = tk.Entry(root)

# Lay out the Entry below the Label (because pack stacks them in creation order).
entry.pack(after=label)

# Buttons.
button = tk.Button(root, text="Greet Me", command=greet)

button2 = tk.Button(root, text="Peek", command=peek)

button3 = tk.Button(root, text="Calibrate", command=calibration)

# Button Layouts
button.pack()
button2.pack()
button3.pack()

# Keeps the window responsive until the user closes it or the program exits.
root.mainloop()
