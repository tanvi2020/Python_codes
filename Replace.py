#The function accepts a string  ‘ str’ of length n and two characters ‘ch1’ and ‘ch2’ as its arguments .
# Implement the function to modify and return the string ‘ str’ in such a way that all occurrences of ‘ch1’ in original string
# are replaced by ‘ch2’ and all occurrences of ‘ch2’  in original string are replaced by ‘ch1’.

#Assumption: String Contains only lower-case alphabetical letters.

#Note:

#Return null if string is null.
#If both characters are not present in string or both of them are same , then return the string unchanged.
#Example:

#Input:
#Str: apples

#ch1:a
#ch2:p

#Output:
#paales

#replace() is an inbuilt function in the Python programming language that returns a copy of the string
#where all occurrences of a substring are replaced with another substring.
#Syntax:

#string.replace(old, new, count)
#old – old substring you want to replace.
#new – new substring which would replace the old substring.
#count – the number of times you want to replace the old substring with the new substring. (Optional )

#this method returns copy of a tring it does not change the original string.
def swap(s,chr1,chr2):
    result=' '
    if(s!=None):
        result=s.replace(chr1,'*').replace(chr2,chr1 ).replace('*',chr2)
        return result
    return 'NULL'


s=input('Enter string: ')
chr1,chr2=map(str,input('Enter chr1 and chr2: ').split())
print(swap(s,chr1,chr2))