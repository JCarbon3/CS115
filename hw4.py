############################################################
# Name: Joseph Carbonell
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
# CS115 Homework 4
#  
############################################################

def add_row(lst):
    """Returns a list of the sums of adjacent terms in a row"""
    if lst == []:
        return []
    if len(lst) == 1:
        return [1]
    return [lst[0] + lst[1]] + add_row(lst[1:])


def pascal_row(rows):
    """Returns the list of numbers to make a row of the pascal's triangle"""
    if rows == 0:
        return [1]
    if rows == 1:
        return [1,1]
    return [1] + add_row(pascal_row(rows-1))

def pascal_triangle(rows):
    """Returns a list of list representing the rows of a pascal's triangle"""
    if rows == 0:
        return [[1]]
    if rows == 1:
        return [[1],[1,1]]
    return pascal_triangle(rows-1)+[pascal_row(rows)]
    

def test_pascal_row():
    assert pascal_row(0) == [1]
    assert pascal_row(1) == [1,1]
    assert pascal_row(5) == [1,5,10,10,5,1]
    assert pascal_row(7) == [1,7,21,35,35,21,7,1]

def test_pascal_triangle():
    assert pascal_triangle(0) == [[1]]
    assert pascal_triangle(1) == [[1],[1,1]]
    assert pascal_triangle(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]
    assert pascal_triangle(7) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1], [1, 6, 15, 20, 15, 6, 1], [1, 7, 21, 35, 35, 21, 7, 1]]

                 
