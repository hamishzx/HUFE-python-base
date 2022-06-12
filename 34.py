student = [['001','李梅',19],['002','韩磊磊',20],['003','张亮',18]]
student.append(['004','王大锤',20])
student.append(['006','刘大刀',18])
student.insert(4, ['005','赵钱孙',20])

for stu in student:
    if "004" in stu:
        print(stu)

for stu in student:
    print(stu[1])

for stu in student:
    if stu[2] > 19:
        print(stu)

s = "I want to study Python perfectly"
s = tuple(s)


for i in range(len(s)):
    print(s[i], end=' ')
    if (i+1) % 5 == 0:
        print("")
dict = {"k1":"v1","k2":"v2","k3":"v3"}
for key in dict:
    print(key)
for value in dict.values():
    print(value)
for item in dict.items():
    print(item)
dict.update({'k4':'v4'})
print(dict)
dict.pop("k1")
print(dict)