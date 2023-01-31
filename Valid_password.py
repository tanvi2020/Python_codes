#Minimum 8 characters.
#The alphabets must be between [a-z]
#At least one alphabet should be of Upper Case [A-Z]
#At least 1 number or digit between [0-9].
#At least 1 character from [ _ or @ or $ ].
# Module of regular expression is used with search()
#Here we have used the re module that provide support for regular expressions in Python.
# Along with this the re.search() method returns False (if the first parameter is not found in the second parameter)
# This method is best suited for testing a regular expression more than extracting data.
# We have used the re.search() to check the validation of alphabets, digits or special characters.
# To check for white spaces we use the “\s” which comes in the module of the regular expression.


import re
def  checkPass(str,n):
    flag=0
    if n==0:
        print('String Empty')
    while True :

        if n<4:
            flag=-1
            break
        elif not re.search('a-z',str):
            flag=0
            break
        elif not re.search('A-Z',str):
            flag=0
        elif not re.search('\s',str):
            flag=-1
            break
        elif not re.search('0-9',str):
            flag=-1
            break
        elif not re.search('[]_@$]',str):
            flag=-1
            break
    if flag==-1:
        print('Invalid Password....')
    else:
            print("Valid Password")
n=int(input('Enter size of string : '))
str=input('Enter string: ')
print(checkPass(str,n))
