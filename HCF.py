#Step 1. Start
#Step 2. Take two user input and store into int type variable. such as num1 and num2.
#Step 3. Create a list name as arr.
#Step 4. Now, check if num1 > num2, then store num2 value in smaller variable.
#Step 5. Else, Store num1 value in smaller variable.
#Step 6.  Run a for loop starts from 1 to smaller+1.
#Step 7. Inside the for loop, check num % i == 0 and num2 % i == 0. If both conditions are true then only add element to list.
#Step 8. Finally, Print the max element of an array.
#Stop 9. Stop

 #HCF is also called as the greatest common divisor GCD

def fun(num1,num2):
    list=[]
    if num1>num2:
        smaller=num2
    else:
        smaller=num1
    for i in range(1,smaller+1):
        if(num1%i==0) and (num2%i==0):
            list.append(i)

    print("The HCF of given numbers is {}".format(max(list)))
    print('The LCF of given numbers is {}'.format(min(list)))

num1=int(input('Enter num1: '))
num2=int(input('Enter num2: '))
print(fun(num1,num2))
