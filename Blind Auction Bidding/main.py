from replit import clear
from art import logo
print(logo)

bids = {}

def find_highest_bidder(bids):
  highest_bid = 0
  winner = ""
  for i in bids:
    amount = bids[i]
    if(amount > highest_bid):
      highest_bid = amount
      winner = i
  print(f"The winner is {winner} with bid of ${highest_bid}")

while(True):
  name = input("Enter your name \n")
  price = int(input("Enter your bid \n"))
  bids[name] = price;
  should_continue = input("Are there any other bidders?Type yes or no \n").lower()
  if(should_continue=="no"):
    break;
  else:
    clear()
find_highest_bidder(bids)
