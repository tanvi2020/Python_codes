#int findCount(int arr[], int length, int num, int diff);

#The function accepts an integer array ‘arr’, its length and two integer variables ‘num’ and ‘diff’. Implement this function
# to find and return the number of elements of ‘arr’ having an absolute difference of less than or equal to ‘diff’ with ‘num’.
#Note: In case there is no element in ‘arr’ whose absolute difference with ‘num’ is less than or equal to ‘diff’, return -1.

#Example:
#Input:

#arr: 12 3 14 56 77 13
#num: 13
#diff: 2
#Output:
#3

#Explanation:
#Elements of ‘arr’ having absolute difference of less than or equal to ‘diff’ i.e. 2 with ‘num’ i.e. 13 are 12, 13 and 14.
#step 1:Take 4 inputs from user -  array_len, array, number and difference
#step2: inside the function initialize a counter variable as 0
#Step 3: Then run a for loop for array_len  ie. for i in range(array_len)
#step 4: if difference of array element and number<=difference then increment the count by 1 . print the count

# RE module will help to incorporate the regular expressions in python. They alllow us to search for and match specific patterns of text.

import re
def absolute(arr,len,num,diff):
    count=0
    for i in range(len):
        if (arr[i]-num<=diff):
            count+=1
    return count
len=int(input('Enter length of array: '))
num=int(input('Enter num: '))
diff=int(input('Enter difference: '))
arr=list(map(int,input("Enter array: ").split()))
print(absolute(arr,len,num,diff))