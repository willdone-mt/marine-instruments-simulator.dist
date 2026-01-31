import tkinter as tk
from tkinter import ttk

# Can we make these rows between =#=== as an external module file? 
# =#====

# defining functions =====

# =====

# Main TKinter functions =====
# Main Window
root = tk.Tk()
root.title("HandRefractometer MVP Simulator")
root.geometry("600x300")
root.resizable(False, False)

# ttk Style
style = ttk.Style()
style.configure("BW.TPanedwindow", foreground="grey", background="white", relief="raised")
style.configure("TLabel", foreground="black", background="white")

# Paned Windows
paned_labels = ttk.PanedWindow(root, orient=tk.HORIZONTAL)
paned_labels.place(relx=0.995, anchor="ne") 
paned_labels.config(width=248, height=150, style="BW.TPanedwindow")

paned_buttons = ttk.PanedWindow(root, orient=tk.HORIZONTAL)
paned_buttons.place(relx=0.005, anchor="nw")
paned_buttons.config(width=248, height=150, style="BW.TPanedwindow")
# =====

# Widgets =====

# Texts
label1 = ttk.Label(paned_labels, text="Lid Status")
label_message = ttk.Label(paned_labels, text="Hand Refractometer Simulator")
label_value = ttk.Label(paned_labels, text="What Value do you get?")

label_group1 = ttk.Label(paned_buttons, text="=== Grouped Actions 1 ===", style="TLabel")
label_group2 = ttk.Label(paned_buttons, text="=== Grouped Actions 2 ===", style="TLabel")
label_group3 = ttk.Label(paned_buttons, text="=== Grouped Actions 3 ===", style="TLabel")

# Buttons.
button1 = ttk.Button(paned_buttons, text="button1")
button2 = ttk.Button(paned_buttons, text="button2")
button3 = ttk.Button(paned_buttons, text="button3")
button4 = ttk.Button(paned_buttons, text="button4")
button5 = ttk.Button(paned_buttons, text="button5")
buttonValue = ttk.Button(paned_buttons, text="buttonValue")
# =====

# =#====

# Layouts =====

# paned_labels group
label_message.place(x=10, y=10)
label1.place(x=10, y=50)
label_value.place(x=10, y=70)

# paned_buttons group
label_group1.grid(row=0, column=0, padx=5, columnspan=3)
button1.grid(row=1, column=0, padx=5, pady=5)
button2.grid(row=1, column=1, padx=5, pady=5)
button3.grid(row=2, column=0, padx=5, pady=5)
button4.grid(row=2, column=1, padx=5, pady=5)
button5.grid(row=2, column=2, padx=5, pady=5)
buttonValue.grid(row=3, column=0, padx=5, pady=5)

label_group2.grid(row=4, column=0, padx=5, columnspan=3)
label_group3.grid(row=5, column=0, padx=5, columnspan=3)
# =====

root.mainloop()