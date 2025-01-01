import tkinter as tk
from tkinter import ttk, messagebox

participants = 10
plates = [f"Plate {i+1}" for i in range(10)]
scores = {plate: 0 for plate in plates}
player_votes = {}

# Συνάρτηση για την καταχώριση ψήφων
current_player = 1
def submit_vote():
    global current_player

    try:
        vote = [int(entry.get()) for entry in entries]
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")
        return

    if sorted(vote) != list(range(1, len(plates) + 1)):
        messagebox.showerror("Error", "Please rank all plates uniquely from 1 to 20.")
        return

    # Καταχώριση ψήφου
    player_votes[f"Player {current_player}"] = vote
    for plate, rank in zip(plates, vote):
        scores[plate] += rank

    # Αποθήκευση ψήφων σε αρχείο
    with open("votes.txt", "a") as file:
        file.write(f"Player {current_player}: {vote}\n")

    # Ενημέρωση βαθμολογίας
    update_scores()

    # Ενημέρωση παίκτη
    current_player += 1
    if current_player > participants:
        messagebox.showinfo("Voting Complete", "All participants have voted!")
        submit_button["state"] = "disabled"
    else:
        player_label.config(text=f"Player {current_player}")
        for entry in entries:
            entry.delete(0, tk.END)

def update_scores():
    sorted_scores = sorted(scores.items(), key=lambda x: x[1])
    score_text.set("\n".join([f"{plate}: {score}" for plate, score in sorted_scores]))

def view_votes():
    votes_text = "\n".join([f"{player}: {votes}" for player, votes in player_votes.items()])
    messagebox.showinfo("Player Votes", votes_text)

# Δημιουργία παραθύρου
window = tk.Tk()
window.title("Voting UI")

# Κύριο πλαίσιο
main_frame = tk.Frame(window)
main_frame.pack(pady=10, padx=10)

# Πλαίσιο ψηφοφορίας
voting_frame = tk.Frame(main_frame)
voting_frame.pack(side=tk.LEFT, padx=10)

# Ετικέτα για τον παίκτη
player_label = tk.Label(window, text=f"Player {current_player}", font=("Arial", 16))
player_label.pack(pady=10)

# Πεδίο καταχώρισης ψήφων
entries = []
for plate in plates:
    frame = tk.Frame(window)
    frame.pack(pady=2)

    label = tk.Label(frame, text=plate, width=20, anchor="w")
    label.pack(side=tk.LEFT)

    entry = tk.Entry(frame, width=5)
    entry.pack(side=tk.LEFT)
    entries.append(entry)

# Κουμπί υποβολής
submit_button = tk.Button(window, text="Submit Vote", command=submit_vote)
submit_button.pack(pady=10)

# Πλαίσιο βαθμολογίας
score_frame = tk.Frame(main_frame, relief=tk.SUNKEN, borderwidth=2)
score_frame.pack(side=tk.RIGHT, padx=10, fill=tk.Y)

score_label_title = tk.Label(score_frame, text="Scores", font=("Arial", 16))
score_label_title.pack(pady=10)

score_text = tk.StringVar()
score_label = tk.Label(score_frame, textvariable=score_text, font=("Arial", 14), justify="left")
score_label.pack(pady=10)
update_scores()

# Κουμπί προβολής ψήφων
view_button = tk.Button(window, text="View Votes", command=view_votes)
view_button.pack(pady=10)

# Εκκίνηση εφαρμογής
window.mainloop()
