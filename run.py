#Andrew Wessels Feb. 2, 2014
import config #edit this file to
from spellcheck import Spellcheck

#load in the dictionary words:
f = open(config.dictionary_path, 'r')
checker = Spellcheck()

for line in f:
    checker.add_word(line.strip())#strip off any newline characters or spaces
f.close()

while(True):
    input_word = raw_input("> ")
    output_word = checker.check_word(input_word)
    print output_word
