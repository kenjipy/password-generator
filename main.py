import random

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456^¨!è&é@€ù%"
# This is for your character i added a coppel basic ones you can add more if you want. #

while 1:
    password_len = int(input("what length would you like your password to be : "))
    password_count = int(input("how many password would you like : "))
    for x in range(0,password_count):
        password = ""
        for x in range(0,password_len):
            password_char = random.choice(chars)
            password      = password + password_char
        print("here is your password = ", password)
