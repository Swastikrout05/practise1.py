import random
rd = random.randint(1,9)
guess = 0
c = 0
while guess != rd and guess != 'exit':
    guess = input('Enter a number between 1 to 9')
    
    if guess == 'exit':
        break
    guess = int(guess)
    c += 1

    if guess < rd:
     print('low digit')
    elif guess > rd:
     print('You have enter high digit')
    else:
     print('Tie')
     print('You took only', c, 'tries!')
input()



    