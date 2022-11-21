import random

uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()
numbers = "0123456789"
symbols = "!@#$%^&*()-_=+[{]};:<,>.?/\|`~ "

upper, lower, nums, syms = True, True, True, True

all = ""

if upper:
    all += uppercase_letters
if lower:
    all += lowercase_letters
if nums:
    all += numbers
if syms:
    all += symbols

length = 50
amount = 10

#You can use seed for this password generator
#But I dont know why you want to use seed to get the same password in a random password generator
#I don't recommend this but you can use seed for this password generator

#seed = "anything"

#random.seed(seed)

for x in range(amount):
    password = "".join(random.sample(all, length))
    print(password)