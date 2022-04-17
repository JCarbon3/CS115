############################################################
# Name: Joseph Carbonell
# Pledge: I pledge my honor that I have abided by the Stevens Honor Code.
# CS115 Lab 3
#  
############################################################

def change(amount,coins):
    """This function takes a list of possible coins as well as an amount of money,
    and finds the least number of coins you need to satisfy the amount."""
    if amount == 0:
        return 0
    elif coins == [] or amount < 0:
        return float("inf")
    else:
        use_it = change(amount - coins[0],coins) + 1
        lose_it = change(amount,coins[1:])
        return min(use_it,lose_it)
 
            
                 


