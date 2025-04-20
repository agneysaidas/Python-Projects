# 📈 Higher or Lower: Instagram Followers Edition

A simple and fun command-line game built in Python where you guess who has more Instagram followers between two famous people or brands.

## 🚀 How It Works

- Two random Instagram accounts are shown to you.
- You have to guess which one has more followers by typing `"A"` or `"B"`.
- If you're correct, your score increases and the game continues.
- If you're wrong, the game ends and your final score is displayed.

## 🧠 Game Logic

- The game pulls from a dataset of celebrities, influencers, brands, and public figures.
- It compares follower counts, but you only see descriptions and names — not the numbers!
- One correct guess leads to the next round with the previous "B" becoming the new "A".

## 🗂️ Project Structure

```bash
📁 higher-lower-game/ 
├── 📜 main.py # Main game logic 
├── 📜 game_data.py # List of Instagram accounts and follower data 
├── 📜 art.py # ASCII art for logo and VS graphic 
└── 📄 README.md # You're here!
```


## ▶️ How to Play

1. **Clone or download** the repository.
2. Make sure you have Python 3 installed.
3. Run the game:

```bash
python main.py
```

## 🧩 Example Output
```bash
Compare A: Cristiano Ronaldo, a Footballer, from Portugal
VS
Against B: Ariana Grande, a Musician and actress, from United States

Who has more followers? Type 'A' or 'B':
```


