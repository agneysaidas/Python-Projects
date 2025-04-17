# 🎮 Hangman Game in Python 🐍

Welcome to the classic Hangman game, now in Python! Test your vocabulary and guessing skills in this fun and interactive word game.

---

## 📝 Description

This is a terminal-based Hangman game where:

- A random word is selected from a predefined list.
- You have 6 lives to guess the word correctly.
- Each incorrect guess brings the hangman closer to completion.
- The game ends when you either guess the word or run out of lives.

---

## 🚀 Getting Started

### 📁 Prerequisites

- Python 3.x installed on your system.

### 📦 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/agneysaidas/Python-Projects.git
   ```
2. **Navigate to the project directory:**
    ```bash
    cd hangman
    ```
3. **Ensure the following files are present:**
  - `hangman.py` – Main game script.
  - `hangman_words.py` – Contains the list of words.
  - `hangman_art.py`  – Contains the stages of the hangman and the game logo.

## 🎮 How to Play
1. **Run the game:**
   ```bash
   python hangman.py
   ```
2. **Game Flow:**
   - The game will display a logo and a series of underscores representing the hidden word.
   - Input one letter per guess.
   - Correct guesses reveal the letter in the word.
   - Incorrect guesses reduce your lives by one and update the hangman illustration.
   - The game continues until you guess the word or exhaust all lives.
## 📂 Project Structure
  ```bash
  hangman-game/
├── hangman.py
├── hangman_words.py
└── hangman_art.py
```
  - `hangman.py` – Main game script.
  - `hangman_words.py` – Contains the list of words.
  - `hangman_art.py`  – Contains the stages of the hangman and the game logo.
## 🎨 Features
- Random word selection from a diverse list.
- Visual representation of the hangman using ASCII art.
- Input validation to prevent repeated guesses.
- Clear display of game status after each guess.

## 💡 Future Enhancements
- Add difficulty levels (easy, medium, hard).
- Implement a scoring system.
- Develop a graphical user interface (GUI) version.
- Allow players to add their own words to the list.
## 🤝 Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

Enjoy the game and happy coding! 🎉
 
