import tkinter as tk
from tkinter import messagebox
from random import randint

# Initialize main window
root = tk.Tk()
root.title("Guess the Number")
root.geometry("500x500+600+200")
root.config(bg="#FFF176")

# Game variables
secret_number = randint(1, 100)
attempts_left = 10
wins = 0
losses = 0

def reset_game():
    global secret_number, attempts_left
    secret_number = randint(1, 100)
    attempts_left = 10
    feedback_label.config(text="")
    guess_entry.delete(0, tk.END)
    number_display.config(text="??")
    status_label.config(text=f"Attempts Left: {attempts_left}")

def update_score():
    score_label.config(text=f"Wins: {wins} | Losses: {losses}")

def check_guess():
    global attempts_left, wins, losses
    try:
        guess = int(guess_entry.get())
    except ValueError:
        messagebox.showwarning("Invalid input", "Please enter a valid number!")
        return

    if guess == secret_number:
        feedback_label.config(text="🎉 You guessed it right!")
        number_display.config(text=str(secret_number))
        wins += 1
        update_score()
        root.update()
        restart = messagebox.askyesno("YOU WON", "Do You Want To Play Again?")
        if restart:
            reset_game()
        else:
            root.quit()
    else:
        attempts_left -= 1
        if guess > secret_number:
            feedback_label.config(text="⬇️ Lower number please!")
        else:
            feedback_label.config(text="⬆️ Higher number please!")
        status_label.config(text=f"Attempts Left: {attempts_left}")
        if attempts_left == 0:
            feedback_label.config(text=f"You lose! The correct number was {secret_number}")
            number_display.config(text=str(secret_number))
            losses += 1
            update_score()
            root.update()
            restart = messagebox.askyesno("YOU LOSE", "Do You Want To Play Again?")
            if restart:
                reset_game()
            else:
                root.quit()

# Header Frame
header_frame = tk.Frame(root, bg="#FF8A65", height=70)
header_frame.pack(fill=tk.X)
title_label = tk.Label(header_frame, text="~ GUESS THE NUMBER ~", font=("Times New Roman", 24, "bold"), bg="#FF8A65", fg="#000000")
title_label.pack(pady=15)

# Decorative line
line = tk.Frame(root, bg="#F4511E", height=5)
line.pack(fill=tk.X)

# Number display
number_display = tk.Label(root, text="??", font=("Times New Roman", 36, "bold"), bg="#FFF176", fg="#000000")
number_display.pack(pady=20)

# Guess Entry
guess_entry = tk.Entry(root, font=("Times New Roman", 20, "bold"), justify="center", width=10, bd=3)
guess_entry.pack()

# Feedback Label
feedback_label = tk.Label(root, text="", font=("Times New Roman", 16, "bold"), bg="#FFF176", fg="#000000")
feedback_label.pack(pady=10)

# Guess Button
guess_button = tk.Button(root, text="Guess", font=("Times New Roman", 18, "bold"), command=check_guess, bg="#4CAF50", fg="#000000", width=10)
guess_button.pack(pady=10)

# Attempts Left
status_label = tk.Label(root, text=f"Attempts Left: {attempts_left}", font=("Times New Roman", 14, "bold"), bg="#FFF176", fg="#000000")
status_label.pack()

# Score
score_label = tk.Label(root, text=f"Wins: {wins} | Losses: {losses}", font=("Times New Roman", 14, "bold"), bg="#FFF176", fg="#000000")
score_label.pack(pady=10)

# Exit and Restart Buttons
bottom_frame = tk.Frame(root, bg="#FFF176")
bottom_frame.pack(pady=10)

restart_button = tk.Button(bottom_frame, text="Restart", command=reset_game, bg="#FFB74D", fg="#000000", font=("Times New Roman", 12, "bold"), width=10)
restart_button.pack(side=tk.LEFT, padx=10)

exit_button = tk.Button(bottom_frame, text="Exit", command=root.quit, bg="#EF5350", fg="#000000", font=("Times New Roman", 12, "bold"), width=10)
exit_button.pack(side=tk.LEFT, padx=10)

root.mainloop()