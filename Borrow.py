def subtraction(num1,num2):
    count=0
    borrow=0
    if len(num1)<=len(num2):
        l=len(num1)-1
    else:
        l=len(num2)-1
    for i in range(l+1):
        temp=int(num1[l-i])-int(num2[l-i])+borrow
        if len(str(temp))>1:
            count+=1
            borrow=1
        else:
            borrow=0
    print("count of borrows generated is {} ".format(count+borrow))
num1=input('Enter num1: ')
num2=input('Enter num2: ')
print(subtraction(num1,num2))