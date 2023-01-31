#Sequence is 0,1,1,2,3,5,8,13,21, 34
#Take a user input and store into int type num variable.
#Initialize n1, n2 variable to 0, 1.
#Inside for loop, using arithmetic addition method, and calculate the n3, where n3 = n1 + n2. Then initialize n1 = n2 and n2 = n3.
#Print n3 inside the loop.
def fibo(num):
    n1=0
    n2=1
    print(n1)
    print(n2)
    for i in range(2,num+1):
        i=n1+n2
        n1=n2
        n2=i
        print(i)
num=int(input('Enter num: '))
print(fibo(num))