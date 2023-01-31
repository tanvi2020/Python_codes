def digits(num):
    temp=num
    while num>1:
        rem=num%10
        n=(num*10)+rem
        num=num//10
    print('sum of {} is {}'.format(temp,n))
num=int(input('Enter num: '))
print(digits(num))