#char*MoveHyphen(char str[],int n);

#The function accepts a string “str” of length ‘n’, that contains alphabets and hyphens (-).
# Implement the function to move all hyphens(.) in the string to the front of the given string.

#NOTE:- Return null if str is null.

#Example :-

#Input:
#str.Move-Hyphens-to-Front
#Output:
#-MoveHyphenstoFront
#Explanation:-

#The string “Move-Hyphens -to-front” has 3 hyphens (.), which are moved to the front of the string, this output is “— MoveHyphen”
def hyphenshift(str,length):
    hyphen=0
    chars=" "
    for i in str:
        if i=='-':
            hyphen+=1
        else:
            chars+=i
    print('-'*hyphen,chars)
length=int(input('Enter length: '))
str=input('Enter a string: ')
print(hyphenshift(str,length))
