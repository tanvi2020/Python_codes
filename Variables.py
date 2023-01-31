# variables are nothing but blocks which have a name , and address and a value in it


#Variables with same values will point to the same address location
a =5
b=5
print('address of a :   ',id(a))
print('address of b : ',id(b))

#If we change value of 'a' and 'b' then they will point to a different memory location
a=10
print('new id of a : ', id(a))
b=20
print('new id of b : ',id(b))

#now what about old value 5 , if it remains unused then it will go for garbage collection
#python does not have making variable constant concept

print(type(a))  #this will return datatype of variable

comp = 12+3j  #complex type variable
print(type(comp))
c=10
b=str(c)
print('type of c before :  =  ',type(c))
print('type of c after : ',type(b))

print(int(True))  #Value of true is 1
print(int(False))  # Value of False is 0

r=10
for i in range(0,r+1):
    print(i)

print(list(range(0,5)))
