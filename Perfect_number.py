#Perfect number is a positive integer that is equal to the sum of its proper divisors.
#Example n=14
#Proper divisors of 14 are 1,2,7
#Sum of the divisors is 10
#14 is not a perfect number
#Input n
#Initialize sum=0
#Iterate through loop and find the divisors of n and add the divisors to the sum
#Check whether the sum is equal to n
#If equal display “Perfect number”
#else display “Not perfect number”
num=int(input('Enter num: '))
sum=0
for i in range(1,num):
    if num%i==0:
        sum=sum+i

if sum==num:
    print('PERFECT!!!')
else:
    print('Not Perfect.......')


