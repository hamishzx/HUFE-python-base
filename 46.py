def func(str):
    upperct = 0
    lowerct = 0
    for i in str:
        if i.islower():
            lowerct += 1
        elif i.isupper():
            upperct += 1
    return (upperct, lowerct)
print(func(input("请输⼊⼀串字符串：")))