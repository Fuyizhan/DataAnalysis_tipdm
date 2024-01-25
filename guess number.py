#if you want to guess a number, then you need to generate a number
import random
def guess(x):
    random_number = random.randint(1, x) # set a range of guess,unless it'll too hard to get it
    # you need to loop it until your guess number equals the random number
    # so before the loop function, you need to initialize your guess number

    guess_number = int(input("Please input a number you want:"))
    while guess_number != random_number:
        if guess_number > random_number:
            guess_number = int(input("too greater, guess again:"))
        else:
            guess_number = int(input("too lower, guess again:"))
    print(f"Congrats! {guess_number} is correct.")

def computer_guess(x):
    low = 1
    high = x
    random_number = random.randint(low, high)
    feedback = ''
    while feedback != 'c':
        feedback = input(f'Is {random_number} is too high(h),too low(l), or correct').lower()
        if feedback == 'h':
            high = random_number - 1
            random_number = random.randint(low, high)
        elif feedback == 'l':
            low = random_number + 1
            random_number = random.randint(low, high)

    print(f"Congrats! {random_number} is correct.")

computer_guess(10)

