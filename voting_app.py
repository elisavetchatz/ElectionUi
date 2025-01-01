import tkinter as tk
from tkinter import messagebox

class VotingApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Voting UI")

        # Αρχικοποίηση δεδομένων
        self.participants = 20
        self.plates = [f"Plate {i+1}" for i in range(20)]
        self.scores = {plate: 0 for plate in self.plates}
        self.player_votes = {}
        self.current_player = 1

        # Δημιουργία UI
        self.create_widgets()

    def create_widgets(self):
        # Κύριο πλαίσιο
        self.main_frame = tk.Frame(self.master)
        self.main_frame.pack(pady=10, padx=10)

        # Πλαίσιο ψηφοφορίας
        self.voting_frame = tk.Frame(self.main_frame)
        self.voting_frame.pack(side=tk.LEFT, padx=10)

        # Ετικέτα για τον παίκτη
        self.player_label = tk.Label(self.voting_frame, text=f"Player {self.current_player}", font=("Arial", 16))
        self.player_label.pack(pady=10)

        # Πεδίο καταχώρισης ψήφων
        self.entries = []
        for plate in self.plates:
            frame = tk.Frame(self.voting_frame)
            frame.pack(pady=2)

            label = tk.Label(frame, text=plate, width=20, anchor="w")
            label.pack(side=tk.LEFT)

            entry = tk.Entry(frame, width=5)
            entry.pack(side=tk.LEFT)
            self.entries.append(entry)

        # Κουμπί υποβολής
        self.submit_button = tk.Button(self.voting_frame, text="Submit Vote", command=self.submit_vote)
        self.submit_button.pack(pady=10)

        # Πλαίσιο βαθμολογίας
        self.score_frame = tk.Frame(self.main_frame, relief=tk.SUNKEN, borderwidth=2)
        self.score_frame.pack(side=tk.LEFT, padx=10, fill=tk.BOTH, expand=True)

        self.score_label_title = tk.Label(self.score_frame, text="Scores", font=("Arial", 16))
        self.score_label_title.pack(pady=10)

        self.score_text = tk.StringVar()
        self.score_label = tk.Label(self.score_frame, textvariable=self.score_text, font=("Arial", 14), justify="left")
        self.score_label.pack(pady=10)

        self.update_scores()

        # Κουμπί προβολής ψήφων
        self.view_button = tk.Button(self.main_frame, text="View Votes", command=self.view_votes)
        self.view_button.pack(side=tk.BOTTOM, pady=10)

    def submit_vote(self):
        try:
            vote = [int(entry.get()) for entry in self.entries]
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers.")
            return

        if sorted(vote) != list(range(1, len(self.plates) + 1)):
            messagebox.showerror("Error", "Please rank all plates uniquely from 1 to 20.")
            return

        # Καταχώριση ψήφου
        self.player_votes[f"Player {self.current_player}"] = vote
        for plate, rank in zip(self.plates, vote):
            self.scores[plate] += rank

        # Αποθήκευση ψήφων σε αρχείο
        with open("votes.txt", "a") as file:
            file.write(f"Player {self.current_player}: {vote}\n")

        # Ενημέρωση βαθμολογίας
        self.update_scores()

        # Ενημέρωση παίκτη
        self.current_player += 1
        if self.current_player > self.participants:
            messagebox.showinfo("Voting Complete", "All participants have voted!")
            self.submit_button["state"] = "disabled"
        else:
            self.player_label.config(text=f"Player {self.current_player}")
            for entry in self.entries:
                entry.delete(0, tk.END)

    def update_scores(self):
        sorted_scores = sorted(self.scores.items(), key=lambda x: x[1])
        self.score_text.set("\n".join([f"{plate}: {score}" for plate, score in sorted_scores]))

    def view_votes(self):
        votes_text = "\n".join([f"{player}: {votes}" for player, votes in self.player_votes.items()])
        messagebox.showinfo("Player Votes", votes_text)

# Εκκίνηση εφαρμογής
if __name__ == "__main__":
    root = tk.Tk()
    app = VotingApp(root)
    root.mainloop()
