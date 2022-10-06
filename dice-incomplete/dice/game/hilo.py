from random import randint
from itertools import count

def number_guessing(minimum, maximum):
    randomNum = randint(minimum, maximum)
    for tries in count(1):
        numPlayer = int(input("Guess the number({}-{})".format(minimum, maximum)))
        if numPlayer > randomNum:
            print ("My number is smaller"  )
        elif numPlayer < randomNum:
            print ("My number is bigger")
        elif numPlayer == randomNum:
            return tries

print ("Well done you guessed my number in {} guesses".format(
    number_guessing(0, 2)))


    