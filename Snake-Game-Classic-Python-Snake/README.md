# Snake Game 🐍  
Classic Snake in Python with High Score Saving

## 🌍 Overview  
This project is a classic **Snake** game implemented in Python.  
You control a snake that moves around the screen, trying to eat blue food dots. Each time the snake eats, it grows longer and your score increases. If the snake hits a wall (or itself), the game resets and the score returns to 0. The **highest score** is saved in a text file so you can try to beat your personal best.

---

## 🚀 Features

- **Classic Snake Gameplay**
  - Move the snake around the screen to eat the blue food circle.
  - Each food eaten increases the score by **1** and makes the snake longer.

- **Collision Logic**
  - Hitting a border causes the game to reset.
  - Score goes back to **0** on reset.

- **Persistent High Score**
  - High score is stored in a `.txt` file.
  - If the player achieves a score higher than the saved one, the file is updated.

- **Score Display**
  - Current score and high score are displayed at the top of the game window.

---

## 🎮 Controls

- Arrow keys (`↑`, `↓`, `←`, `→`) – move the snake up, down, left, and right.

---

## 🛠 Technologies Used

- **Python 3**
- **turtle** module (for graphics and game loop)
- Basic file I/O for saving and loading the high score

---

## ▶️ Quick Start: Run the Game

1. **Clone the repo**

   ```bash
   git clone https://github.com/L-YS-Ayoussef/Snake-Game-Classic-Python-Snake.git
   cd Snake-Game-Classic-Python-Snake

2. **Create and activate a virtual environment**
- **Windows**:
   ```bash
   python -m venv venv
  venv\Scripts\activate
   
- **macOS / Linux**:
  ```bash
   python3 -m venv venv
  source venv/bin/activate
  
3. **Run the app**

   ```bash
   python main.py

## 🖼️ App Screenshots

### Snake Classic Game
![Snake Classic Game](https://github.com/L-YS-Ayoussef/Snake-Game-Classic-Python-Snake/blob/master/Screenshots/Screenshot1.png)


## 📜 License
This project is **open-source** and available for anyone to use, modify, and distribute.

📌 **Copyright © 2025 Chameleon Tech**
