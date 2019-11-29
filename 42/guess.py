import random

MAX_GUESSES = 5
START, END = 1, 20


def get_random_number():
    """Get a random number between START and END, returns int"""
    return random.randint(START, END)


class Game:
    """Number guess class, make it callable to initiate game"""

    def __init__(self):
        """Init _guesses, _answer, _win to set(), get_random_number(), False"""
        self._guesses = set()
        self._answer = get_random_number()
        self._win = False

    def guess(self):
        """Ask user for input, convert to int, raise ValueError outputting
           the following errors when applicable:
           'Please enter a number'
           'Should be a number'
           'Number not in range'
           'Already guessed'
           If all good, return the int"""
        user_input = input("Guess a number between 1 and 20: ")
        if not user_input:
            # print("Please enter a number")
            raise ValueError("Please enter a number")
        try:
            user_input = int(user_input)
        except ValueError:
            # print("Should be a number")
            raise ValueError("Should be a number")
        if user_input < START or user_input > END:
            # print("Number not in range")
            raise ValueError("Number not in range")
        if user_input in self._guesses:
            # print("Already guessed")
            raise ValueError("Already guessed")
        self._guesses.add(user_input)
        return user_input

    def _validate_guess(self, guess):
        """Verify if guess is correct, print the following when applicable:
           {guess} is correct!
           {guess} is too low
           {guess} is too high
           Return a boolean"""
        if guess == self._answer:
            print(f"{guess} is correct!")
            return True
        elif guess > self._answer:
            print(f"{guess} is too high")
        elif guess < self._answer:
            print(f"{guess} is too low")
        return False

    def __call__(self):
        """Entry point / game loop, use a loop break/continue,
           see the tests for the exact win/lose messaging"""
        while not self._win and len(self._guesses) < MAX_GUESSES:
            try:
                g = self.guess()
                if not g:
                    continue
                self._guesses.add(g)
                if self._validate_guess(g):
                    self._win = True
                    break
            except ValueError as e:
                print(e)
        if self._win:
            print(f"It took you {len(self._guesses)} {'guess' if len(self._guesses) == 1 else 'guesses'}")
        else:
            print(f"Guessed {MAX_GUESSES} times, answer was {self._answer}")


if __name__ == '__main__':
    game = Game()
    game()
