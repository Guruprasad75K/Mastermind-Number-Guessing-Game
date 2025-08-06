# 🎯 Mastermind Number Guessing Game (2-Player Fun!)

This is a fun two-player Python game where you and a friend test each other’s brainpower in a game of hidden 4-digit numbers! One sets the number, and the other tries to guess it — but here’s the twist: you’ll only see which digits are right and in the correct place, shown as hints!


## 🕹️ How to Play:

1. Two players enter their names.
2. **Player 1** sets a secret 4-digit number (between 1000 and 9999). It’s hidden from Player 2 using `getpass`!
3. **Player 2** guesses the number.
   - After each guess, you'll get a hint:
     - Correct digits in the correct positions are shown.
     - Incorrect digits are replaced with **`X`**.
4. The number of attempts is recorded.
5. Then roles switch — Player 2 sets a number, and Player 1 guesses.
6. The player who guesses in fewer tries becomes the **Mastermind!**
7. You’ll be asked if you want to play again. Choose wisely 😄


## 🧠 Example Hint:

If the secret number is `4267` and you guessed `1234`, you might see:

X2XX
Not quite the number. You did get 1 digits correct.


## 🚀 Why It's Fun:

- 🔐 Hidden secrets!
- 🧠 Logical thinking!
- 😄 Friendly competition!
- 🖥️ Just run the script and start playing!


Enjoy the game and find out who the real **Mastermind** is!
