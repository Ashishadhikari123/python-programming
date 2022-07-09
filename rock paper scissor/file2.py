import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]
user = int(input("what do u choose? type 0 for ROCK type 1 for PAPER type 2 for SCISSOR\n"))
print("you choose")
print(game_images[user])
x = random.randint(0,2)
systemChoose = x
print("computer choose")
print(x)
print(game_images[x])

# if user choose rock
if user == 0 and systemChoose == 0:
    print("tie")
elif user == 0 and systemChoose == 1:
    print("you lose")
elif user == 0 and systemChoose == 2:
    print("you win")

# if user choose paper
elif user == 1 and systemChoose == 0:
    print("you lose")
elif user == 1 and systemChoose == 1:
    print("tie")
elif user == 1 and systemChoose == 3:
    print("you lose")

# if user choose scissor
elif user == 2 and systemChoose == 0:
    print("you lose")
elif user == 2 and systemChoose == 1:
    print("you win")
else :
    print("tie")
