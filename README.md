# 🐍 Python Mini Projects
This repository contains a collection of beginner-to-intermediate Python projects exploring core programming concepts, games, and basic API usage.

---

## 📂 Projects Breakdown

| File Name         | Description                                                                            |
|------------------|----------------------------------------------------------------------------------------|
| `HelloTwitter.py` | A Twitter API experiment using Tweepy to authenticate and interact with accounts      |
| `TicTacToe.py`    | Classic two-player Tic Tac Toe game with computer AI and board visuals                |
| `hangman.py`      | A word-guessing game with lives, letter tracking, and visual feedback                 |
| `hangman_visual.py` | ASCII visual representation for Hangman lives (used in `hangman.py`)               |
| `madlibs.py`      | A fill-in-the-blanks style word game using Python string manipulation                |
| `words.py`        | A word list used for the Hangman and MadLib games (imports into other files)         |

---

## 🚀 How to Run These Projects

1. Make sure Python 3 is installed on your system.
2. Clone this repository:
   ```bash
   git clone https://github.com/iamkimbert/PythonProjects-.git
   cd PythonProjects-
   ```
3. Run any script using:
   ```bash
   python filename.py
   ```

For example:
```bash
python TicTacToe.py
```

---

## 🧐 MadLib Game Example (madlibs.py)

This mini-game prompts the user for random words to generate a silly sentence. Example snippet:

```python
# string concatenation (aka how to put strings together)
# suppose we want to create a string that says "Subscribe to ________"
# youtuber = "vsuofficialchannel" #some string variable

# a few ways to do this:
# print("subscribe to " + youtuber)
# print("subscribe to {}".format(youtuber))
# print(f"subscribe to {youtuber}")

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous Person: ")

madlib = f"Computer programming is so {adj}! It makes me so excited all the time because I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"
print(madlib)
```

This game also pulls from a list of random words in `words.py`.

---

## 💠 Project Notes

### HelloTwitter.py
- Uses the [Tweepy](https://docs.tweepy.org/en/stable/) library
- Requires a Twitter Developer Account and API keys
- Make sure to insert your actual `CONSUMER_KEY`, `ACCESS_TOKEN`, etc.

### Hangman
- Uses visual ASCII from `hangman_visual.py`
- Imports `words.py` for random word selection

---

## 💡 Ideas for Future Enhancements

- Add GUI versions of the games using `tkinter`
- Create an interactive CLI menu for selecting games
- Use `.env` to store Twitter API keys securely
- Add unit tests for core functions

---

## 👩🏾‍💻 Author

**Kimberly Townsend**  
Masters in Computer Science | Virginia State University  
Passionate about software development, automation, and educational tech.

---

## 📜 License

This repository is licensed under the MIT License.

