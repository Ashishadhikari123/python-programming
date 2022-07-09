import random

names = input("Enter your friends name {separated by single space} \n")
names = names.split()
length = len(names)
number = random.randint(0 , length-1)
print(names[number] + " is going to pay the bill")

