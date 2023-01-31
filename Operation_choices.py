#Int OperationChoices(int c, int a , int b )

#The function accepts 3 positive integers ‘a’ , ‘b’ and ‘c ‘ as its arguments. Implement the function to return.

#( a+ b ) , if c=1
#( a – b ) , if c=2
#( a * b ) ,  if c=3
#(a / b) ,  if c =4
#Assumption : All operations will result in integer output.

#Example:

#Input
#c :1
#a:12
#b:16
#Output:
#Since ‘c’=1 , (12+16) is performed which is equal to 28 , hence 28 is returned.
def operations(a,b,c):
    result=0
    if c==1:
        return (a+b)
    if c==2:
        return (a-b)
    if c==3:
        return (a*b)
    if c==4:
        return (a/b)
a=int(input('Enter a: '))
b=int(input('Enter b: '))
c=int(input('Enter c: '))
print(operations(a,b,c))