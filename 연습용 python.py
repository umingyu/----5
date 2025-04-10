i,e,r=0,0,""

for i in range(2,10):
    r=r+(" # %d단 #"%i)

print(r)

for i in range(1, 10) : 
    r=""
    for e in range(2,10):
        r=r+str("%2dx%2d=%2d"%(e, i, e*i))
    print(r)