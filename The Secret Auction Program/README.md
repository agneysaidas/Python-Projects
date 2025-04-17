# 🏆 Silent Auction Program

Welcome to the **Silent Auction Program**! This Python script allows multiple participants to place bids in a simple text-based auction system. At the end of the bidding process, the script announces the winner with the highest bid. 💰

---

## 📜 Features

- 🔢 Collects multiple bids from different participants.
- 🤫 Keeps the bids hidden from other users (simulated by clearing the screen).
- 🥇 Determines the highest bidder and announces the winner.
- 🎨 Displays a cool ASCII art logo at the start using the `art` module.

---

## 🧠 How It Works

1. The program starts by printing an ASCII logo.
2. It repeatedly asks for:
   - The participant's name.
   - Their bid amount (as a number).
3. After each bid, it asks whether there are more participants.
4. Once all bids are collected, it finds the highest bid and prints the winner’s name and bid amount.

---

## 🖥️ Sample Output
```yaml
What is your name?: Alice 
What's your bid: 500 
Are there any other bid? type 'yes' or 'no': yes

What is your name?: Bob 
What's your bid: 1200 
Are there any other bid? type 'yes' or 'no': no

The winner is Bob with a bid of ₹1200
```

## 🚀 How to Run
1. Clone or download this script.
2. Make sure you have Python installed.
3. Install the required art module.
4. Run the script:
   ```bash
   python auction.py
   ```
## 🛠️ Customization Ideas

- Add input validation (e.g., check if bid is a positive number).
- Handle tie cases where multiple participants place the same highest bid.
- Use a proper screen clearing method (os.system('cls' or 'clear')) for better terminal experience.
- Save bid history to a file.

## 📃 License
This project is open for learning and fun purposes! 🎉

Happy Bidding! 🧑‍⚖️💸
