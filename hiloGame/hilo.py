import random

class Director():
    '''The responsibility of the director is to direct the game'''

    def __init__(self) -> None:
        pass


    keep_playing = "yes"

    while keep_playing == "yes":


        #class Director:

            #def __init__(self) -> None:


        highest = 300

        answer = random.randint(1, 300)

        guess_count = 0

        user_guess = -1

        print(answer)


        # Keep going as long as the guess doesn't match the magic number
        while user_guess != answer:
            user_guess = int(input("What is your guess btwn 1 - {}: ".format(highest)))
            guess_count = guess_count + 1

            if user_guess < answer:
                print("Higher")
            elif user_guess > answer:
                print("Lower")
            else:
                print("You guessed it!")

        # At this point, they have guessed it correctly
        print(f"It took you {guess_count} guesses")

        keep_playing = input("Would you like to play again (yes/no)? ")

    print("Thank you for playing. Goodbye.")