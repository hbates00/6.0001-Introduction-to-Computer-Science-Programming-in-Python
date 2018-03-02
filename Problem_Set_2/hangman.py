# Problem Set 2, hangman.py
# Name: Haley Bates-Tarasewicz 
# Collaborators: William Kalb
# Time spent: 2:00

# Hangman Game
# -----------------------------------Provided Code
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def choose_word(wordlist):
    return random.choice(wordlist)

# -----------------------------------Global Variables
wordlist = load_words()

# -----------------------------------Hangman Functions
#Takes a string secret_word and a list letters_guessed and returns true if all of the letters in secret_word have been guessed. 
#Returns false otherwise
def is_word_guessed(secret_word, letters_guessed):
    
    for i in secret_word:
        if i not in letters_guessed:
            return False
        else:
            pass
    return True

#Takes a string secret_word and a list letters_guessed and returns secret_word with all of the unguessed letters as asterisks
def get_guessed_word(secret_word, letters_guessed):
    
    secret_list = list(secret_word)    
    count = 0
    for i in secret_word:
        if i not in letters_guessed:
             secret_list[count] = '*'
        else:
            pass
        count += 1
    return "".join(secret_list)

#takes a list letters_guessed and returns the alphabet with the letters in the list letters_guessed removed
def get_available_letters(letters_guessed):
    
    letters = list(string.ascii_lowercase)
    for i in letters_guessed:
        letters.remove(i)
            

    return "".join(letters)

# -----------------------------------Hangman Main Loop
def hangman(secret_word):
    
    print "Welcome to the game Hangman!"
    print "I am thinking of a word that is ", len(secret_word), 'letters long.'
    
    guesses = 6
    letters_guessed = []
    vowels = ['a', 'e', 'i', 'o', 'u']    
    
    while True:
        print '-------------'
        print 'you have', guesses, 'guesses left.'
        print 'Available letters: ', get_available_letters(letters_guessed)
        
        guess = raw_input('Please guess a letter:')
        
        if guess in letters_guessed:
            print "Oops! You've already guessed that letter:", get_guessed_word(secret_word, letters_guessed)
            guesses -= 1
        
        elif guess in secret_word:
            letters_guessed.append(guess)
            print 'Good guess:', get_guessed_word(secret_word, letters_guessed)
        
        else:
            letters_guessed.append(guess)
            print 'Oops! That letter is not in my word:', get_guessed_word(secret_word, letters_guessed)
            if guess in vowels:
                guesses -= 2
            else:
                guesses -= 1
        
        
        if is_word_guessed(secret_word, letters_guessed):
            print 'Congratulations, you won!'
            break
        elif guesses <= 0:
            print 'Sorry, you ran out of guesses. The word was', str(secret_word) + '.'
            break
        else:
            pass
             
# -----------------------------------Calls the Hangman Function
hangman(choose_word(wordlist))

# -----------------------------------Hangman With Hints Functions
#takes two strings and returns true if they match exactly, or are the same length with non-matching asterisk characters. 
#Returns false otherwise
def match_with_gaps(my_word, other_word):
    
    count = 0
    
    if len(my_word) != len(other_word):
        return False
    else:
        pass
        
    for i in my_word:
        if i != '*':
            if my_word[count] != other_word[count]:               
                return False
            count += 1
        else:
            count += 1
            pass
    return True

#takes a string my_word with a mix of letters and asterisks with asterisks representing unknown letters 
#returns a string every word my_word could be based on the placement of the asterisks
def show_possible_matches(my_word):
    megastring = []
    
    for word in wordlist:
        if match_with_gaps(my_word, word):
            megastring.append(word)
        else:
            pass
    print " ".join(megastring)

# -----------------------------------Hangman With Hints Main Loop
def hangman_with_hints(secret_word):
    
    print "Welcome to the game Hangman!"
    print "I am thinking of a word that is ", len(secret_word), 'letters long.'
    
    guesses = 6
    letters_guessed = []
    vowels = ['a', 'e', 'i', 'o', 'u']    
    
    while True:
        print '-------------'
        print 'you have', guesses, 'guesses left.'
        print 'Available letters: ', get_available_letters(letters_guessed)
        
        guess = raw_input('Please guess a letter:')
        
        if guess == '*':
            print 'Possible word matches are:'
            show_possible_matches(get_guessed_word(secret_word, letters_guessed))
        
        elif guess in letters_guessed:
            print "Oops! You've already guessed that letter:", get_guessed_word(secret_word, letters_guessed)
            guesses -= 1
        
        elif guess in secret_word:
            letters_guessed.append(guess)
            print 'Good guess:', get_guessed_word(secret_word, letters_guessed)
        
        else:
            letters_guessed.append(guess)
            print 'Oops! That letter is not in my word:', get_guessed_word(secret_word, letters_guessed)
            if guess in vowels:
                guesses -= 2
            else:
                guesses -= 1
        
        
        if is_word_guessed(secret_word, letters_guessed):
            print 'Congratulations, you won!'
            break
        elif guesses <= 0:
            print 'Sorry, you ran out of guesses. The word was', str(secret_word) + '.'
            break
        else:
            pass

# -----------------------------------Calls the Hangman With Hints Function
hangman_with_hints(choose_word(wordlist).lower())
