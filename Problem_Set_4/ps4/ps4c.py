# Problem Set 4C
# Name: Haley Bates-Tarasewicz
# Collaborators:
# Time Spent: 4:00
# Late Days Used: 2

import string
import random
from ps4a import get_permutations

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print 'Loading word list from file...'
    # inFile: file
    in_file = open(file_name, 'r', 0)
    # line: string
    line = in_file.readline()
    # word_list: list of strings
    word_list = line.split()
    print '  ', len(word_list), 'words loaded.'
    in_file.close()
    return word_list

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list


### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

# you may find these constants helpful
VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'

class SubMessage(object):
    def __init__(self, text):
        '''
        Initializes a SubMessage object
                
        text (string): the message's text

        A SubMessage object has three attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)
    
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class
        
        Returns: a COPY of self.valid_words
        '''
        words = self.valid_words.copy()
        return words
                
    def build_transpose_dict(self, vowels_permutation):
        '''
        vowels_permutation (string): a string containing a permutation of vowels (a, e, i, o, u)
        
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to an
        uppercase and lowercase letter, respectively. Vowels are shuffled according
        to vowels_permutation. The first letter in vowels_permutation corresponds to a,
        the second to e, and so on in the order a, e, i, o, u. The consonants remain the same. The dictionary should have 52 
        keys of all the uppercase letters and all the lowercase letters.

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        #the number of vowels processed is equal to the current index of the vowel permutation
        transdict = {}
        uppervowelcount = 0
        lowervowelcount = 0
        
        for i in string.ascii_lowercase: #for lowercase letters
            if i in VOWELS_LOWER:
                transdict[i] = string.lower(vowels_permutation[lowervowelcount]) 
                lowervowelcount += 1
            else:
                transdict[i] = i
        
        for i in string.ascii_uppercase: #for uppercase letters
            if i in VOWELS_UPPER:
                transdict[i] = string.upper(vowels_permutation[uppervowelcount])
                uppervowelcount += 1
            else:
                transdict[i] = i
        
        return transdict
        
    def apply_encrypt(self, transpose_dict):
        '''
        transpose_dict (dict): a transpose dictionary
        
        Returns: an encrypted version of the message text, based 
        on the dictionary

        Example usage:
        >>> msg = SubMessage('hello')
        >>> transpose_dict = msg.build_transpose_dict('uoiea')
        >>> encrypted_msg = msg.apply_encrypt(transpose_dict)
        '''
        newstring = ''
        
        for i in self.get_message_text():
            newstring += transpose_dict[i] 
        
        return newstring
        
class EncryptedSubMessage(SubMessage):
    def __init__(self, text):
        '''
        Initializes an EncryptedSubMessage object

        text (string): the encrypted message text

        An EncryptedSubMessage object inherits from SubMessage and has one attributes:
            self.message_text_encrypted (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        SubMessage.__init__(self, text)
        self.message_text_encrypted = self.message_text


    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted


    def decrypt_message(self):
        '''
        Attempt to decrypt the encrypted message 
        
        Idea is to go through each permutation of the vowels and test it
        on the encrypted message. For each permutation, check how many
        words in the decrypted text are valid English words, and return
        the decrypted message with the most English words.
        
        Returns: the best decrypted message    
        
        Hint: use your function from Part 4C
        '''
        permutations = get_permutations('aeiou') #a list of all of the permutations of 'aeiou'
        #keeps track of the number of correct words and the best key to decrypt the message        
        bestwords = 0    
        bestkey = ''
        
        for i in permutations:
            realwords = 0 
            
            for word in self.apply_encrypt(self.build_transpose_dict(i)).split(' '):
                if is_word(WORDLIST_FILENAME, string.lower(word)):
                    realwords += 1
                else:
                    pass
                
            if realwords > bestwords:
                bestwords = realwords                
                bestkey = i
                
            else:
                pass    
        
        return self.apply_encrypt(self.build_transpose_dict(bestkey))

if __name__ == '__main__':

    #TODO: WRITE YOUR TEST CASES HERE
 
    print 'Test Case 1: SubMessage'
    print '---------------'
    test = SubMessage('Hello')
    print "Expected Output: 'Holle'"
    print 'Actual Output:', test.apply_encrypt(test.build_transpose_dict('uoiea'))
    print
    
    print 'Test Case 2: SubMessage'
    print '---------------'
    test2 = SubMessage('Thing')
    print "Expected Output: 'Thang'"
    print 'Actual Output:', test2.apply_encrypt(test.build_transpose_dict('iuaoe'))
    print
        
    print "the Is_word function isn't working, so my decryption cases aren't working." 
    print "is_word(WORDLIST_FILENAME, 'Boom') returns:", is_word(WORDLIST_FILENAME, 'Boom')  
    print "is_word(WORDLIST_FILENAME, 'Tarts') returns:", is_word(WORDLIST_FILENAME, 'Tarts')      
        
    print 'Test Case 3: EncryptedMessage'
    print '---------------'
    test3 = EncryptedSubMessage('Biim')
    print "Expected Output: 'Boom'"
    print 'Actual Output:', test3.decrypt_message()
    print
    
    print 'Test Case 4: EncryptedMessage'
    print '---------------'
    test4 = EncryptedSubMessage('Torts')
    print "Expected Output: 'Tarts'"
    print 'Actual Output:', test4.decrypt_message()
    print
