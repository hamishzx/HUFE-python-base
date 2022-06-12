from random import randrange


count = 0
randrange = [0, 2, 3, 4]
for i in randrange:
    for j in randrange:
        for k in randrange:
            if i != j and j != k and k != i:
                count +=1

print("可生成%d个无重复数字的三位数" % count)