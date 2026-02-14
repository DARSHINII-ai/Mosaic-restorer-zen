# The Mosaic Restorer 🧩✨

An experimental, Zen-inspired puzzle game built with Python. 

## 💡 Concept
"The Mosaic Restorer" is a cognitive-ease puzzle designed to reduce stress. Unlike traditional games that focus on high-speed reactions or "winning," this project explores **Restorative Gameplay**—the psychological satisfaction of bringing order to a randomized system.

## 🛠️ Technical Implementation
- Architecture: Object-Oriented Programming (OOP) using Python's `tkinter`.
- Logic: Matrix-based state management and 2D-array comparison algorithms.
- Design Philosophy:** Minimalist UI with a restricted pastel palette to ensure visual harmony.

## 🧠 Logic & Interview Talking Points
If you are reviewing this code for recruitment, here are the core concepts I implemented:

1. **State-Cycling Algorithm:** Clicking a tile cycles through a fixed list of Hex colors using the Modulo Operator (%), ensuring infinite, circular state transitions.
2. **Matrix Comparison:** The game logic performs a nested loop comparison between the User Grid (current state) and a Hidden Master Matrix (target state) to validate completion.
3. **Non-Punitive UX:** I intentionally removed "fail states" or "Game Over" screens to maintain a flow state, rewarding exploration rather than just accuracy.

## 🚀 How to Run
1. Ensure you have Python installed.
2. Download `mosaic_game.py`.
3. Run `python mosaic_game.py`.
4. **Note:** This project uses the built-in `tkinter` library, so no external modules (like Pygame) are required!
5.# Mosaic-restorer-zen
