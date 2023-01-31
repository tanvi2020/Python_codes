#Python bin() function returns the binary string of a given integer.
#Syntax:  bin(a)
#Parameters : a : an integer to convert
#Return Value : A binary string of an integer or int object.

#Exceptions : Raises TypeError when a float value is sent in arguments.

print(bin(7))   #decimal to binary conversion
print(bin(8).replace('0b'," "))
print(oct(5))
print(hex(14))

print('Code for binary to decimal conversion')
def func(number):
    binary=number  #binary=100
    dec=0
    i=0
    while(binary!=0): #100!=0   TRUE                                                                                                                                Condition: FALSE
        temp=binary%10              #100%10=0                    10%10=0                                            1%10=1
        dec=dec+temp*pow(2,i) #0+0*(2,0)=0                   0+0*(2,1)=0                                      0+1*pow(2,2)=4
        binary=binary//10          #100//10=10                     10//10=1                                          1//10=0                           binary=0
        i+=1                            #i=0                                   i=1                                                   i=2
    print(dec)

if __name__=="__main__":
    func(100)
print("Code 2 for binary to decimal")
def convert(num):
    return int(num,2)
if __name__=="__main__":
    print(convert('1001'))

