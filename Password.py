# Python snippet to guess passwords
# purely for educational purposes
# Try to limit password entry to 5 or less words due to pc processing speed

from random import *

guess_pass = input('Enter you password ')
password = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z',
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z',
            '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ]
guess = ""
while guess != guess_pass:
    guess = ""
    for letter in range(len(guess_pass)):
        guess_letter = password[randint(0, 60)]
        guess = str(guess_letter) + str(guess)
    print(guess)

print("Your Password is ", guess)
