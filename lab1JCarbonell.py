############################################################
# Name: Joseph Carbonell
# Pledge: I pledge my honor that I have abided by the Stevens Honor Code.
# CS115 Lab 1
#  
############################################################

from math import factorial
from functools import reduce

def inverse(x):
    return float(1/x)

def e(n):
    terms = list(range(1,n+1))
    factorials = list(map(factorial,terms))
    approximation = 1 + sum(map(inverse,factorials))
    return approximation
                 


