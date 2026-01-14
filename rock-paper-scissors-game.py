import random

choices = ('r', 'p', 's')

emojiDict = {
    'r': '🪨',
    'p': '🧻',
    's': '✂️'
}

totalRoundInit = 3  


def pickWinner(u, c, winCount, loseCount, roundLeft):
    
    if (u == 'r' and c == 's') or (u == 's' and c == 'p') or (u == 'p' and c == 'r'):
        winCount += 1
        print('You win! Moving to the next round')
    elif u == c:
        print("It's a Draw! Moving to the next round")
    else:
        loseCount += 1
        print('You lose! Moving to the next round')

    roundLeft -= 1 
    return winCount, loseCount, roundLeft


while True:

    winCount = 0
    loseCount = 0
    totalRound = totalRoundInit 

    while totalRound > 0:

        userInput = input('Rock, paper, or scissors? (r/p/s): ').lower()

        if userInput in choices:
            userChosed = userInput
            computerChosed = random.choice(choices)

            print(f'You choosed {emojiDict[userChosed]}')
            print(f'Computer choosed {emojiDict[computerChosed]}')

            winCount, loseCount, totalRound = pickWinner(
                userChosed, computerChosed, winCount, loseCount, totalRound
            )

        else:
            print('Invalid Choice!')

    print("\n--- Final Result ---")
    if winCount > loseCount:
        print(f'Yessss baby! You beat the computer! You won {winCount} rounds.')
    elif winCount == loseCount:
        print(f'The match is Draw. You won {winCount} rounds.')
    else:
        print(f'Computer wins! You lost {loseCount} rounds. Looser hahaha!')

    nextMatch = input('Do you want to play again? (y/n): ').lower()
    if nextMatch != 'y':
        break
    print("\nStarting a new game!\n")
