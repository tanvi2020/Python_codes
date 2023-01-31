#Input number of rows and columns.
#For rows of rectangle run the outer loop from 1 to rows.

#for (i = 1; i < = rows; i++)
#For column of rectangle run the inner loop from 1 to columns.

#for (j = 1; j < = columns; j++)
#Print star for first or last row or for first or last column, otherwise print blank space.

#After printing all columns of a row, print new line after inner loop.

#  ***********
# *                  *
# *                  *
# *                  *
# *                  *
# ************

def hollow_rectangle(row,col):
    for i in range(1,row+1):
        for j in range(1,col+1):
            if(i==1 or i==row or j==1 or j==col):
                print('*',end=' ')
            else:
                print(end=' ')
        print()
row=int(input('Enter rows: '))
col=int(input('Enter columns: '))
print(hollow_rectangle(row,col))

def hollow_square(n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if (i==1 or i==n or j==1 or j==n):
                print('@',end=' ')
            else:
                print(end=' ')
    print(')
n=int(input('Enter square sides n:'))
print(hollow_square(n))