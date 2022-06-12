number = input('请输入一个三位数：')
list1 = list(number)
list1.reverse()
a = int(list1[0])
b = int(list1[1])
c = int(list1[2])
re_number = a*100 + b*10 + c
print(re_number)