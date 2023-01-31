# A number is said to be amstrong if sum of every digit of that number raised to the power n is eqaul to the number itself
a=153
temp=a
order=len(str(a))
sum=0
while temp>0:
        digit=temp%10
        sum+=digit**order
        temp//=10
if sum==a:
        print("Amstrong number!")
else:
        print('Not an amstrong number......')

#finding amstrong number in an interval
def amstr(b):
        lower=100
        upper=3000


        for b in range(lower,upper+1):
                power=len(str(b))
                temp = b
                sum = 0
                while(temp>0):
                        digit=temp%10
                        sum+=digit**power
                        temp//=10
                if b==sum:
                        print(b)
b=int(input('Enter b: '))
print(amstr(b))