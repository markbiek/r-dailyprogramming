#!/usr/bin/python

import re

def disemvowel(s):
    v = re.sub(r'[^aeiou]', '', s)
    nonv = re.sub(r'[aeiou ]', '', s)
    print nonv
    print v
    print ""

def disemvowel2(s):
    v = [ c for c in s if c in 'aeiou' ]
    nonv = [ c for c in s if not c in 'aeiou ' ]
    print "".join(nonv)
    print "".join(v)
    print ""

disemvowel("two drums and a cymbal fall off a cliff")
disemvowel2("two drums and a cymbal fall off a cliff")

disemvowel("all those who believe in psychokinesis raise my hand");
disemvowel2("all those who believe in psychokinesis raise my hand");

disemvowel("did you hear about the excellent farmer who was outstanding in his field")
disemvowel2("did you hear about the excellent farmer who was outstanding in his field")

