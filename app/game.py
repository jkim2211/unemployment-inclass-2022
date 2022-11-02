from random import choice

VALID_OPTIONS = ["rock", "paper", "scissors"]



def determine_winner(user_choice, computer_choice):
    winners = {
        "rock": {
            "rock": None,
            "paper": "paper",
            "scissors": "rock",
        },
        "paper": {
            "rock": "paper",
            "paper": None,
            "scissors": "scissors",
        },
        "scissors": {
            "rock": "rock",
            "paper": "scissors",
            "scissors": None,
        }
    }
    winning_choice = winners[user_choice][computer_choice]
    return winning_choice



if __name__ == "__main__":


    #only run code blow when we run from command line, not when we try to import the file
    #
    # USER SELECTION
    #

    u = input("Please choose one of 'Rock', 'Paper', or 'Scissors': ").lower()
    print("USER CHOICE:", u)
    if u not in VALID_OPTIONS:
        print("OOPS, TRY AGAIN")
        exit()

    #
    # COMPUTER SELECTION
    #

    c = choice(VALID_OPTIONS)
    print("COMPUTER CHOICE:", c)

    #
    # DETERMINATION OF WINNER
    #

    result = determine_winner(u, c).lower()

    if result == u:
        print("YOU WON")
    elif result == c:
        print("COMPUTER WON")
    else:
        print("TIE")