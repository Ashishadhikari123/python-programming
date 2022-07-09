import random
user = int(input("what do u choose? type 1 for ROCK type 2 for PAPER type 3 for SCISSOR\n"))
system = ["rock", "paper", "scissor"]
x = random.randint(0,2)
systemChoose = system[x]
print("computer choose : "+ systemChoose)

# if user choose rock
if user == 1 and systemChoose == "rock":
    print("tie")
elif user == 1 and systemChoose == "paper":
    print("you lose")
elif user == 1 and systemChoose == "scissor":
    print("you win")

# if user choose paper
elif user == 2 and systemChoose == "rock":
    print("you lose")
elif user == 2 and systemChoose == "paper":
    print("tie")
elif user == 2 and systemChoose == "scissor":
    print("you lose")

# if user choose scissor
elif user == 3 and systemChoose == "rock":
    print("you lose")
elif user == 3 and systemChoose == "paper":
    print("you win")
else :
    print("tie")
