numbers = list(range(10))
sum = 0
func = lambda x: x ** 2
for num in numbers:
   sum += func(num)
print(sum)