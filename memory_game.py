import tkinter as tk
import random
from functools import partial
import time

# Game setup
root = tk.Tk()
root.title("🧠 Memory Game")
root.resizable(False, False)

# Game variables
tiles = list(range(1, 9)) * 2  # 8 pairs
random.shuffle(tiles)

buttons = []
first_click = None
second_click = None
matched = []
score = 0

# Functions
def check_match(i, btn):
    global first_click, second_click, score

    if btn in matched or btn == first_click:
        return

    btn.config(text=tiles[i], state='disabled')

    if not first_click:
        first_click = btn
    elif not second_click:
        second_click = btn
        root.update()
        root.after(500, evaluate_match)

def evaluate_match():
    global first_click, second_click, score

    i1 = buttons.index(first_click)
    i2 = buttons.index(second_click)

    if tiles[i1] == tiles[i2]:
        matched.extend([first_click, second_click])
        score += 1
    else:
        first_click.config(text="", state='normal')
        second_click.config(text="", state='normal')

    first_click = None
    second_click = None

    if len(matched) == len(tiles):
        end_label = tk.Label(root, text=f"🎉 You won! Score: {score}", font=("Arial", 14))
        end_label.grid(row=5, column=0, columnspan=4, pady=10)

# Layout
for i in range(4):
    for j in range(4):
        index = i * 4 + j
        btn = tk.Button(root, text="", width=6, height=3, font=("Arial", 16),
                        command=partial(check_match, index, None))
        btn.grid(row=i, column=j, padx=5, pady=5)
        buttons.append(btn)

# Assign command after buttons are all created
for i, btn in enumerate(buttons):
    btn.config(command=partial(check_match, i, btn))

root.mainloop()
