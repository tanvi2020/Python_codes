#a string is split into two sub_strings. if sub1 char1 matches sub2 reverse chr last...then it is considered a palindrome string
#start=starting index ie. 0            end=last index value           ,mid=middle of the string where it will get divided into 2 sub strings

def palindrome(str):
    start=0
    last=len(str)-1
    mid=(len(str)-1)//2
    flag=0
    while(start<=mid):
        if (str[start]==str[last]):
            start+=1
            last-=1
            flag=1
        else:
            flag=0
            break
    if flag==1:
        print('Palindrome')
    else:
        print('Not Palindrome')
str=input('Enter a string: ')
print(palindrome(str))