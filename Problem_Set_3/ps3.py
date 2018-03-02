# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name: Haley Bates-Tarasewicz
# Collaborators: none
# Time spent: 6 hours

import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print "  ", len(wordlist), "words loaded."
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------

def get_word_score(word, n):
  
    wordsum = 0   
    
    for i in word:
        wordsum += SCRABBLE_LETTER_VALUES.get(i.lower(),0)
    
    if ((5 * len(word)) - (2 * (n - len(word)))) < 1:
        return wordsum
    else:
        return ((5 * len(word)) - (2 * (n - len(word)))) * wordsum


def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    
    for letter in hand.keys():
        for j in range(hand[letter]):
             print letter,              # print all on the same line
    print                               # print an empty line


def deal_hand(n):
    
    hand={}
    num_vowels = n / 3
    
    for i in range(num_vowels):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(num_vowels, n - 1):    
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1
    
    hand['*'] = 1
        
    return hand


def update_hand(hand, word):
    
    new_hand = hand.copy()

    for i in word:
        if i.lower() in new_hand:
            if new_hand[i.lower()] > 1:
                new_hand[i.lower()] -= 1
            else:
                del new_hand[i.lower()]
        else:
            pass
    return new_hand


def is_valid_word(word, hand, word_list):
    
    new_hand = hand.copy()
    first = ''
    second = ''
    yes = False

    if '*' in word:
        
        spot = word.index('*')  
        first = word[:(spot)]
        second = word[(spot + 1):]
        
        for letter in string.ascii_lowercase:
            new_word = first + letter + second
            if new_word in word_list:
                yes = True
        
        if yes == False:
            return False
        else:
            for i in word:
                if i.lower() not in new_hand:
                    return False
                else:
                    if new_hand[i.lower()] > 1:
                        new_hand[i.lower()] -= 1
                    else:
                        del new_hand[i.lower()]  
    else:
        if word.lower() not in word_list:
            return False
        else:
            for i in word:
                if i.lower() not in new_hand:
                    return False
                else:
                    if new_hand[i.lower()] > 1:
                        new_hand[i.lower()] -= 1
                    else:
                        del new_hand[i.lower()]
                    
                
    return True


def calculate_handlen(hand):
    return len(hand.keys())


def play_hand(hand, word_list):

    total = 0

    while calculate_handlen(hand) > 0:
        
        print 'Current Hand: '
        display_hand(hand)
        user_input = raw_input('Enter word, or "&&&" to indicate that you are finished:')
        
        if user_input == '&&&':
            break

        else:
            if is_valid_word(user_input, hand, word_list):
                print '"' + user_input + '" earned', get_word_score(user_input, calculate_handlen(hand)), 'points'
                total += get_word_score(user_input, calculate_handlen(hand))
                print 'Total score:', total

            else:
                print 'That is not a valid word. Please choose another word.'
                print
            hand = update_hand(hand, user_input)
            
    if calculate_handlen(hand) == 0:
        print 'Ran out of letters! Your total was', total, '.'
    else:
        print 'Hand ended! Your total was', total, '.'
    
    return total


def substitute_hand(hand, letter):
    
    new_hand = hand.copy()
    x = random.choice(hand.keys())
    del new_hand[x]
    new_hand[letter] = hand[x]
    return new_hand


def play_game(word_list):
    
    print 'Welcome to 6.0001 Wordgame!'
    hands_number = int(raw_input('How many hands you would like to play? '))
    total = 0
    count = 1
    substitution = True
    replay = True
    
    while hands_number > 0:
        print 'Hand number ', count
        hand = deal_hand(HAND_SIZE)
        if substitution == True:
            if raw_input('Would you like to substitute one letter for another? If so, enter "yes". Otherwise, enter "no".').lower() == 'yes':
                letter = raw_input('What letter would you like in your hand?').lower()
                hand = substitute_hand(hand, letter)
                substitution = False
            else:
                pass
        else:
            pass
        
        score = play_hand(hand, word_list)
        
        if replay == True:
            if raw_input('Would you like to replay your last hand? If so, enter "yes". Otherwise, enter "no".').lower() == 'yes':
                score2 = play_hand(hand, word_list) 
                if score2 > score:
                    score = score2
                else:
                    pass
                replay = False
            else:
                pass
        total += score
        count += 1
        hands_number -= 1
    print "Game over! Your final score was", str(total) + ". Nice job!"
    return total


if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
