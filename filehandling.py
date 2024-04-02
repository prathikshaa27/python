import os
f = open("sample.txt","r")
print(f.read(2))

f= open("sample.txt","a")
f.write("Iam from coimbatore")
f.close()

f=open("sample.txt")
print(f.read())

f=open("sample.txt","w")
f.write("The content will be over written")
f.close()

f=open("sample.txt")
print(f.read())


#deleting a file
if os.path.exists("demo.txt"):
    os.remove("demo.txt")
else:
    print("There is no such file")