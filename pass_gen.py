import random
import string
from string import ascii_lowercase, ascii_uppercase, digits, punctuation

letters = list(ascii_lowercase) + list(ascii_uppercase)
symbols = list(punctuation)
numbers = list(digits)

password = ""

num_of_letters = int(input("Enter the amount of letters you want in the password: "))
num_of_symbols = int(input("Enter the amount of symbol you want in the password: "))
num_of_numbers = int(input("Enter the amount of number you want in the password: "))
pass_list = []


for char in range(0,num_of_letters):
    pass_list.append(random.choice(letters))
for char in range(0,num_of_symbols):
    pass_list.append(random.choice(symbols))
for char in range(0,num_of_numbers):
    pass_list.append(random.choice(numbers))
random.shuffle(pass_list)

for char in pass_list:
    password += char
print(password)