'''
Created on 2/16/2022
@author:   Joseph Carbonell
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Hw 3
'''
# Be sure to submit hw3.py.  Remove the '_template' from the file name.

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 0
' Implement the function giveChange() here:
' See the PDF in Canvas for more details.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# your code goes here
def giveChange(amount,coins):
    """This function takes a list of possible coins as well as an amount of money,
    and finds the least number of coins you need to satisfy the amount."""
    if amount == 0:
        return [0,[]]
    elif coins == [] or amount < 0:
        return [float("inf"),[]]
    else:
        use_it = giveChange(amount - coins[0],coins)
        use_it = [use_it[0] + 1, use_it[1] + [coins[0]]]
        lose_it = giveChange(amount,coins[1:])
        return min(use_it,lose_it)
        
 
# Here's the list of letter values and a small dictionary to use.
# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 1
' Implement wordsWithScore() which is specified below.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def wordsWithScore(dct, scores):
    '''List of words in dct, with their Scrabble score.

    Assume dct is a list of words and scores is a list of [letter,number]
    pairs. Return the dictionary annotated so each word is paired with its
    value. For example, wordsWithScore(Dictionary, scrabbleScores) should
    return [['a', 1], ['am', 4], ['at', 2] ...etc... ]
    '''
    def letterScore(letter, scorelist):
        """This function takes 2 inputs, a letter and a scorelist, and finds the letter
        in the scorelist, returning the corresponding score."""
        if scorelist == []:
            return []
        elif scorelist[0][0] == letter:
            return scorelist[0][1]
        else:
            return letterScore(letter,scorelist[1:])

    def wordScore(S):
        """This function takes a string S and a scorelist, and returns the total value of S
        after it has had letterScore applied to each letter."""
        if S == "" or scores == []:
            return ['',0]
        return [S,letterScore(S[0],scores) + wordScore(S[1:])[1]]

    return list(map(wordScore,dct))

    
    
    



'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 2
' For the sake of an exercise, we will implement a function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
' (Notice that you cannot assume anything about the length of the list.)
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def take(n, L):
    '''Returns the list L[0:n], assuming L is a list and n is at least 0.'''
    if L == [] or n == 0:
        return []
    return [L[0]] + take(n-1,L[1:])




'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 3
' Similar to problem 2, will implement another function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def drop(n, L):
    '''Returns the list L[n:], assuming L is a list and n is at least 0.'''
    if n == 0:
        return L
    return drop(n-1,L[1:])


