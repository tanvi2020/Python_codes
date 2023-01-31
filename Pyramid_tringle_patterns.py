#left triangle pattern
def pattern(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print('#',end=' ')
        print()
n=int(input('Enter n:'))
print(pattern(n))

#right triangle pattern
def pattern3(v):
    k=2*v-2
    #main loop
    for i in range(0,v):
        #for spaces inner loop
        for j in range(0,k):
            print(end=' ')
        k=k-2
        #for printing @
        for j in range(0,i+1):
            print('*',end='')
        print("\r")
v=int(input('Enter v: '))
print(pattern3(v))

#pyramid pattern
def pyramid(p):
    k=2*p-2
    for i in range(0,p):
        for j in range(0,k):
            print(end=' ')
        k=k-2
        for i in range(0,i+1):
            print('A ',end=' ')
        print()
p=int(input('Enter p: '))
print(pyramid(p))

#numbered left triangle(non-repeting numbers)
def triangle(t):
    num=1
    for i in range(0,t): #for rows
        for j in range(0,i+1):  #for columns
            print(num,end=' ')
            num+=1
        print()
t=int(input('Enter t: '))
print(triangle(t))

#numbered left triangle(repeating numbers)
def tri(r):
    num=1
    for i in range(0,r):
        for j in range(0,i+1):
            print(num,end=' ')
        num+=1
        print()
r=int(input('Enter r: '))
print(tri(r))

#numbered left triangle incrementing number series
def trinum(a):
    num=1 #initialize num
    for i in range(0,a):
        num=1 #re assign num
        for j in range(0,i+1):
            print(num,end=' ')
            num+=1
        print()
a=int(input('Enter a: '))
print(trinum(a))

#Left sided Alphabet triangle
def alpha(b):
    num=65
    for i in range(0,b):
        for j in range(0,i+1):
            ch=chr(num)
            print(ch,end=' ')
            num+=1
        print()
b=int(input('Enter b: '))
print(alpha(b))

def alpha_pyramid(alp):
    k=2*alp-2
    num=65
    for i in range(0,alp):

        for j in range(0,k):
            print(end=' ')
        k=k-2
        for j in range(0,i+1):
            ch = chr(num)
            print(ch,end='  ')
            num+=1
        print()
alp=int(input('Enter alp:'))
print(alpha_pyramid(alp))