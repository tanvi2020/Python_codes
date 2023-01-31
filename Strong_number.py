def strong(num):
    temp=num
    sum=0
    while(temp):
        digit=temp%10
        temp=temp//10
        fact=1
        for i in range(1,digit+1):
            fact=fact*i
        sum+=fact
    if sum==num:
        print('STRONG NUMBER !!!')
    else:
        print('Not a strong number....')
num=int(input('Enter a number: '))
print(strong(num))
