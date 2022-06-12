def func(n):
    for i in range(1, n):
        if i % 7 == 0 and i % 5 != 0:
            print(i)
 
x = eval(input("请输入一个整数："))
func(x)