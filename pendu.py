# -*- coding: utf-8 -*-

"""
Hangman game main file
"""

# include all data and all functions defined in donnees/fonctions.py
from donnees import *
from fonctions import *

# get existing scores ()
scores = get_existing_scores()

# get player's name
player = get_player_name()

# if player not registred, set scores to 0
if player not in scores.keys():
    scores[player] = 0

LetsPlay = True # set while letslay loop to True

while LetsPlay:
    # show player name and score
    print("player {} has {} point(s)".format(player, scores[player]))
    # get word to guess as a random choice
    word_to_guess = get_word_to_guess()   
    letters_found = []
    # set mask on word to guess: all letters masked with *
    masked_word = update_masked_word(word_to_guess, letters_found)
    remaining_rounds = rounds
    # start game rounds (8 max.)
    while word_to_guess != masked_word and remaining_rounds > 0:
        # show masked word and current round
        print("word to guess is {} - remaining rounds {}".format(masked_word, remaining_rounds))
        # check player's letter
        letter = get_player_letter()
        if letter in letters_found: # Lettre already chosen
            print("Letter already chosen.")
        elif letter in word_to_guess: # Letter part of word to guess
            letters_found.append(letter)
            print("well one {}!".format(player))
        else: # letter not in word to guess
            remaining_rounds -= 1 # remove 1 game rounds 
            print("nop, no such letter in the word, please try again")
        # update mask on word to guess
        masked_word = update_masked_word(word_to_guess, letters_found)

    # check if word to guess was found
    if word_to_guess == masked_word: # word found so player wins
        print("congrats {}, you found the word {}.".format(player,word_to_guess))
    else: # not found so player hangs
        print("shame on you Hanged man!!!")

    # update scores
    scores[player] += remaining_rounds

    # restart or end game ?
    if(input("Still willing to play {} (Enter or anything else (+enter) for yes / no (+enter) for no) ? ".format(player)) == "no"):
        LetsPlay = False # player prefers to leave

# save scores in file
save_current_scores(scores)


# show scores
print("Player {} scored {} points.".format(player, scores[player]))