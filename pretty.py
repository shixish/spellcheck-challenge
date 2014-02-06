#Andrew Wessels Feb. 2, 2014
import config #edit this file to
from spellcheck import Spellcheck

#load in the dictionary words:
f = open(config.dictionary_path, 'r')
checker = Spellcheck()

for line in f:
    checker.add_word(line.strip())#strip off any newline characters or spaces
f.close()



print "You will be prompted to give me a sequence of words."
print "I will attempt to spellcheck the words that you give me, and I'll tell you what I think the word is supposed to be, otherwise I'll say \"NO SUGGESTION\"."


while(True):
    input_word = raw_input("Enter a word: ")
    output_word = checker.check_word(input_word)
    if output_word == input_word:
        print "I recognize that word!"
    elif output_word != "NO SUGGESTION":
        print "I think you meant \"%s\"."%(output_word)
    else:
        print output_word
