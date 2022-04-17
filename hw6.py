'''
Created on 3/8/2022
@author:   Joseph Carbonell & Sean Scadden
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Hw 6
'''
# Number of bits for data in the run-length encoding format.
# The assignment refers to this as k.
COMPRESSED_BLOCK_SIZE = 5

# Number of bits for data in the original format.
MAX_RUN_LENGTH = 2 ** COMPRESSED_BLOCK_SIZE - 1

# Do not change the variables above.
# Write your functions here. You may use those variables in your code.

def numToBinary(n):
    '''Returns the binary equivalent of a non-negative integer n,
        or an empty string if n is 0'''
    if n == 0:
        return ""
    return numToBinary(int(n / 2)) + str(n % 2)
    
def binaryToNum(s):
    '''Returns the integer equivalent of a binary string, an empty string
        returns 0'''
    if s == "":
        return 0
    return binaryToNum(s[:-1]) * 2 + int(s[-1])
                        
def finishFiveBit(s):
    '''Adds 0s to a binary number of less than 5 bits to make it 5 bits'''
    return "0" * (5-len(s)) + s

def compress(s):
    '''Compress binary string and returns compressed version'''
    def compress_helper(s,tracker):
        '''Return a 2 item array, with the first representing whether we are tracking 1 or 0,
            and the second element tracking the consecutive number of the first in s'''
        if s == "":
            return [tracker]
        if s[0] != tracker[0] and tracker[1] != 0:
            return [tracker] + compress_helper(s[1:], [s[0]] + [1])
        return compress_helper(s[1:],[s[0]] + [tracker[1] + 1])

    def compress_arrays(array):
        '''Take arrays from compress_helper and return the corresponding binary string
            for each array combined.'''
        if array == []:
            return ""
        if array[0][1] > MAX_RUN_LENGTH:
            return "1111100000" + compress_arrays([[array[0][0]] + [array[0][1]-31]] + array[1:])
        return finishFiveBit(numToBinary(array[0][1])) + compress_arrays(array[1:])
    return ("00000" if s[0] == "1" else "") + compress_arrays(compress_helper(s,["0",0]))

def uncompress(s):
    '''Take a compressed binary string and return uncompressed string'''
    def uncompress_to_arrays(s):
        '''Uncompress binary string into a list of arrays representing consecutive zeros and ones'''
        if s == "":
            return []
        return [binaryToNum(s[0:COMPRESSED_BLOCK_SIZE])] + uncompress_to_arrays(s[COMPRESSED_BLOCK_SIZE:])

    def uncompress_helper(array,isZero):
        '''Takes the arrays from uncompress_to_arrays and convert them back into the respective binary string'''
        if array == []:
            return ""
        return ("0" if isZero else "1") * array[0] + uncompress_helper(array[1:],not isZero)

    return uncompress_helper(uncompress_to_arrays(s),True)

'''Our compress function could use a maximum of 325 bits because a series of alternating bits starting with 1 would
   require an initial 5 bits for 0, then 5 bits for each alternating bit due to k being 5.'''

def compression(s):
    '''Return the compression ratio of the algorithm'''
    return len(compress(s)) / len(s)

'''Penguin'''
print(compression("00011000"+"00111100"*3 + "01111110"+"11111111"+"00111100"+"00100100"))
'''Smile'''
print(compression("0"*8 + "01100110"*2 + "0"*8 + "00001000" + "01000010" + "01111110" + "0"*8))
'''Five'''
print(compression("1"*9 + "0"*7 + "10000000"*2 + "1"*7 + "0" + "00000001"*2 + "1"*7 + "0"))
    
'''The more times you alternate between 1 and 0, the lower the compression rate.'''

'''Such an algorithm is impossible because an image with either alternating bits, or unique bits for every spot
   will not be possible to compress while still representing every bit.'''

        
