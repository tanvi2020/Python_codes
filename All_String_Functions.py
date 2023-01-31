#capitalize()	Converts the first character to upper case
#casefold()	Converts string into lower case
#center()	Returns a centered string
#count()	Returns the number of times a specified value occurs in a string
#encode()	Returns an encoded version of the string
#endswith()	Returns true if the string ends with the specified value
#expandtabs()	Sets the tab size of the string
#find()	Searches the string for a specified value and returns the position of where it was found
#format()	Formats specified values in a string
#format_map()	Formats specified values in a string
#index()	Searches the string for a specified value and returns the position of where it was found
#isalnum()	Returns True if all characters in the string are alphanumeric
#isalpha()	Returns True if all characters in the string are in the alphabet
#isascii()	Returns True if all characters in the string are ascii characters
#isdecimal()	Returns True if all characters in the string are decimals
#isdigit()	Returns True if all characters in the string are digits
#isidentifier()	Returns True if the string is an identifier
#islower()	Returns True if all characters in the string are lower case
#isnumeric()	Returns True if all characters in the string are numeric
#isprintable()	Returns True if all characters in the string are printable
#isspace()	Returns True if all characters in the string are whitespaces
#istitle()	Returns True if the string follows the rules of a title
#isupper()	Returns True if all characters in the string are upper case
#join()	Converts the elements of an iterable into a string
#ljust()	Returns a left justified version of the string
#lower()	Converts a string into lower case
#lstrip()	Returns a left trim version of the string
#maketrans()	Returns a translation table to be used in translations
#partition()	Returns a tuple where the string is parted into three parts
#replace()	Returns a string where a specified value is replaced with a specified value
#rfind()	Searches the string for a specified value and returns the last position of where it was found
#rindex()	Searches the string for a specified value and returns the last position of where it was found
#rjust()	Returns a right justified version of the string
#rpartition()	Returns a tuple where the string is parted into three parts
#rsplit()	Splits the string at the specified separator, and returns a list
#rstrip()	Returns a right trim version of the string
#split()	Splits the string at the specified separator, and returns a list
#splitlines()	Splits the string at line breaks and returns a list
#startswith()	Returns true if the string starts with the specified value
#strip()	Returns a trimmed version of the string
#swapcase()	Swaps cases, lower case becomes upper case and vice versa
#title()	Converts the first character of each word to upper case
#translate()	Returns a translated string
#upper()	Converts a string into upper case
#zfill()	Fills the string with a specified number of 0 values at the beginning
#removeprefix() Removes the specified prefix substring from the given string
#removesuffix() Removes the specified suffix substring and returns only the prefix string

str1='tanviSushil'
str2='        boooooo          '
str3="name:Tanvi"
str4="ADJKHFSKJFDK"
str5="GnGkHFDLFwewAL"
str6="hey Tanvi. How are you Tanvi? How's your python tutorial going Tanvi. Hope you are doing well Tanvi"
str7='12HG445JK'
str8='7796103180'
print("Capitlize: ",str1.capitalize())
print("Casefold: ",str4.casefold())
print("Center: ",str1.center(20))    #center(width)
print("count: ",str1.count("i"))  #count(self,'x',start,end)
print("UPPER: ",str2.upper())
print("lower: ",str4.lower())
print("isupper: ",str2.isupper())
print("islower: ",str2.islower())
print("strip: ",str2.strip())
print("lstrp: ",str2.lstrip())
print("rstrip:",str2.rstrip())
print("Swapcase:: ",str5.swapcase())
print("removeprefix: ",str3.removeprefix("name:"))
print("removesuffix: ",str3.removesuffix("Tanvi"))
print('replace:',str6.replace('Tanvi','Tanu'))
print('replace: ',str2.replace(' ','-'))
print("split: ",str6.split(' '))
print("split: ",str6.split(' ',maxsplit=3)) #split the string and max no. of spilts are 3
print("split: ",str6.rsplit(' ',maxsplit=1)) # split string from right side and max no. of split=1
mystr=str6.split(' ')
print("join: ",'/'.join(mystr))
print('isalpha:',str5.isalpha())
print("isnumeric: ",str8.isnumeric())
print("isalnum: ",str7.isalnum())



