# -*- coding: utf-8 -*-

from random import randrange
from math import ceil

def byebye(): # "Leave the game" function
    print("We are looking forwrd to seeing you soon, Mr Neil !")
    return(False) # set letPlay to False

moneyToSpend = 500 # current amount of $$$
LetsPlay = True # set while letslay loop to True

print("Welcome Mr Neil, what can we to for your ${} ?".format(moneyToSpend))

while LetsPlay:
    
    # player's number
    chosen = False
    while not chosen:
        try:
            yourNumber = int(input("Please choose your number (between 0 and 49): "))
            assert yourNumber >= 0 and yourNumber < 50 # make sure number is in between 0 to 49
        except ValueError: # Not a proper number
            pass
        except AssertionError: # number < 0 and > 49
            pass
        else: # player's number is chosen
            chosen = True
    
    # player's bet
    no_bet = True
    while no_bet:
        try:
            yourBet = int(input("Please enter your bet (not less than $1 and not more than ${}): ".format(moneyToSpend)))
            assert yourBet > 0 and yourBet <= moneyToSpend #make sure bet is at least $1 and not greater than available money
        except ValueError: # not a proper number
            pass
        except AssertionError: # bet is 0 or greater than available money
            pass
        else: # player's bet is made
            no_bet = False

    print("Alea jacta est...Games are made...")
    winning_number = randrange(50) # choose random number between 0 to 49
    print("... and the winning number is {}".format(winning_number))

    # check win
    if winning_number == yourNumber: # same number so player wins 3 times the bet
        yourBet = yourBet * 3
        moneyToSpend += yourBet
        print("Congratulations Mr Neil, you won ${}".format(yourBet))
    elif (winning_number%2) == (yourNumber%2): # same coulour so player wins half the bet
        yourBet = ceil(yourBet*0.5)
        moneyToSpend += yourBet
        print("Well done Mr Neil, you won ${}".format(yourBet))
    else: # you loser !!!
        moneyToSpend -= yourBet
        print("Sorry Mr Neil, just take another chance")

    if moneyToSpend <= 0: # if no money left
        LetsPlay = byebye() # move over
    else:
        print("You currently owns ${}".format(moneyToSpend)) # show money currently available
        if(input("Still willing to play Mr Neil (Enter or anything else (+enter) for yes / no (+enter) for no) ? ") == "no"):
            letsPlay = byebye()  # player wants to leave
