import random

print('----------------------------------')
print('    GUESS THAT NUMBER GAME')
print('----------------------------------')
print()

the_number = random.randint(0,100)
guess = -1

name = input('Player what is your name? ')

while guess != the_number:
    guess_text = input('Guess a number between 0 and 100:  ')
    guess = int(guess_text)

    if guess < the_number:
        print(f'Sorry {name} your guess of {guess} was too low')
    elif guess > the_number:
        print(f'Sorry {name} your guess of {guess} was too high')
    else:
        print(f'Excellent work {name}, you won, it was {guess}!')
print('done')