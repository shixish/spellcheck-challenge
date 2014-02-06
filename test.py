#Andrew Wessels Feb. 2, 2014
import config
import random
from spellcheck import Spellcheck

f = open(config.dictionary_path, 'r')
tests = []
checker = Spellcheck()

for line in f:
    line = line.strip()#strip off any newline characters or spaces
    checker.add_word(line)#add the word to the spellchecker
    tests.append(line);#first test the correctly spelled word
    for n in range(5):#make 5 additional tests per dictionary word
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

results_good = 0
results_bad = 0
results_total = float(len(tests))
#test each of the generated strings:
for test in tests:
    output = checker.check_word(test)
    print "Test: %s Result: %s"%(test, output)
    if output == "NO SUGGESTION":
        results_bad += 1
    else:
        results_good += 1

print "Results:"
print "\tGood: %d (%.1f%%)"%(results_good, 100*results_good/results_total)
print "\tBad: %d (%.1f%%)"%(results_bad, 100*results_bad/results_total)
