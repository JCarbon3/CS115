'''
Created on 2/9/2022
@author:   Joseph Carbonell
Pledge:    I pledge my honor that I have abided by the Stevens Honor Code.
CS115 - Hw 2
'''
import sys
# Be sure to submit hw2.py.  Remove the '_template' from the file name.

# Allows up to 10000 recursive calls.
# The maximum permitted limit varies from system to system.
sys.setrecursionlimit(10000)

# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

# Implement your functions here.

def letterScore(letter, scorelist):
    """This function takes 2 inputs, a letter and a scorelist, and finds the letter
    in the scorelist, returning the corresponding score."""
    if scorelist == []:
        return []
    elif scorelist[0][0] == letter:
        return scorelist[0][1]
    else:
        return letterScore(letter,scorelist[1:])

def wordScore(S,scorelist):
    """This function takes a string S and a scorelist, and returns the total value of S
    after it has had letterScore applied to each letter."""
    if S == "" or scorelist == []:
        return 0
    return letterScore(S[0],scorelist) + wordScore(S[1:],scorelist)

def removeLetter(letter, rack):
    """This function removes a letter from the rack so it cannot be used twice."""
    if rack[0] == letter:
        return rack[1:]
    else:
        return [rack[0]] + removeLetter(letter,rack[1:])
                                            

def wordInRack(rack, word):
    """This function checks if a word can be made using the current rack, and returns either True or False."""
    if word == "":
        return True
    elif word[0] in rack:
        return wordInRack(removeLetter(word[0],rack),word[1:])
    else:
        return False
        

def allWordsInRack(rack,dictionary):
    """This function returns a list of all words that can be made using the current rack."""
    return filter(lambda word: wordInRack(rack,word),dictionary)


def wordScorePair(word):
    """This function takes a word and returns a 2 item list of the word and its score."""
    return [word,wordScore(word,scrabbleScores)]

def scoreList(Rack):
    """This function takes a rack and returns all word score pairs that can be made from it."""
    return list(map(wordScorePair,allWordsInRack(Rack,Dictionary)))

def findHighestScore(scorelist):
    """This function a scorelist and returns the word score pair with the highest score.""" 
    if scorelist == []:
        return['',0]
    elif len(scorelist) == 1:
        return scorelist[0]
    elif int(scorelist[0][1]) < int(scorelist[1][1]):
        return findHighestScore(scorelist[1:])
    else:
        return findHighestScore([scorelist[0]]+scorelist[2:])
    
    
def bestWord(Rack):
    """This function takes a rack of letters and returns the highest scoring word possible given the provided dictionary."""
    words = scoreList(Rack)
    return findHighestScore(words)
    
    
    
    
        
        
