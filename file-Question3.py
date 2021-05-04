banks_list = ["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"] 
f=open("file-Question3.txt","w")
i=0
while i<len(banks_list):
    f.write(banks_list[i])
    f.write("\n")
    i+=1
f=open("file-Question3.txt","r")
print(f.read())
f.close()
