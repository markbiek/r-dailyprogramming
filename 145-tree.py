#!/usr/bin/python

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

print input
