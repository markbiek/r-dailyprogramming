#!/usr/bin/python

#http://www.reddit.com/r/dailyprogrammer/comments/1t0r09/121613_challenge_145_easy_tree_generation/

import sys

_USAGE = "<size> <trunk char> <leaf char>: "

print _USAGE
input = raw_input().split(" ")

size = int(input[0])
trunk = input[1]
leaf = input[2]

if size % 2 == 0 or size < 3 or size > 21:
    sys.stderr.write("Size must be an odd number between 3-21.\n")
    sys.exit(1)

tree = []

tdiff = (size/2) - 1
tree.append( (tdiff * ' ') + (trunk * 3) )

cursize = size
while cursize > 0:
    spaces = (size-cursize) / 2
    tree.append((spaces * ' ') + (leaf * cursize) + '\n')
    cursize = cursize - 2


print "".join(reversed(tree))
