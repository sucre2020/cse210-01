import random

while True:

    class Director:

        def __init__(self) -> None:


            self.highest = 300

            self.answer = random.randint(1, 300)

            print(self.answer)

        def start_game(self):

            user_guess = float(input("Please guess a number btwn 1 - {}: or enter 0 to quit".format(self.highest)))

            if user_guess == self.answer:
                print("Well done, you got it!")
            elif user_guess > self.answer:
                print("Please guess lower")
            else:
                print("Please guess higher")

            while user_guess != self.answer:
                user_guess = float(input(""))
            #if user_guess == 0:
             #   break
            if user_guess == self.answer:
                print("Well done, you got it")
            elif user_guess > self.answer:
                print("Please guess lower")
            else:
                print("Please guess higher")