import tkinter as tk
import random

root = tk.Tk()
root.configure(width=800, height=600)
root.title("Rzut kością")

def roll():
    label["text"] = str(random.randint(1,6))

# Widzety
label = tk.Label(root, text="-", font="Times 24 bold")
label.grid()

button = tk.Button(root,
    text="Roll",
    width=25,
    height=5,
    command=roll,
)
button.grid()


root.mainloop()