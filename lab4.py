############################################################
# Name: Joseph Carbonell
# Pledge: I pledge my honor that I have abided by the Stevens Honor Code.
# CS115 Lab 4
#  
############################################################

def knapsack(capacity,itemList):
    """This function takes two inputs, a capacity and an itemList containing
    weight value pairs. It then returns a list containing the maximum value able to
    fit in the knapsack, and the list of items that make that value."""
    if capacity == 0 or itemList == []:
        return [0,[]]
    elif capacity - itemList[0][0] < 0:
        return knapsack(capacity,itemList[1:])
    else:
        use_it = knapsack(capacity - itemList[0][0],itemList[1:])
        lose_it = knapsack(capacity,itemList[1:])
        use_it = [use_it[0] + itemList[0][1], [itemList[0]] + use_it[1]]
        if use_it[0] > lose_it[0]:
            return use_it
        else:
            return lose_it
 
            
                 


