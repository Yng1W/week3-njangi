PROJECT: NJANGI LEDGER

- This program manages a Njangi savings group by registering members, recording contributions, checking member totals, displaying a group summary, and saving/loading data from a JSON file. Run the program writing "python3 njangi.py" in your terminal and press Enter.

- I chose a "dictionary" because it allows fast lookup of members by name, while each value is a list containing that member's contribution history.

- One entry in the data file looks like this: ("Alice" : [5000, 3000, 2000]), where the key (on the left) is the member's name and the value (on the right) which is a list stores all contributions.

- On the first run, if "members.json" which is our DATA_FILE where data is been written to or retrieved from does not exist, the program catches the "FileNotFoundError" using the try/except, starts with an empty ledger, and continues without crashing.

- The hardest part of this project was understanding and implementing some of the concepts not taught in class, especially how "try/except" works for handling errors, how reading from and writing to JSON files works, implementing a class, using a module and a few smaller concepts related to file handling.

- Building and testing each function step by step helped me understand these ideas much better.



