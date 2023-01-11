#file handling:
f=open('file2.txt','r')
print(f.read())
acount=0
ecount=0
icount=0
ocount=0
ucount=0
vowels={"a":acount,"e":ecount,"i":icount,"o":ocount,"u":ucount}
str=file2.txt
total=0
for s in str:
    if s=="a" or s=="A":
        vowels["a"]+=1
    elif s=="e" or s=="E":
        vowels["e"]+=1
    elif s=="i" or s=="I":
        vowels["i"]+=1
    elif s=="o" or s=="O":
        vowels["o"]+=1
    elif s=="u" or s=="U":
        vowels["u"]+=1

    total+=1

print(vowels)
print("tatal character=",total)
print("tatal no. of vowels =",vowels["a"]+vowels["e"]+vowels["i"]+vowels["o"]+vowels['u'])
