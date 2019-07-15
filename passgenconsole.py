import random
import string
import pyperclip

password = ''
stack = ''

'''while True:
    length = input("What character length do you want your password to be? (16 and up is recommended)")
    if int(length) == int:
        break'''
length = int(input("What character length do you want your password to be? (16 and up is recommended)"))    # Get the input
while type(length) != int:        # Loop until it is a blank line
    length = input("What character length do you want your password to be? (16 and up is recommended)")

while True:
    sym = input("Do you want symbols? (y or n)")
    if sym == 'y':
        stack += 'a'
        break
    elif sym == 'n':
        break

while True:
    sym = input("Do you want numbers? (y or n)")
    if sym == 'y':
        stack += 'b'
        break
    elif sym == 'n':
        break

if stack == '':
    for x in range(length):
        password += random.choice(string.ascii_letters)
elif stack == 'a':
    for x in range(length):
        path = random.randint(0, 1)
        if path == 0:
            password += random.choice(string.ascii_letters)
        elif path == 1:
            password += random.choice(string.punctuation)
elif stack == 'b':
    for x in range(length):
        path = random.randint(0,1)
        if path == 0:
            password += random.choice(string.ascii_letters)
        elif path == 1:
            password += random.choice(string.digits)
elif stack == 'ab':
    for x in range(length):
        path = random.randint(0, 2)
        if path == 0:
            password += random.choice(string.ascii_letters)
        elif path == 1:
            password += random.choice(string.punctuation)
        elif path == 2:
            password += random.choice(string.digits)

pyperclip.copy(password)
print(password + '\nYour password is now copied onto the clipboard.')