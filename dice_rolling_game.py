import random   #module that allows us to generate a random number

while True:   #better than declaring a variable and setting it to true
    choice = input('Start the game? (y/n): ').lower()   #convert the answer into lowercase so we don't have too many conditions in the if statement

    if choice == 'y':
        num_dice = int(input('How many dice would you like to roll? '))

        for i in range(num_dice):
            dice = random.randint(1, 6)    #method to generate a random number between 1 & 6
            print(dice)
    elif choice =='n':
        print('Thanks for playing!!!')
        break
    else:
        print('Invalid Input!!!')
