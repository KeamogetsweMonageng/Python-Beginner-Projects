import random

number_to_guess = random.randint(1, 100)   #generate a random number between 1 & 100. Outside loop to do it once

while True:
    try:   #Error handling so the program does not crash
        guessed_number = int(input('Guess the number between 1 & 100: '))
        if guessed_number > number_to_guess:
                print('Too high!')
        elif guessed_number < number_to_guess:
                print('Too low!')
        elif guessed_number == number_to_guess:
                print('congrats! you guessed the number!')
                break
    except ValueError:
        print('Please enter a valid number')
