#The Binary number system only uses two digits, 0 and 1 and  number system can be called binary string.
# You are required to implement the following function:

#int OperationsBinaryString(char* str);

#The function accepts a string str as its argument. The string str consists of binary digits eparated with an alphabet as follows:

# A denotes AND operation
# B denotes OR operation
# C denotes XOR Operation
#You are required to calculate the result of the string str,
# scanning the string to right taking one opearation at a time, and return the same.

#No order of priorities of operations is required
#Length of str is odd
#If str is NULL or None (in case of Python), return -1
#Input:

#str: 1C0C1C1A0B1

#Output:

#1
import string
import re
def Operations(str):
    a=int(str[0])
    i=1
    while i<len(str):
        if str[i]=='A' :   #AND operation
            a&= int(str[i+1])
        if str[i]=='B' :      #OR operation
            a|=int(str[i+1])
        if str[2]=='C' :     #XOR operation
            a^=int(str[i+1])
        i+=2
    return a
str=input()
print(Operations(str))
