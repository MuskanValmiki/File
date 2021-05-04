a=[]
b=[]
f=open("interview.txt","r")
data=f.read()
l=data.split()
i=0
while i<len(l):
    if i%2!=0:
        a.append(l[i])
    else:
        b.append(l[i])
    i+=1
d={}
list=[]
dic={}
j=0
while j<len(a):
    d[b[j]]=a[j]
    j+=1
list.append(d)
dic["user"]=list
print(dic)
