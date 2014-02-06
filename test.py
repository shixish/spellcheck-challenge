#Andrew Wessels Feb. 2, 2014
import config

f = open(config.dictionary_path, 'r')

for line in f:
    print line.strip()#strip off any newline characters or spaces
f.close()
