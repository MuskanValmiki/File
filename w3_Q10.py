f=open("w3_Q10.txt","r")
a=f.read().split()
i=0
empty=[]
while i <len(a):
    j=0
    e=[]
    c=0
    while j<len(a):
        if a[i]==a[j]:
            c+=1
        j+=1
    e.append(a[i])
    e.append(c)
    if e not in empty:
        empty.append(e)
    i+=1
print(empty)
f.close()
# count the frequeny  