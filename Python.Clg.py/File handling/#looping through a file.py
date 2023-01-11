#Looping through a file

f= open("TextFile.txt.py","r")
for x in f:
    print("*",x)

f= open("demoFile.txt","w")
f.write("And oft when on my couch I lie, ")
f.close()

f= open("DemoFile.txt","a")
f.write("In vacant or in pensive mood, \n")
f.write("They flash upon that inward oye ")
f.close()

str=""
f= open("DemoFile.txt","r")
for x in f:
    str +=x
    print("*",x)

print("\nstr :",str)
