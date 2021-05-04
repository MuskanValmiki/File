f=open("w3_Q5.txt","r")
a=f.readlines()
b=[]
i=0
while i<len(a):
    b.append(a[i])
    i+=1
print(b)
f.close()
# ['Rakesh\n', 'Krishna\n', 'Aditya\n', 'Kajal\n', 'Muskan\n', 'Kashish\n']
# readline by line and append in list
