def func(n):
    ls = list(map(int, str(n)))
    return sum(ls)
 
count = 0
n = eval(input('输入一个正整数：'))
print(f'{n}各位数之和为：{func(n)}')
