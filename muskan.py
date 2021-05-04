a=["somi","ruchi","muskan"]
b=[23,45,67]
f=open("muskan.txt","w")
i=0
while i<len(a):
    c=a[i]+str(b[i])
    d=f.write(c)
    d=f.write("\n")
    i+=1
print(d)
f.close()


