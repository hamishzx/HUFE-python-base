l1 = [11,22,33,55]
l2 = [22,33,44,66,77]

a = []
for i1 in l1:
    for i2 in l2:
        if i1 == i2:
            a.append(i1)
print(a)

a = []
for i1 in l1:
   if i1 not in l2:
        a.append(i1)
print(a)

a = []
a = l1 + l2
a = list(set(a))
a.sort()
print(a)