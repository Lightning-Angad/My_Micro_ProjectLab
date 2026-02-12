import random
char="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
length=int(input("Enter Length: "))
password=""
for i in range(length):
    password+=random.choice(char)
print(f"Your password is {password}")