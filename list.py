f=open("list.txt","r")
i=0
m=(f.read()).split(",")
while i<len( m):
    print(m[i])
    i+=1
f.close()
