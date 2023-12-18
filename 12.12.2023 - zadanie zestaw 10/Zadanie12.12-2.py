import tkinter as tk
import random, time

root = tk.Tk()
root.configure(width=800, height=600)
root.title("Papier kamień nożyce")

player_guess = 0
computer_guess = 0
# 0 -> kamień
# 1 -> papier
# 2 -> nożyce
def setr():
    global player_guess
    player_guess = 0
    roll()

def setp():
    global player_guess
    player_guess = 1
    roll()

def sets():
    global player_guess
    player_guess = 2
    roll()

def roll():
    global computer_guess, image_list, player_guess
    computer_guess = random.randint(0,2)
    label["image"] = image_list[computer_guess]
    if player_guess == computer_guess:
        label0["text"] = "Draw"
    elif player_guess == 2 and computer_guess == 0:
        label0["text"] = "You Lose"
    elif player_guess == 0 and computer_guess == 2:
        label0["text"] = "You Win"
    elif player_guess > computer_guess:
        label0["text"] = "You Win"
    else: 
        label0["text"] = "You Lose"


# Obrazy
rps = tk.PhotoImage(file="rps.png")
rock = tk.PhotoImage(file="rock.png")
paper = tk.PhotoImage(file="paper.png")
scissors = tk.PhotoImage(file="scissors.png")

image_list = [rock, paper, scissors]

# Widzety
label = tk.Label(root, compound=tk.CENTER, image = rps, width = 300, height = 300)
label.grid()

label0 = tk.Label(root, text="", font="Times 36 bold")
label0.grid()

rbutton = tk.Button(root,
    text="Rock",
    width=25,
    height=5,
    command=setr,
)
rbutton.grid()

pbutton = tk.Button(root,
    text="Paper",
    width=25,
    height=5,
    command=setp,
)
pbutton.grid()

sbutton = tk.Button(root,
    text="Scissors",
    width=25,
    height=5,
    command=sets,
)
sbutton.grid()

root.mainloop()