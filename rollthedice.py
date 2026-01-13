import random

while True:
    userIput =  input('Roll the dice? (y/n): ').lower()
    if userIput == 'y' :
      userInpt2 = input('Do you want to roll multiple times? (y/n): ').lower()
      if userInpt2 == 'y':
        userInput3 = int(input('How many dice you want to roll?: '))
        for _ in range(userInput3) :
            rand1 = random.randint(1, 6)
            rand2 = random.randint(1, 6)
            print(f"({rand1} , {rand2})")
        userWish =  input("Do you want to roll the dice again? (y/n): ").lower()
        if userWish == 'y':
            continue
        elif userWish == 'n':
                break
        else:
            print('Invalid choice')
      elif userInpt2 == 'n' :
         rand1 = random.randint(1, 6)
         rand2 = random.randint(1, 6)
         print(f"({rand1} , {rand2})")
         userWish =  input("Do you want to roll the dice again? (y/n): ").lower()
         if userWish == 'y':
            continue
         elif userWish == 'n':
            break
         else:
            print('Invalid choice')
      else:
         print("Invalid choice")

    elif userIput == 'n':
        print("Thanks for being interested!")
        break
    else:
        print('Invalid choice')

