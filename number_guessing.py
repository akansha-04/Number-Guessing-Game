import random
import artnumber
number=[1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,10 ,11 ,12 ,13 ,14 ,15 ,16 ,17 ,18 ,19 ,20 ,21 ,22 ,23 ,24 ,25 ,26 ,27 ,28 ,29 ,30 ,31 ,32 ,33 ,34 ,35 ,36 ,37 ,38 ,39 ,40 ,41 ,42 ,43 ,44 ,45 ,46 ,47 ,48 ,49 ,50 ,51 ,52 ,53 ,54 ,55 ,56 ,57 ,58 ,59 ,60 ,61 ,62 ,63 ,64 ,65 ,66 ,67 ,68 ,69 ,70 ,71 ,72 ,73 ,74 ,75 ,76 ,77 ,78 ,79 ,80 ,81 ,82 ,83 ,84 ,85 ,86 ,87 ,88 ,89 ,90 ,91 ,92 ,93 ,94 ,95 ,96 ,97 ,98 ,99 ,100]
print(artnumber.logo)
print('Welcome to the number guessing game!')
print('I am guessing a number between 1 to 100.Can you guess which number I was guessing ?')
choice=input('Do you want easy level or hard level ?').lower()
computer_guess=random.choice(number)
min_range=computer_guess-10
max_range=computer_guess+10
attempts=0
if choice=='easy':
    attempts=10
else:
    attempts=5
finish_game =False
while finish_game==False:
    print(f'You have {attempts} attempts to guess the number. ')
    hint=input('Do you want a hint: Type y for yes and n for no ').lower()
    if hint=='y':
        print(f'The number is between {min_range} to {max_range}')
    user_guess=int(input('Make a guess: '))
    if user_guess==computer_guess :
        print('You have succesfully guessed the number')
        finish_game=True
        break
    if attempts==0:
        print('You lose since you ran out of attempts')
        print(f'The number was {computer_guess}')
        finish_game=True
        break
    if user_guess!=computer_guess:
        attempts=attempts-1
        if user_guess<computer_guess:
            print(f'Too Low')
        elif user_guess>computer_guess:
            print(f'Too High')
        
    