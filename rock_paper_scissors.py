import random

def play():
    computer = random.choice(['r', 'p', 's'])
    user = input("what's your choice?")

    if computer == user:
        return "tie"

    if is_win(user, computer):
        return "Win"

    return "lose"
def is_win(player, opponent):
    if(player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r') \
        or (player == 's' and opponent == 'p'):
        return True;

#print(play())


