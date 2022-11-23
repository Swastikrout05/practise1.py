import sys

user1 = input('What is your name: \n')
user2 = input('And your name: \n')
user1_answer = input('%s, do you wanna play Rock, Paper, Scissor?' % user1)
user2_answer = input('%s, do you wanna play Rock, Paper, Scissor?' % user2)

def compare(u1, u2):
    if u1 == u2:
        return('It is a tie')
    elif u1 == 'Rock':
        if u2 == 'Scissor':
            return('Rock wins!')
        else:
            return('Paper wins!')
    elif u1 == 'Scissor':
        if u2 == 'Paper':
            return('Scissor wins!')
        else:
            return('Rock wins!')
    elif u1 == 'Paper':
        if user2 == 'Rock':
            return('Paper wins!')
        else:
            return('Scissor wins!')
    else:
        return('Invalid input! You have not entered Rock, Paper, Scissor, try again.')
        sys.exit()

print(compare(user1_answer, user2_answer))


