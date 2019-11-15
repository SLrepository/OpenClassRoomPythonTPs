# Open Classroom Python programming exercise (TPs)
## Python TPs from https://openclassrooms.com/en/courses/235344-apprenez-a-programmer-en-python
Implement all programming exercises (TPs) from the above link

## Description of content
### First programming exercise: leapyear.py (année bissextile)
This really simple implementation on a standalone file performs a quick leapyear check on any year entered by the user.

Ex.: entry 1967 shows "l'année n'est pas bissextile", entry 1968 shows "l'année est bissextile"

### Second programming exercise: Zcasino.py (simulation de roulette)
Still a standalone file, but implementation is slightly more sophisticated (but not yet advanced).

This python program simulates a (casino) roulette  on which a player can bet some virtual $$$ on a number (between 0 and 49) and, either gain three times the amount (by chosing the winning number), either gain half the amount (by chosing the same colour, weither the number is odd or even) or loose the lot.

This file shows the use of randrange() function from random module and ceil() function from math module, also implements bloc sequences like:

       try:
            ...
            assert ...
        except ...:
            pass
        except ...:
            pass
        else: 
            ...
### Third programming exercise: donnees.py, fonctions.py and pendu.py (jeu du pendu)
This exercice requiers some modular implementation based on the following file structure:

- pendu.py: Hangman game main module
- fonctions.py: Hangman game functions called in main module
- donnees.py: Hangman game relevant data used in function or main module

This program implements another game, the Hangman game (jeu du pendu), where the player is given 8 attempts to guess a word, randomly chosen from a predefined list. If no attempt left, the player has lost and is virtually hanged.

This implementation also handles a scores file, updating all the different player's scores on every game.

Usage of import statements, list operations, choice() from random module or pickle module is quite popular, here.

