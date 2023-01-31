def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact

def strong(n):
    temp=n
    sum=0
    while(temp):
        digit=temp%10
        temp=temp//10
    sum+=factorial(digit)
    return sum==n

start=int(input('Enter start:'))
end=int(input('Enter end:'))
for i in range(start,end+1):
    if strong(i):
        print(i)

