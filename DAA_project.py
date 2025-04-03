import tkinter as tk
from tkinter import messagebox
import math

def check_winner():
    global winner
    for combo in [[0,1,2], [3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]:
        if buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] != "":
            buttons[combo[0]].config(bg="green")
            buttons[combo[1]].config(bg="green")
            buttons[combo[2]].config(bg="green")
            winner = True
            messagebox.showinfo("Tic-Tac-Toe", f"Player {buttons[combo[0]]["text"]} wins!")
            root.quit()
    if all(button["text"] != "" for button in buttons) and not winner:
        messagebox.showinfo("Tic-Tac-Toe", "It's a tie!")
        root.quit()

def button_click(index):
    global current_player
    if buttons[index]["text"] == "" and not winner:
        buttons[index]["text"] = current_player
        check_winner()
        if not winner:
            toggle_player()
            if current_player == "o":
                ai_move()

def toggle_player():
    global current_player
    current_player = "x" if current_player == "o" else "o"
    label.config(text=f"Player {current_player}'s turn")

def minimax(board, depth, is_maximizing):
    for combo in [[0,1,2], [3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != "":
            return 1 if board[combo[0]] == "o" else -1
    if "" not in board:
        return 0
    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == "":
                board[i] = "o"
                score = minimax(board, depth + 1, False)
                board[i] = ""
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == "":
                board[i] = "x"
                score = minimax(board, depth + 1, True)
                board[i] = ""
                best_score = min(score, best_score)
        return best_score

def ai_move():
    best_score = -math.inf
    best_move = -1
    for i in range(9):
        if buttons[i]["text"] == "":
            buttons[i]["text"] = "o"
            score = minimax([b["text"] for b in buttons], 0, False)
            buttons[i]["text"] = ""
            if score > best_score:
                best_score = score
                best_move = i
    if best_move != -1:
        button_click(best_move)

root = tk.Tk()
root.title("Tic-Tac-Toe with Minimax AI")
buttons = [tk.Button(root, text="", font=("normal", 25), width=10, height=2, command=lambda i=i: button_click(i)) for i in range(9)]
for i, button in enumerate(buttons):
    button.grid(row=i // 3, column=i % 3)
current_player = "x"
winner = False
label = tk.Label(root, text=f"Player {current_player}'s turn", font=("normal", 16))
label.grid(row=3, column=0, columnspan=3)
root.mainloop()