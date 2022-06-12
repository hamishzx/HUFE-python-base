import random
lst = [random.randint(0, 20) for i in range(20)]
lst = list(set(lst))
print(lst)