import random

secretNumber = random.randint(1, 20)
print('I am thingk of a number between 1 and 20.')

# ask the players to guess 6 times
for guessTaken in range(1, 7):
    print('Take a guess')
    guess = int(input())

    if guess < secretNumber:
        print('your number is smaller!')
    elif guess > secretNumber:
        print('your number is bigger!')
    else:
        break

if guess == secretNumber:
    print(f'great! You guessed my number {secretNumber} in {guessTaken} times!')
else:
    print(f'No. The number I was thinking was {secretNumber}.')
