import random
print('''Welcome To Number Hunt
''')

name=input('Input Player Name ')

print(f'''
The game is simple {name}
You have to guess the number in the least number of attempts possible
There are two ranks Legendary and Regular
You are ranked based on the number of attempts u took

Let's get started {name}
''')
number_to_guess= random.randint(1,10)
guess=0
attempts=0

while guess != number_to_guess:
    guess=int(input('Guess a number between 1 and 10 '))
    attempts +=1
    if guess < number_to_guess:
        print('Oops! Too low Try again '+name)
    elif guess > number_to_guess:
        print('Too high! Try again '+name)
    else:
        if attempts <3:
            print(f"BINGO!!!!!!!You got it in {attempts} attempts, LEGENDARY RANK THAT'S IMPRESSIVE!!! {name} " )
        else:
            print(f"BINGO!!!!!!!You got it in {attempts} attempts, REGULAR RANK BETTER LUCK NEXT TIME!!! {name} " )

