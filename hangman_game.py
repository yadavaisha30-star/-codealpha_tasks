import random

words = [
    "python",
    "computer",
    "programming",
    "developer",
    "keyboard",
    "internet",
    "laptop",
    "hangman",
    "software",
    "technology"
]

word = random.choice(words)
guessed_letters = []
wrong_guesses = 0
max_attempts = 6

print("=" * 50)
print("           WELCOME TO HANGMAN GAME")
print("=" * 50)

display_word = ["_" for _ in word]

while wrong_guesses < max_attempts and "_" in display_word:

    print("\nWord:", " ".join(display_word))
    print("Guessed Letters:", ", ".join(guessed_letters))
    print("Remaining Attempts:", max_attempts - wrong_guesses)

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct Guess!")

        for i in range(len(word)):
            if word[i] == guess:
                display_word[i] = guess
    else:
        print("Wrong Guess!")
        wrong_guesses += 1

        print("\nHangman Status:")

        stages = [
            """
               -----
               |   |
                   |
                   |
                   |
                   |
            =========
            """,
            """
               -----
               |   |
               O   |
                   |
                   |
                   |
            =========
            """,
            """
               -----
               |   |
               O   |
               |   |
                   |
                   |
            =========
            """,
            """
               -----
               |   |
               O   |
              /|   |
                   |
                   |
            =========
            """,
            """
               -----
               |   |
               O   |
              /|\\  |
                   |
                   |
            =========
            """,
            """
               -----
               |   |
               O   |
              /|\\  |
              /    |
                   |
            =========
            """,
            """
               -----
               |   |
               O   |
              /|\\  |
              / \\  |
                   |
            =========
            """
        ]

        print(stages[wrong_guesses])

if "_" not in display_word:
    print("\n🎉 Congratulations!")
    print("You guessed the word:", word)
else:
    print("\n❌ Game Over!")
    print("The correct word was:", word)

print("=" * 50)
print("Thank You For Playing Hangman Game")
print("=" * 50)