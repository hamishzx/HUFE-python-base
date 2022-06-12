i=1
sum=0
for num in range(1, 100):
    if num % 3 ==0:
        sum += num
while i<=100:
    if i % 5 == 0:
        sum += i
    i += 1
print(sum)