#Andrew Wessels Feb. 2, 2014
import config #edit this file to 

class Spellcheck: #Node definition
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    def __init__(self, word = None):
        self.children = {}#max children is 26 (one for each letter)
        if word: #add the word when creating the new node:
            self.add_word(word)


    #add a word to the dictionary, construct the tree structure
    def add_word(self, word):
        if len(word) > 0:
            first_letter = word[0]
            if first_letter in self.children:
                self.children[first_letter].add_word(word[1:])
            else:
                self.children[first_letter] = Spellcheck(word[1:])

    #check a word against the dictionary, return corrected string
    def check_word(self, word):
        output = self.traverse(word);
        if output:
            return output
        else:
            return "NO SUGGESTION"

    def traverse(self, word):
        #print word
        if len(word) > 0:
            first_letter = word[0].lower()
            try_letters = [first_letter]#the normal case

            #If looking at a vowel, add the other vowels to be checked
            #   if the given vowel doesn't work out.
            if first_letter in self.vowels:
                add_on = self.vowels[:]#clone the vowels list
                add_on.remove(first_letter)#remove the current vowel from the list
                try_letters.extend(add_on)#merge the two, so that our current vowel is at the front
            
            for letter in try_letters:
                if letter in self.children:
                    #print letter
                    #print self.children
                    remaining_letters = word[1:]
                    if (len(remaining_letters) == 0):#end of the tree
                        return letter

                    #do the normal check...
                    test = self.children[letter].traverse(remaining_letters)
                    if (test):
                        #the remaining_letters are fine.
                        return letter + test

                    #check for repeats...
                    test = self.traverse(remaining_letters)
                    if (test):
                        #don't add the current letter on, because it's been repeated
                        return test;
