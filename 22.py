count = int(input("几个整数？"))
i = 1
sum = 0
while i < count+1:
    sum += int(input("整数{0}: ".format(str(i))))
    i += 1
print(sum)