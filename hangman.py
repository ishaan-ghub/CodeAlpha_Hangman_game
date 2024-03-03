import random

def choose_word():
    words = ["thor", "spiderman", "hulk", "ironman", "superman", "batman"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    max_attempts = 6
    guessed_letters = []
    word_to_guess = choose_word()
    attempts_left = max_attempts

    print("Welcome to Hangman!")
    print("Guess the names of the superheroes!")

    while attempts_left > 0:
        current_display = display_word(word_to_guess, guessed_letters)
        print(f"Current word: {current_display}")
        print(f"Attempts left: {attempts_left}")

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Enter a valid single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter. Try again!")
            continue

        guessed_letters.append(guess)

        if guess not in word_to_guess:
            print("Incorrect guess!")
            attempts_left -= 1

        if all(letter in guessed_letters for letter in word_to_guess):
            print("Congratulations! You guessed the word:", word_to_guess)
            return  # End the function if all letters are guessed

    print("Game over! Attempts finished. The word was:", word_to_guess)

if __name__ == "__main__":
    hangman()
