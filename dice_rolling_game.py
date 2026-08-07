import random    #module that allows us to generate a random number

while True:    #better than declaring a variable and setting it to true
    #Ask user if they want to roll the dice
    choice = input('Roll the dice? (y/n): ').lower()  #convert the answer into lowercase so we don't have too many conditions in the if statement

    if choice == 'y':
        die1 = random.randint(1, 6)   #method to generate a random number between 1 & 6
        die2 = random.randint(1, 6)
        print(f'({die1}, {die2})')    #use f string for simplicity
    elif choice == 'n':
        print('Thanks for playing!!!')
        break
    else:
        print('Invalid choice!!!')
