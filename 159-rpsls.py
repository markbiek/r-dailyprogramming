#!/usr/bin/python

from random import randint
import sys

stats = {
        "games": 0,
        "cwins": 0,
        "pwins": 0,
        "ties": 0
        }

moves = {
        'Rock': {'Lizard':'crushes', 'Scissors':'crushes'},
        'Paper': {'Rock':'covers', 'Spock':'disproves'},
        'Scissors': {'Paper':'cut', 'Lizard':'decapitate'},
        'Lizard': {'Spock':'poisons', 'Paper':'eats'},
        'Spock': {'Scissors':'smashes', 'Rock':'vaporizes'}
        }

choices = dict(zip(range(1,6), moves.keys()))

def percent_stat(key):
    global stats

    return str((stats[key] / stats["games"]) * 100) + "%"

def output_stats():
    global stats

    print "Total Games Played: ", stats["games"]
    print "Computer Wins: ", stats["cwins"], percent_stat("cwins")
    print "Player Wins: ", stats["pwins"], percent_stat("pwins")
    print "Ties: ", stats["ties"], percent_stat("ties")

while True:
    print "Select a move:"
    for key in choices:
        print str(key) + ".) " + choices[key]
    print "q.) Quit"

    choice = raw_input(">")

    if choice == 'q':
        output_stats()
        sys.exit(0)
    else:
        stats["games"] = stats["games"] + 1

        choice = int(choice)

        if choice in choices.keys():
            cchoice = randint(1,5)

            pc = choices[choice]
            cc = choices[cchoice]

            print "\nPlayer picked: " + pc
            print "Computer picked: " + cc

            if choice == cchoice:
                stats["ties"] = stats["ties"] + 1
                print "Tie!\n"
            else:
                if cc in moves[pc].keys():
                    stats["pwins"] = stats["pwins"] + 1
                    win_text = pc + " " + moves[pc][cc] + " " + cc + ", Player wins!\n"
                else:
                    stats["cwins"] = stats["cwins"] + 1
                    win_text = cc + " " + moves[cc][pc] + " " + pc + ", Computer wins!\n"
                print win_text
        else:
            print "Invalid choice."
