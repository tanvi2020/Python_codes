def leap(year):
    if year%4==0:
        print('LEAP YEAR!!')
    else:
        print('Not a leap year.......')
year=int(input('Enter year: '))
print(leap(year))

def leap_century(century):
    if century%400==0:
        print('LEAP CENTURY!!')
    else:
        print('Not a leap century......')
century=int(input('Enter century:' ))
print(leap_century(century))