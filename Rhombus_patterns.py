# Solid Rhombus : Making Solid Rhombus is a bit similar to making solid square rather than the concept that for each ith row we have n-i blank spaces before stars as:
#   – – – ****
#   – – ****
#   – ****
#   ****

#Formation of Hollow Rhombus uses the idea behind formation of hollow square and solid rhombus.
# A hollow square with n-i blank spaces before stars in each ith rows result in formation of hollow rhombus.

#Hollow Rhombus:
#    *****
#   *   *
#  *   *
# *   *
#*****
def solid_rhombus(rows):
    for i in range(1,rows+1):
            for j in range(1,rows-i+1):
                print(end=' ')
            for j in range(1,rows+1):
                print('*',end='')

            print()
rows=int(input('Enter rows: '))
print(solid_rhombus(rows))

def hollow_rhombus(rows):
    for i in range(1,rows+1):
        for j in range(1,rows-i+1):
            print(end=' ')
        if i==1 or i==rows:
            for j in range(1,rows+1):
                print('@',end='')
        else:
            for j in range(1,rows+1):
                if(j==1 or j==rows):
                    print('*',end='')
                else:
                    print(end=' ')
        print()


rows=int(input('Enter rows: '))
print(hollow_rhombus(rows))