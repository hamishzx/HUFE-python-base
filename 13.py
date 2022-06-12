import random 
n=int(input("请输入总人数: "))
strMix = ""
stuList = [] 
i=0
count = 1 
while i<n:
    stuList.append(input("请输入第"+ str(count)+"个同学的姓名:")) 
    i+=1
    count += 1 
for stu in stuList: 
    strMix += stu[random.randint(0,len(stu)-1)]
print(strMix)