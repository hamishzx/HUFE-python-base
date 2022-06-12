i = 1
j = 1
s = 0
for i in range(1, 10):
    for j in range(1, (i+1)):
        s = i * j
        print("%d * %d = %s" % (i, j, s), end = "\t")
        j += 1
    print(" "*30)
    i+=1