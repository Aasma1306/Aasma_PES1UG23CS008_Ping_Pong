# Aasma_PES1UG23CS051_Ping_Pong
# 🏓 Ping Pong Game (Pygame)

A simple **Ping Pong (Pong)** game built with **Python** and **Pygame**.
The game includes different modes: **Best of 3**, **Best of 5**, and **Best of 7**.

---

## 🎮 Features

* Classic Pong mechanics with a bouncing ball and paddles.
* Player vs AI (computer-controlled opponent).
* Score display at the top of the screen.
* Game over screen announcing the winner.
* Start menu with game mode selection:

  * **Press 3** → Play Best of 3
  * **Press 5** → Play Best of 5
  * **Press 7** → Play Best of 7
  * **Press ESC** → Exit

---

## 📂 Project Structure

```
ping-pong/
├── main.py
├── requirements.txt
├── README.md
├── game/
│   ├── __init__.py
│   ├── ball.py
│   ├── paddle.py
│   └── game_engine.py
└── assets/   (optional for sounds/images)
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/ping-pong.git
cd ping-pong
```

### 2. Install dependencies

Make sure you have **Python 3.9+** installed. Then install the requirements:

```bash
pip install -r requirements.txt
```

### 3. Run the game

```bash
python3 main.py
```

---

## 🎵 Optional (Sound Effects)

You can add sound effects in the `assets/` folder (like `bounce.wav`, `score.wav`, etc.)
Modify the code to load and play them if you’d like enhanced gameplay.

---

## 🛠️ Requirements

* Python 3.9 or higher
* Pygame 2.6.1

---

