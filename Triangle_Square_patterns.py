######
######
######
######
print('SIMPLE SQAURE PATTERN IN PYTHON')
for row in range(5):
    for col in range(5):
        print('#',end=' ')
    print()

#
# #
# # #
# # # #
print('LEFT TRIANGLE ')
for row in range(5):
    for col in range(row):
        print('*',end=' ')
    print()

print('LEFT DOWNWARD TRIANGLE ')
# # # #
# # #
# #
#
for row in range(5):
    for col in range(5-row):
        print('$',end=' ')
    print()


#Print Hollow Square Star Pattern
print('HOLLOW SQUARE PATTERN')
# # # #

#    #

#    #

# # # #

#To create hollow pattern again run a nested for loop.
#External loop will be same as the previous square pattern but inside internal loop you will have to check the condition.
#f its the first or last row or column then print onlu stars.
#Otherwise check if its the first or last column then print star else print spaces


n=int(input('Enter row and column size :  '))
for row in range(n):  #outer loop
    for  col in range(n): #outer loop
        if row==0 or row==n-1 or col==0 or col==n-1:         #inner loop to print first and last row/col stars
            print('*',end='')
        else:
            print(' ',end='')

    print()


#RIGHT DOWNWARD TRIANGLE

#####
  ####
    ###
      ##
        #

print('Right Downward Triangle')
size=int(input('Enter row and col size: '))
for row in range(size):
    for col in range(row):    #Loop for spaces : column = rows
        print('_',end='  ')
    for col in range(size,row,-1):  #loop to print * . This loop runs in reverse
        print('@',end=' ')
    print()



#Create a loop that will run for the number of rows (size).
#Inside this we will have 2 loops, first will print spaces and second will print stars. (look at pattern above)
#Spaces will be printed for size - i times and stars will be printed for i times. Where i is the current row.
#Print new line at the end of both internal loops.
                #
            # #
        # # #
    # # # #
# # # # #

print('RIGHT UPWARD TRIANGLE ')
for row in range(5):
    for col in range(5-row):  #total number of spaces = total no. of rows - current row number
        print('_',end='  ')
    for col in range(row+1): #total number of star = current row number
        print('*',end='  ')
    print()


#Hollow TRIANGLE PATTERN
#First run a loop  in which apply two conditions:
# first col and last row stars will get printed    AND   if row_number==column_number then print *
#IF both these conditions fail then print space

#
#   #
#       #
#           #
#               #
#  #  #  # #  #
print('Hollow Triangle Pattern')
n=int(input('Enter row and col size n : '))
for row in range(1,n):
    for col in range(1,row+1):
        if row==n-1  or col == 1  or col==row:
            print('*',end='  ')
        else:
             print('_',end='  ')
    print()


print('Hollow Triangle Numbered Pattern')
for row in range(1,6):
    for col in range(1,6):
        if col==1 or row==5 or col==row:
            print(col,end='  ')
        else:
            print('  ',end='  ')
    print()


print('Numbered Left Triangle Pattern')
for row in range(5):
    for col in range(row):
        print(row,end='  ')
    print()
for row in range()





