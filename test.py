#Andrew Wessels Feb. 2, 2014
import config
import random
from spellcheck import Spellcheck

f = open(config.dictionary_path, 'r')
tests = []

for line in f:
    line = line.strip()#strip off any newline characters or spaces
    for n in range(5):#make 5 tests per dictionary word
        word = ""
        for l in line:#each letter
            if l in Spellcheck.vowels:#randomize all vowels
                l = random.choice(Spellcheck.vowels)

            if (random.randint(0,2) == 0):# 1 in 3 to upper-case the letter
                l = l.upper()

            if (random.randint(0,2) == 0):# 1 in 3 chance to repeat the letter
                word += l
            word += l
        tests.append(word);
f.close()

#print tests
