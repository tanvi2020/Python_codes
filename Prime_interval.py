#The idea to solve this problem is to iterate the val from start to end using a for loop and for every number,
#if it is greater than 1, check if it divides n(smallest prime number ie. 2). If we find any other number which divides, print that value.
def prime(start,end):
    for i in range(start,end+1):
            if i>1:
                for j in range(2, i):
                    if i%j==0:
                        break
                else:
                    print(i)
start=int(input('Enter start : '))
end=int(input('Enter end: '))
print(prime(start,end))