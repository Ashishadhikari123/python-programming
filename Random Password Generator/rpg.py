import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
           'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
           'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

password = ""
password_list = []

letter = int(input("Enter number of letters you want to like in your password\n"))
symbol = int(input("Enter number of symbols you want to like in your password\n"))
number = int(input("How many numbers you want to like in your password\n"))

for i in range(1,letter+1):
    password_list.append(random.choice(letters))

for i in range(1,symbol+1):
    password_list.append(random.choice(symbols))

for i in range(1,number+1):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)

for i in password_list:
    password+=i
print(password + " use it as your password")
