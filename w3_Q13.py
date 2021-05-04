f=open("w3_Q13.txt","r")
a=f.read()
print(a)
f1=open("new.txt","w")
b=f1.write(a)
f1.close()
f.close()

# copy one file to another file
