from random import choice

valid_options = ["rock","paper","scissors","hoya"]
#
# USER SELECTION
#

u = input("Please choose one of 'Rock', 'Paper', or 'Scissors': ").lower()
print("USER CHOICE:", u)
if u not in valid_options:
    print("OOPS, TRY AGAIN")
    exit()

#
# COMPUTER SELECTION
#

c = choice(valid_options)
print("COMPUTER CHOICE:", c)

#
# DETERMINATION OF WINNER
# ... (there may be a bug in this logic :-)

if u == "rock" and c == "rock":
    print("It's a tie!")
elif u == "rock" and c == "paper":
    print("The computer wins")
elif u == "rock" and c == "scissors":
    print("The user wins")

elif u == "paper" and c == "rock":
    print("The computer wins")
elif u == "paper" and c == "paper":
    print("It's a tie!")
elif u == "paper" and c == "scissors":
    print("The user wins")

elif u == "scissors" and c == "rock":
    print("The computer wins")
elif u == "scissors" and c == "paper":
    print("The user wins")
elif u == "scissors" and c == "scissors":
    print("It's a tie!")