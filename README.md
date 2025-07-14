🎯 Mastermind – Color Code Guessing Game (Python CLI)
A terminal-based Python implementation of the classic Mastermind game. The computer generates a secret code of 4 colors, and your task is to crack it within a limited number of guesses. After each guess, you'll receive hints to help you get closer to the solution!

🧠 How the Game Works:
🎨 Colors to choose from: R (Red), G (Green), B (Blue), Y (Yellow), W (White), O (Orange)

🔢 Code Length: 4 colors (can be repeated)

🎯 Guess Limit: 10 tries

✅ After each guess, you'll see:

Correct positions: right color in the right place

Incorrect positions: right color in the wrong place

📜 Rules
1. The computer randomly selects a 4-color code from 6 options.

2. You must input your guess in the format: R G B Y

3. After each guess, you’ll get feedback on how close you are.

Guess correctly within 10 tries to win.

If you exceed the guess limit, the correct code is revealed and you lose.

🧪 Sample Gameplay

Welcome to mastermind, you have 10 tries to guess the code...

Guess the code, length is 4 colors, choices are ['R', 'G', 'B', 'Y', 'W', 'O']

Guess: R G B Y

Correct positions: 2 | Incorrect positions: 1

Guess: G W O R

Correct positions: 4 | Incorrect positions: 0

You guessed in 2 tries.
