#Joseph Carbonell
#I pledge my honor that I have abided by the Stevens Honor System.

def dot(L,K):
    """This function takes 2 lists as input
    and returns the dot product of these lists."""
    if L == [] or K == []:
        return 0
    return L[0]*K[0] + dot(L[1:],K[1:])

def explode(S):
    """This function takes a string as input and
    returns a list of each character."""
    if S == "":
        return []
    return [S[0]] + explode(S[1:])

def ind(e,L):
    """"This function takes two inputs e and L, and checks for the presence
    of e in L, and returns either the index of e in L, or the length of L"""
    if L[0] == e or L[0] == '':
        return 0
    return 1 + ind(e,L[1:])

def removeAll(e,L):
    """This function takes two inputs e and L, and removes all instances of
    e in L then returns the remainder"""
    if L == []:
        return []
    elif L[0] == e:
        return [] + removeAll(e,L[1:])
    return [L[0]] + removeAll(e,L[1:])

def myFilter(f,L):
    """This function takes a predicate function f, and a list L. It removes all
    elements of L where f is false and returns the remainder"""
    if L == []:
        return []
    elif f(L[0]) == True:
        return L[0] + MyFilter(f,L[1:])

def DeepReverse(L):
    pass
        
        

    
