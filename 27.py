import random

numbers = [random.randint(1, 100) for i in range(100)]
max = numbers[0]
for i in numbers:
    if i > max:
        max = i
print(max)