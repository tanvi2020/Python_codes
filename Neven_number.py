#if a number is divisible by the sum of its digits
num = 156
rem = sum = 0

# Make a copy of num and store it in variable n
n = num

# Calculates sum of digits
while (num > 0):
    rem = num % 10
    sum = sum + rem
    num = num // 10

# Checks whether the number is divisible by the sum of digits
if (n % sum == 0):
    print(rem);
    print(str(n) + " is a neven number")
else:
    print(str(n) + " is not a neven number")