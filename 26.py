import random

n = random.randint(100, 1000)
num = 1
sum = 0
while num < n+1:
    if num % 2 == 0:
        sum += num
    num += 1
print(sum)
