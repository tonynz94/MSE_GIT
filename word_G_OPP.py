import random
import string


class WordGuessGame:
    # Word bank the secret word is picked from
    WORDS = [
        "python", "variable", "function", "iterator", "notebook",
        "pipeline", "dataset", "computer", "research", "analytics"
    ]

    def __init__(self, max_lives=6):
        # Game state lives on the instance instead of being passed around
        self.secret = random.choice(self.WORDS)
        self.blanks = ["_" for _ in self.secret]
        self.lives = max_lives
        self.used_letters = set()

    def prompt_for_letter(self):
        # Keep asking until a valid, unused single letter is entered
        while True:
            guess = input("Guess a letter: ").strip().lower()
            if len(guess) != 1 or guess not in string.ascii_lowercase:
                print(" → Please enter a single A-Z letter.")
                continue
            if guess in self.used_letters:
                print(" → You already tried that letter.")
                continue
            return guess

    def reveal_letters(self, letter):
        # Fill in every blank that matches the guessed letter
        found_any = False
        for i, ch in enumerate(self.secret):
            if ch == letter and self.blanks[i] == "_":
                self.blanks[i] = letter
                found_any = True
        return found_any

    def is_solved(self):
        # True when no blanks remain
        return "_" not in self.blanks

    def show_blanks(self):
        print(" ".join(self.blanks))

    def play(self):
        print("\nWelcome to Word Guessing!")
        print(f"The word has {len(self.secret)} letters.")
        self.show_blanks()

        while True:
            # Ask the user to guess a letter
            guess = self.prompt_for_letter()
            self.used_letters.add(guess)

            # Is the guessed letter in the word?
            if self.reveal_letters(guess):
                print("\n Well done, Nice job! You found a letter.")
                self.show_blanks()
                # Are all blanks filled?
                if self.is_solved():
                    print("\n Congratulation! You guessed the word!")
                    print(f"Word: {self.secret}")
                    print("GAME OVER")
                    break
            else:
                # Lose a life
                self.lives -= 1
                print(f"\nNope. You lose a life. Lives left: {self.lives}")
                self.show_blanks()

                # Have they run out of lives?
                if self.lives <= 0:
                    print("\n Out of lives & Sad story!")
                    print(f"The word was: {self.secret}")
                    print("GAME OVER")
                    break

            # (loop continues to ask for another letter)


if __name__ == "__main__":
    WordGuessGame().play()
