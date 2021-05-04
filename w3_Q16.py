f = open('w3_Q16.txt','r')
print(f.closed)
f.close()
print(f.closed)
# agar hum print mai direct likh dateh hai ki closed to bo bolta hai ki file open hai
# but second time mai hum close karke print mai closed karte hai to bolta hai hmm close hai
