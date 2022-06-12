def sum(a, n):
    sn = 0
    sum = 0
    for i in range(1, n+1):
        sn = sn * 10 + a
        sum += sn
    return sum
a = eval(input('请输入a：'))
n = eval(input('请输入n：'))
result = sum(a, n)
print(result)