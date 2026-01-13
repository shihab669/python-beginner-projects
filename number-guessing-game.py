import random

playAgain = True

while playAgain:
    i = 0
    attempts = 5

    userGivenmin = int(input('Please enter a minimum number: '))

    userGivenmax = int(input('Please enter a maximum number: '))

    randomNumber = random.randint(userGivenmin, userGivenmax)

    while True:
        if attempts == 0:
            print('Maximum attempts reached')
            playAgain = False
            break
        else:
            userInput = int(input(f'Select a number between {userGivenmin} and {userGivenmax} (maximum attempts {attempts}): '))

            if userInput < randomNumber:
                i += 1
                attempts -= 1
                print(f'Too low! Try again. attempts left  {attempts}')
            elif userInput > randomNumber:
                i += 1
                attempts -= 1
                print(f'Too high! Try again. attempts left   {attempts}')
            elif userInput == randomNumber:
                print(f'Congratulations! You guessed the number in {i} attempts.')
                userWish = input('Do you want to play more? (y/n): ')
                if userWish == 'y':
                    break
                else:
                    playAgain = False
                    break
            else:
                print('Something went wrong!')
