f=open("Question3.txt","r")
f1=open("delhi.txt","w")
f2=open("simla.txt","w")
f3=open("other.txt","w")
data=f.read()
data1=data.split("\n")
for i in range (0,len(data1)):
    if "delhi" in data1[i]:
        f1.write(data1[i])
        f1.write("\n")
    elif "shimla" in data1[i]:
        f2.write(data1[i])
        f2.write("\n")
    else:
        f3.write(data1[i])
        f3.write("\n")
f.close()
f1.close()
f2.close()
f3.close()
f=open("Question3.txt","r")
f1=open("delhi.txt","r")
f2=open("simla.txt","r")
f3=open("other.txt","r")
print(f1.read())
print(f2.read())
print(f3.read())


