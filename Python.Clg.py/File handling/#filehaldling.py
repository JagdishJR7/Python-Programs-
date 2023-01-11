#file handling

f= open("textFile.txt(2)","r")
print(f.read())

#Reading line by line :
f= open("textFile.txt(2)","r")
print(f.readline())

#Reading parts of the file
f= open("textFile.txt(2)","r")
print(f.read(10))

#Writing to a file
str=input("Enter string :")
f= open("TextFile2.txt(2)","W")
f.write(str)
f.close()

f= open("TextFile2.txt(2)","r")
print(f.read())

#Appending
f.close()
f= open("TextFile2.txt(2)","a")
print(f.Write(" Good Work\nkeep going!"))

f.close()
f= open("TextFile2.txt(2)","r")
print(f.read())
