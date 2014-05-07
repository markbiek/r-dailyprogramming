#!/usr/bin/python

from random import randint
import sys

win_text = {
        'ScissorsPaper': 'Scissors cut Paper',
        'PaperRock': 'Paper covers Rock',
        'RockLizard': 'Rock crushes Lizard',
        'LizardSpock': 'Lizard poisons Spock',
        'SpockScissors': 'Spock smashes Scissors',
        'ScissorsLizard': 'Scissors decpaitate Lizard',
        'LizardPaper': 'Lizard eats Paper',
        'PaperSpock': 'Paper disproves Spock',
        'SpockRock': 'Spock vaporizes Rock',
        'RockScissors': 'Rock crushes scissors'
        }

moves = {
        'Rock': ['Lizard', 'Scissors'],
        'Paper': ['Rock', 'Spock'],
        'Scissors': ['Paper', 'Lizard'],
        'Lizard': ['Spock', 'Paper'],
        'Spock': ['Scissors', 'Rock']
        }

choices = dict(zip(range(1,6), moves.keys()))

while True:
    print "Select a move:"
    for key in choices:
        print str(key) + ".) " + choices[key]
    print "q.) Quit"

    choice = raw_input(">")

    if choice == 'q':
        sys.exit(0)
    else:
        choice = int(choice)

        if choice in choices.keys():
            cchoice = randint(1,5)

            print "\nPlayer picked: " + choices[choice]
            print "Computer picked: " + choices[cchoice]

            if choice == cchoice:
                print "Tie!\n"
            else:
                pass
        else:
            print "Invalid choice."
