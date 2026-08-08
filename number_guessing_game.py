import random

minimum_range = int(input('Specify your minimum range: '))
maximum_range = int(input('Specify your maximum range: '))
number_to_guess = random.randint(minimum_range, maximum_range)   #generate a random number between the specified ranges. 
guesses = 5   #To run the code only 5 times
attempts = 0   #To keep track of the number of guesses already made

for i in range(guesses):
    try:   #Error handling
        guessed_number = int(input(f"Guess the number between {minimum_range} and {maximum_range}, You have {5 - i} guesses left:  "))
        attempts += 1
        if guessed_number > number_to_guess:
            print('Too high!')
        elif guessed_number < number_to_guess:
            print('Too low!')
        elif guessed_number == number_to_guess:
            print('congrats! you guessed the number!')
            print(f"Number of attempts: {attempts}")
            break
    except ValueError:
        print('Please enter a valid number')
else:
    print('You lost! Ran out of guesses')
