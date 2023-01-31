#The format() method formats the specified value(s) and insert them inside the string's placeholder.


def rev(num):
    reverse=0
    temp=num
    x=num
    while num>0:
        remainder=num%10
        reverse=(reverse*10)+remainder
        num = num // 10

    print("Reverse of {} is {}".format(temp,reverse))
    if x==reverse:
        print('Palindrome')
    else:
        print('Not Palindrome...')
num=int(input('Enter num: '))
print(rev(num))