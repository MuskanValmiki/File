# f=open("w3_Q11.txt","w")
# a=f.write("hey \ni am muskan\ni am from utter pradesh")
# print(a)
# f.close()
# #size of file



def remove_newlines(fname):
    flist = open(fname).readlines()
    print(flist)
    # return [s.rstrip('\n') for s in flist]

print(remove_newlines("w3_Q11.txt"))

 