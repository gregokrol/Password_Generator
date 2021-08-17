import random

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_- ={}[]/'

while 1:
    password_len = int(input("What lenght would you want for your Password: "))
    password_count = int(input("How many Password option you want : "))
    for x in range(0,password_count):
        password = ""
        for x in range(0,password_len):
            password_char = random.choice(chars)
            password = password + password_char
        print('Here is your Password: ', password)