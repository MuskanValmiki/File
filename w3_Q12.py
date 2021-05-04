file1=open("w3_Q12ans.py","w")
a=["aditya","kajal","muskan","kashish"]
i=0
while i<len(a):
    file1.write(a[i])
    file1.write("\n")
    i+=1
file1.close()
