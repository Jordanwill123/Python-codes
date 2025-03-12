import random

# List of possible words
words = ["python", "elephant",]

# Pick a random word
secret_word = random.choice(words)

# Create dashes for the secret word
dashes = "-" * len(secret_word)

# Number of incorrect guesses allowed
guesses_left = 10


def get_guess():
    """Retrieve a valid single lowercase letter guess from the user."""
    while True:
        guess = input("Guess: ")
        if len(guess) != 1:
            print("Your guess must have exactly one character!")
        elif not guess.islower():
            print("Your guess must be a lowercase letter!")
        else:
            return guess


def update_dashes(secret_word, dashes, guess):
    """Update the dashes based on correct guesses."""
    result = ""
    for i in range(len(secret_word)):
        if secret_word[i] == guess:
            result += guess  # Reveal the guessed letter
        else:
            result += dashes[i]  # Keep previous dashes/letters
    return result


# Game loop
while dashes != secret_word and guesses_left > 0:
    print(dashes)
    print(f"{guesses_left} incorrect guesses left.")

    guess = get_guess()

    if guess in secret_word:
        print("That letter is in the word!")
        dashes = update_dashes(secret_word, dashes, guess)
    else:
        print("That letter is not in the word.")
        guesses_left -= 1

# End of game
if dashes == secret_word:
    print(f"Congrats! You win. The word was: {secret_word}")
else:
    print(f"You lose. The word was: {secret_word}")
