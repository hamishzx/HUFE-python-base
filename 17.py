number = int(input('请输入一个数：'))
list1 = list(str(number))
list1.reverse()
a = int(list1[0])
if (a == 3 and number % 7 == 0):
    print("满足被7整除且最后一位数字为3")
else:
    print("不满足被7整除且最后一位数字为3")