#take input as number and define an attribute divisor which will be the smallest prime number ie. 2, also define a empty list to store the prime factors
#run a while loop to check whether divisor<=2 if divisor==num then the process of factorization will be complete
#If division of num by divisor results in a remainder 0 then append that devisor in the list and try to divide the resultant number with the same divisor value again
#If result is not 0 then increment the divisor value by 1 .
#print the list[divisors]
def prime(num):
    divisor=2
    list_prime_factors=[]
    while divisor<=num:
        if num%divisor==0:
            list.append(divisor)
            num=num//divisor
        else:
            divisor+=1
    print(list_prime_factors)
num=int(input('Enter num: '))
print(prime(num))