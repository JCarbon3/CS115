'''
Created on 3/3/2022
@author:   Joseph Carbonell
Pledge:    I pledge my honor that I have abided by the Stevens Honor Code.

CS115 - Lab 6
'''
def isOdd(n):
    '''Returns whether or not the integer argument is odd.'''
    return n % 2 != 0

def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''
    if n == 0:
        return ""
    elif isOdd(n):
        return numToBinary(int(n/2)) + '1'
    else:
        return numToBinary(int(n/2)) + '0'


def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    if s == '':
        return 0
    else:
        return binaryToNum(s[:-1]) * 2 + int(s[-1])

def increment(s):
    '''Precondition: s is a string of 8 bits.
    Returns the binary representation of binaryToNum(s) + 1.'''
    return (('0' * 8) + numToBinary(binaryToNum(s) + 1))[-8:]

def count(s, n):
    '''Precondition: s is an 8-bit string and n >= 0.
    Prints s and its n successors.'''
    if n > 0:
        print(s)
        return count(increment(s),n-1)
    print(s)

def numToTernary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the ternary representation of non-negative integer
    n. If n is 0, the empty string is returned.'''
    if n == 0:
        return ''
    s = n % 3
    return numToTernary(int(n/3)) + str(s)

def ternaryToNum(s):
    '''Precondition: s is a string of 0s, 1s, and 2s.
    Returns the integer corresponding to the ternary representation in s.
    Note: the empty string represents 0.'''
    if s == '':
        return 0
    return ternaryToNum(s[:-1]) * 3 + int(s[-1])
