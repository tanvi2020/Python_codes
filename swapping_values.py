a=2
b=3

#method 1                               this method uses more bits so we use the xor method
a=a+b
b=a-b
a=a-b
print(a)
print(b)
#method2
a=a ^ b
b=a ^ b
a =a ^ b
print(a)
print(b)

#method3
a,b=b,a
print(a)
print(b)

#method4
temp=a
a=b
b=temp
print(a,b)

