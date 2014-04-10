#!/usr/bin/python

import re

def disemvowel(s):
    nonv = re.sub(r'[^aeiou]', '', s)
    v = re.sub(r'[aeiou ]', '', s)
    print v
    print nonv
    print ""

disemvowel("two drums and a cymbal fall off a cliff")
disemvowel("all those who believe in psychokinesis raise my hand");
disemvowel("did you hear about the excellent farmer who was outstanding in his field")
