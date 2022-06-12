def func(ls):
    _ls = filter(lambda n: n > 0, ls)
    return sum(_ls)


ls = eval(input('请按照列表格式输入列表元素：'))
print(f'该列表中所有正数之和为：{func(ls)}')