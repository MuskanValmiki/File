f=open("w3_Q8.txt","r")
a=f.read().split()
max=a[0]
i=0
while i<len(a):
    j=0
    while j<len(a):
        if len(a[i])>len(a[j]):
            if len(a[i])>len(max):
                max=(a[i])
        j+=1
    i+=1
print(max)
f.close()
# which word is longest


