import random
class RandomNumberGenerator:
    # creates random int number between min and max value.
    def get_random_number(self, min, max):
        return random.randint(min, max)


class GuessingGame:
    def __init__(self, generator:RandomNumberGenerator, attempt_limit) -> None:
        self.target_number = generator.get_random_number(1,100)
        self.attempts = [] # all attempts from player.
        self.flag = None # True for win, False for lose
        self.attempt_limit = attempt_limit
    
    # returns user input as int
    def get_user_input(self):
        guess = int(input("Guess a number between 1 and 100: "))
        return guess

    def check_guess(self, guess):
        self.attempts.append(guess)
        if guess == self.target_number:
            self.flag = True
            print("Correct, you won!")
            message = "Correct, you won!"
        elif guess > self.target_number and len(self.attempts) < self.attempt_limit:
            print(f"the number is lower then {guess}")
            message = f"The number is lower then {guess}"
        elif guess < self.target_number and len(self.attempts) < self.attempt_limit:
            print(f"the number is higher then {guess}")
            message = f"the number is higher then {guess}"
        else:
            self.flag = False
            print(f"You lost! You've used your {self.attempt_limit} guess attempt.")
            message = f"You lost! You've used your {self.attempt_limit} guess attempt."
        return message      
    # player has limited guess. game will be ended when its true or has no attempt limit
    def end_condition(self):
        if self.flag or (self.flag == False and len(self.attempts) >= self.attempt_limit):
            print(f"Your attempts: {self.attempts}")
            print(f"Generated number is: {self.target_number}")
            return True
        else:
            return False