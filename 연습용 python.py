i,e=0,0

for i in range(2,10,1):
    print("#%d단 입니다."%i)
    for e in range(1, 10, 1):
        print("%d * %d = %d" % (i, e, i * e))
