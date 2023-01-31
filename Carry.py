#The functions accepts two numbers ‘num1’ and ‘num2’ as its arguments.
# You are required to calculate and return  the total number of carries generated while adding digits of two numbers ‘num1’ and ‘ num2’.

#Assumption: num1, num2>=0

#Example:

#Input
#Num 1: 451
#Num 2: 349
#Output
#2
#Explanation:

#Adding ‘num 1’ and ‘num 2’ right-to-left results in 2 carries since ( 1+9) is 10. 1 is carried and (5+4=1) is 10,
# again 1 is carried. Hence 2 is returned.
def carry_count(num1,num2):
    count=0
    carry=0
    if len(num1)<=len(num2):
        l=len(num1)-1
    else:
        l=len(num2)-1
    for i in range(l+1):
        temp=int(num1[l-i])+int(num2[l-i])+carry
        if len(str(temp))>1:
            count+=1
            carry=1
        else:
            carry=0
    return count+carry
num1=input('Enter num1: ')
num2=input('Enter num2: ')
print(carry_count(num1,num2))