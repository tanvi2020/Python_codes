
#Step 1. Start
#Step 2. Take a user input and store into int type number variable.
#Step 3. Run a for loop starts from 0 to number + 1.
#Step 4. Inside for loop, Check condition number % i == 0,
#Step 5. After condition is true, then print the loop value.
def fact(num):
    for i in range(1,num+1):
        if num%i==0:
            print(i)

num=int(input('Enter num:'))
print(fact(num))