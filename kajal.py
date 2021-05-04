a=[1,2,3,4,5,6,7,8,9,10]
f=open("kajal.txt","w")
i=0
c=[]
while i<len(a):
    if a[i]%2==0:
        d=a[i]
        c.append(d)
    i+=1
f.write(str(c))
f.close()
