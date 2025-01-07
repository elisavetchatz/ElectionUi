# Voting Application

This is a **Voting Application** implemented in Python using the `tkinter` library. It provides a graphical user interface (GUI) for participants to vote and view scores in a voting contest.

## Features

- **Participant Voting:** Allows multiple participants to assign scores to various dishes or items.
- **Dynamic Score Updates:** Displays a real-time leaderboard based on the scores.
- **Vote Management:** Handles and stores votes for each participant in a text file.
- **Intuitive Navigation:** Simplifies navigation between input fields for seamless voting.
- **View Submitted Votes:** Enables viewing of all submitted votes.

## Getting Started

### Prerequisites

Ensure you have Python 3 installed on your system. You can download it from the [official Python website](https://www.python.org/).

### Installation

1. Clone this repository or download the `voting_app.py` file.
2. Install required libraries (if not already installed):
   ```bash
   pip install tk

### Running the Application
1. Open a terminal or command prompt.
2. Navigate to the directory containing voting_app.py.
3. Run the script: ```python voting_app.py ```
4. The GUI window for the application will launch.

### How to Use
1. Participant Voting:

Each participant votes for the dishes displayed.
Assign scores by entering values in the input fields next to each dish.
Press the ```Submit Vote``` button after entering scores.
2. Real-Time Scores:

The right panel displays the current scores leaderboard.
Scores are updated dynamically after each vote.
3. View Votes:

Click the ```View Votes``` button to see all submitted votes.
Completion:

Once all participants have voted, the system will notify you that voting is complete.
4. File Structure
```voting_app.py```: The main application code.
```votes.txt```: A log file where all votes are stored for record-keeping.

### Customization
You can customize the application by editing the ```participant_data``` dictionary in the script. This dictionary contains the names of participants and their corresponding dishes or items to vote on.

Example:
```
self.participant_data = {
    "Participant 1": "Dish 1",
    "Participant 2": "Dish 2",
    ...
}
```

### Future Improvements

- Add support for exporting scores to a CSV or Excel file.
- Include participant authentication for enhanced vote security.
- Improve UI design and add theme customization options.4
### Screenshots
Coming soon...

### Contributing
Feel free to fork this repository and submit pull requests for improvements or new features.

### License
This project is licensed under the MIT License.

Developed with ❤️ in Python. Specifically designed for a Christmas gathering with the family!

