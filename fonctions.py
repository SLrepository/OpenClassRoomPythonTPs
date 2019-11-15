# -*- coding: utf-8 -*-

"""
Hangman game function file : includes all functions called in main file
"""

import os
import pickle
from random import choice

# include words_to_guess data dictionary
from donnees import *


def get_existing_scores(): # get existing score from file or set scores to "none"
    
    if os.path.exists(file_path): # check if scores file exists
        with open(file_path, 'rb') as file_handler: # then get existing scores
            read_data_stream = pickle.Unpickler(file_handler)
            scores = read_data_stream.load()
    else: # no existing scores set scores to "none"
        scores = {}
    return scores


def get_player_name(): # get player's name

    no_proper_name = True
    while no_proper_name:
        try:
            player_name = input("Please enter your name: ")
            check_if_number = float(player_name) # if player's name is a number, keep looping
        except: # player's name is no number, leave the loop
            no_proper_name= False
    return player_name


def get_word_to_guess(): # get word to guess (random choice in predefined list)
    return choice(words_to_guess)


def update_masked_word(word_to_guess, letters_found): # update masked word to guess with letters found
    
    masked_word = ""
    for letter in word_to_guess:
        if letter in letters_found:
            masked_word += letter
        else:
            masked_word += "*"
    return masked_word


def get_player_letter(): # get player's letter 

    not_a_letter = True
    while not_a_letter:
        try:
            player_letter = input("Please choose your letter: ")
            player_letter = player_letter.lower()
            check_if_number = float(player_letter) # if player's letter is a number, keep looping
        except: # player's letter is no number, leave the loop
            not_a_letter = False
    return player_letter


def save_current_scores(scores): # save current scores by overwriting any existing scores

    with open(file_path, 'wb') as file_handler: # then get existing scores
        write_data_stream = pickle.Pickler(file_handler)
        write_data_stream.dump(scores)
