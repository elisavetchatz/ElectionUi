import tkinter as tk
from tkinter import messagebox

class VotingApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Voting UI")
        self.master.configure(bg="#2E2E2E")  # Σκούρο φόντο για εορταστική αίσθηση
        self.master.geometry("900x600")  # Αύξηση διαστάσεων παραθύρου

        # Αρχικοποίηση δεδομένων
        self.participants = 20
        self.participant_data = {
            "Καλλίτσα": "Μακαρονόπιτα Κ...αλλιώς", 
            "Καλλίτσα2": "Φτερουγίσματα με Κασέρια", 
            "Μαρία Μικρή": "Σαλάτα της Χοληστερίνης", 
            "Μαρία Μικρή2": "Ρολό Κιμά-> Απόπειρα 2",
            "Άρης": "Sevasto...bai",
            "Κοσμάς": "brownies του Κόσμου", 
            "Σοφούλα": "Κοτόπουλο Γεμιστό",
            "Χριστίνα Χ.": "Του κολοκυθιού τα εννιάμερα",
            "Σλβάνα": "Σοφρίτο αλά... Σεβαστιώτα",
            "Γιάννης και Δημήτρης": "Μοσχάρι Κρασάτο με Μεθυσμένες Πατάτες",
            "Χριστίνα Β": "Ψαρονεύρι με ρύζι",
            "Μαρία Όμορφη": "Banana CAKE",
            "Μαρία Όμορφη και Σταυρούλα": "Φωλίτσες",
            "Πάολα": "Σνιτσελόνια με Ντιπ",
            "Ελένη": "Μπισκοτίνια με Εσάνς... Μελομακάρονο"
        
        }
        self.scores = {f"{name} - {plate}": 0 for name, plate in self.participant_data.items()}
        self.player_votes = {}
        self.current_player = 1

        # Δημιουργία UI
        self.create_widgets()

    def create_widgets(self):
        # Κύριο πλαίσιο
        self.main_frame = tk.Frame(self.master, bg="#2E2E2E")
        self.main_frame.pack(pady=10, padx=10)

        # Πλαίσιο ψηφοφορίας
        self.voting_frame = tk.Frame(self.main_frame, bg="#2E2E2E")
        self.voting_frame.pack(side=tk.LEFT, padx=20)

        # Ετικέτα για τον παίκτη
        self.player_label = tk.Label(
            self.voting_frame,
            text=f"Player {self.current_player}",
            font=("Ubuntu", 16, "bold"),
            fg="#FFFFFF",
            bg="#2E2E2E"
        )
        self.name_label.pack()

        self.name_entry = tk.Entry(self.voting_frame, width=30, bg="#D5E8D4", font=("Ubuntu", 12))
        self.name_entry.pack(pady=5)

        # Πεδίο καταχώρισης ψήφων
        self.entries = []
        for name, plate in self.participant_data.items():
            frame = tk.Frame(self.voting_frame, bg="#2E2E2E")
            frame.pack(pady=5)  # Αυξημένο κενό μεταξύ των στοιχείων

            label = tk.Label(frame, text=f"{name} - {plate}", width=30, anchor="w", fg="#FFFFFF", bg="#2E2E2E", font=("Ubuntu", 12))
            label.pack(side=tk.LEFT)

            entry = tk.Entry(frame, width=5, bg="#D5E8D4", font=("Ubuntu", 12))
            entry.pack(side=tk.LEFT)
            entry.bind("<Down>", self.focus_next_entry)
            entry.bind("<Up>", self.focus_previous_entry)
            self.entries.append(entry)

        # Κουμπί υποβολής
        self.submit_button = tk.Button(
            self.voting_frame,
            text="Submit Vote",
            command=self.submit_vote,
            bg="#FF5733",
            fg="#FFFFFF",
            font=("Ubuntu", 12, "bold")
        )
        self.submit_button.pack(pady=10)

        # Πλαίσιο βαθμολογίας
        self.score_frame = tk.Frame(self.main_frame, relief=tk.SUNKEN, borderwidth=2, bg="#4CAF50", width=600, height=600)
        self.score_frame.pack_propagate(False)
        self.score_frame.pack(side=tk.LEFT, padx=10, fill=tk.BOTH, expand=True)

        self.score_label_title = tk.Label(self.score_frame, text="Scores", font=("Ubuntu", 16, "bold"), fg="#FFFFFF", bg="#4CAF50")
        self.score_label_title.pack(pady=10)

        self.score_text = tk.StringVar()
        self.score_label = tk.Label(self.score_frame, textvariable=self.score_text, font=("Ubuntu", 14), justify="left", fg="#FFFFFF", bg="#4CAF50", pady=5)
        self.score_label.pack(pady=10)

        self.update_scores()

        # Κουμπί προβολής ψήφων
        self.view_button = tk.Button(
            self.main_frame,
            text="View Votes",
            command=self.view_votes,
            bg="#FF5733",
            fg="#FFFFFF",
            font=("Ubuntu", 12, "bold")
        )
        self.view_button.pack(side=tk.BOTTOM, pady=10)

    def focus_next_entry(self, event):
        widget = event.widget
        index = self.entries.index(widget)
        if index < len(self.entries) - 1:
            self.entries[index + 1].focus()
        return "break"

    def focus_previous_entry(self, event):
        widget = event.widget
        index = self.entries.index(widget)
        if index > 0:
            self.entries[index - 1].focus()
        return "break"

    def submit_vote(self):
        try:
            vote = [int(entry.get()) for entry in self.entries]
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers.")
            return

        if not all(1 <= v <= 10 for v in vote):
            messagebox.showerror("Error", "Please enter numbers between 1 and 10.")
            return

        if len(vote) != len(self.participant_data):
            messagebox.showerror("Error", "Please provide a score for every plate.")
            return

        # Καταχώριση ψήφου
        self.player_votes[f"Player {self.current_player}"] = vote
        for (name, plate), rank in zip(self.participant_data.items(), vote):
            self.scores[f"{name} - {plate}"] += rank

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
        sorted_scores = sorted(self.scores.items(), key=lambda x: x[1], reverse=True)
        self.score_text.set("\n".join([f"{plate}: {score}" for plate, score in sorted_scores]))

    def view_votes(self):
        votes_text = "\n".join([f"{player}: {votes}" for player, votes in self.player_votes.items()])
        messagebox.showinfo("Player Votes", votes_text)

# Εκκίνηση εφαρμογής
if __name__ == "__main__":
    root = tk.Tk()
    app = VotingApp(root)
    root.mainloop()

