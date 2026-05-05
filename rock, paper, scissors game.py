import random
choices = ['rock', 'paper', 'scissors']
computer_choice = random.choice(choices)
name = input('''Hi there, Input Player name: 
''')
user_choice=''
attempts=0

while user_choice !=computer_choice:
    user_choice= input(f'Rock, Paper, or Scissors? {name} ')
    attempts +=1
    if user_choice.lower() == computer_choice:
        print(f'Its a tie! try again {name}')
    elif user_choice == 'rock' and computer_choice== 'paper':
         print(f'You lose! try again {name}')
    elif user_choice == 'rock' and computer_choice== 'scissors':
         print(f'''You win! {name}...Number of attempts: {attempts}''')
         break
    elif user_choice == 'paper' and computer_choice== 'rock':
         print(f'''You win! {name}...Number of attempts: {attempts} ''')
         break
    elif user_choice == 'paper' and computer_choice== 'scissors':
         print(f'You lose! try again {name}')
    elif user_choice == 'scissors' and computer_choice== 'paper':
         print(f'''You win! {name}..Number of attempts: {attempts}''')
         break
    elif user_choice == 'scissors' and computer_choice== 'rock':
         print(f'You lose! try again {name}')
    else:
        print(f"Sorry!! but i don't understand your choice {name}")
