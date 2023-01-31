#Given a string. The task is to print all words with even length in the given string.
#Input: s = "This is a python language"
#Output: This
#          is
 #         python
 #         language
str='hii my name is tanvi sushil desai'
s=str.split(' ')
for words in s:
    if len(words)%2==0:
        print(words)
    else:
        pass
