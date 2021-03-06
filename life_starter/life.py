#
# life.py - Game of Life lab
#
# Name:  Joseph Carbonell
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
#

import random
import sys

def createOneRow(width):
    """Returns one row of zeros of width "width"...  
       You should use this in your
       createBoard(width, height) function."""
    row = []
    for col in range(width):
        row += [0]
    return row


def createBoard(width, height):
    """Returns a 2D array with "height" rows and "width" cols """
    A = []
    for row in range(height):
        A += [createOneRow(width)]
    return A

def printBoard( A ): 
    """ this function prints the 2d list-of-lists 
        A without spaces (using sys.stdout.write) 
    """ 
    for row in A: 
        for col in row: 
            sys.stdout.write( str(col) ) 
        sys.stdout.write( '\n' )

def diagonalize(width,height): 
    """ creates an empty board and then modifies it 
        so that it has a diagonal strip of "on" cells. 
    """ 
    A = createBoard( width, height ) 
     
    for row in range(height): 
        for col in range(width): 
            if row == col: 
                A[row][col] = 1 
            else: 
                A[row][col] = 0      
 
    return A

def innerCells(w, h):
    """ creates an empty board and then modies it
        so that all cells are "on" except a one-
        cell-wide border of empty cells """
    A = createBoard(w, h)
    for row in range(h):
        for col in range(w):
            if row == 0 or row == (h-1) or col == 0 or col == (w-1):
                A[row][col] = 0
            else:
                A[row][col] = 1
    return A

def randomCells(w,h):
    """ creates an empty board and then modies it
        so that random cells are "on" except a one-
        cell-wide border of empty cells """
    A = createBoard(w, h)
    for row in range(h):
        for col in range(w):
            if row == 0 or row == (h-1) or col == 0 or col == (w-1):
                A[row][col] = 0
            else:
                A[row][col] = random.choice( [0,1])
    return A

def copy(A):
    """ creates an empty board of the same
        dimensions as A and then modifies it
        so each cell matches A """
    newA = createBoard(len(A[0]),len(A))
    for row in range(len(A)):
        for col in range(len(A[0])):
            newA[row][col] = A[row][col]
    return newA

def innerReverse(A):
    """ creates a copy of A then inverses
        all cells except for the outer
        border """
    reversedA = copy(A)
    for row in range(len(A)):
        for col in range(len(A[0])):
            if (row != 0 and row != (len(A)-1) and col != 0 and col != (len(A[0])-1)):
                if reversedA[row][col] == 0:
                    reversedA[row][col] = 1
                else:
                    reversedA[row][col] = 0
    return reversedA


def countNeighbors( row, col, A):
    """ returns the number of live neighbors
        of the cell at [row][col] in A """
    alive = 0
    for currentRow in range(row-1,row+2):
        for currentCol in range(col-1, col+2):
            if ((currentRow == row and currentCol == col) == False):
                if A[currentRow][currentCol] == 1:
                    alive += 1
    return alive


def next_life_generation( A ): 
    """ makes a copy of A and then advanced one 
        generation of Conway's game of life within 
        the *inner cells* of that copy. 
        The outer edge always stays 0. 
    """
    newA = copy(A)
    for row in range(len(A)):
        for col in range(len(A[0])):
            if (row != 0 and row != (len(A)-1) and col != 0 and col != (len(A[0])-1)):
                neighborsAlive = countNeighbors(row,col,A)
                if neighborsAlive < 2:
                    newA[row][col] = 0
                elif neighborsAlive > 3:
                    newA[row][col] = 0
                elif neighborsAlive == 3:
                    newA[row][col] = 1
    return newA
                    
                    
    
    
                


