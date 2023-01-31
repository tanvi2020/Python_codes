def reverse():
    str = 'Tanvi is a good girl. she is active. she loves singing'
    r=str.split(' ')
    rev=' '.join(reversed(r))
    print(rev)

print(reverse())


a='this is a paragraph to reverse a string. Also you have to capitlaize the firts letter of this para.'
b='You HAve To TuRn AlL CaPiTAl LeTtERs InTO sMAll aND aLL SmALl CaSE lETters iNtO UpPeR CasE'
c='turn into upper '
d='TURN INTo LOWER'
Cap=a.capitalize()
swap=b.swapcase()
up=c.upper()
low=d.lower()
v=a.split(' ')
verse=' '.join(reversed(v))
print(verse)
print(Cap)
print(swap)
print(up)
print(low)

mystr="wir rgkpoh gorkhpt gfodkhgfk"
s=mystr.split(' ') #split by space
print('#'.join(s)) #join by hash
