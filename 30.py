import random

english = [random.randint(40, 100) for i in range(5)]
english.sort(reverse=True)
print(english)