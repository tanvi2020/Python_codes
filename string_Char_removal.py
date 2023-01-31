#In Python it is all known that string is immutable.when a string reference is reinitialized with a new valueit is creating a new object rather thanoverwriting
#the previous value. In Python, strings are made immutable so that programmers cannot alter the contents of the object (even by mistake). This avoids unnecessary bugs.
#because strings don't support item assignment, thus they are immutable. Something is mutable only when
# we are able to change the values held in the memory location without changing the memory location itself.

#Ways to remove i’th character from string

str='Tanvi is studying in her room. Tanvi is a BE student. singing and cooking are hobbies of tanvi. hello tanvi. how are you tanvi'
new=str.replace('tanvi','ranganekar') #replace tanvi with ranganekar
new2=str.replace('Tanvi',' ') #remove Tanvi from the string
print('new =  ',new)
print('new2 =  ',new2)
num1='230030030400'
num2=num1.replace('0','1')
print(int(num2))

#replace method in python will replaces all occurunces of a char or word in the string. This is a case sensitive method.
#syntax:       str.replace(self,old_,new_,count/' ') where ' ' means all occurunces
#returns a copy of the string where all occurrences of a substring are replaced with another substring.