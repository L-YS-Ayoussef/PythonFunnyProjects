# FlashyWords 🇫🇷📚  
A Simple French Vocabulary Flashcard App

## 🌍 Overview  
FlashyWords is a small desktop flashcard app built with Python and Tkinter.  
It helps you practice French vocabulary: a French word appears on a card, then flips to show the English meaning. You decide whether you knew the word or not, and the words you answer correctly are saved so you can review them later.

---

## 🚀 Features

- **Flashcard Flow**
  - Shows a **French** word on the front of the card.
  - After a short delay, the card flips to show the **English** meaning.
  - Nice card-front/card-back images for a more realistic flashcard feel.

- **Answer Buttons**
  - ✅ **Right** – you knew the word:
    - The word pair is added to your *learned words* list.
  - ❌ **Wrong** – you didn’t know the word:
    - The word stays in the pool and will appear again.

- **Learned Words Tracking**
  - Correctly answered words are saved into `words_to_learn.csv`.
  - On **Finish**, you can open a “Learned Words” window displaying a table:
    - Left column: French
    - Right column: English

- **Progress Persistence**
  - Uses CSV files for input (`french_words.csv`) and for learned words (`words_to_learn.csv`).
  - You can close and later inspect or reuse the learned words CSV.

---

## 🛠 Technologies Used

- **Python 3**
- **Tkinter** – GUI, buttons, windows
- **pandas** – reading and writing CSV word lists
- **random** – selecting a random word from the list

---

## ▶️ Quick Start: Run the App

1. **Clone the repo**

   ```bash
   git clone https://github.com/L-YS-Ayoussef/FlashyWords-French-Flashcard-Trainer.git
   cd FlashyWords-French-Flashcard-Trainer

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
   python Flash_Card_Project.py

## 🖼️ App Screenshots

### Flash Card
![Flash Card](https://github.com/L-YS-Ayoussef/FlashyWords-French-Flashcard-Trainer/blob/master/Screenshots/Screenshot1.png)

### Learned Words
![Learned Words](https://github.com/L-YS-Ayoussef/FlashyWords-French-Flashcard-Trainer/blob/master/Screenshots/Screenshot2.png)


## 📜 License
This project is **open-source** and available for anyone to use, modify, and distribute.

📌 **Copyright © 2025 Chameleon Tech** 
