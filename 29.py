score = [68,87,92,100,76,88,54,89,76,61]
print(score[-5:])
print(score[:6])
score.insert(2, 59)
num = 76
print(score.count(num))
score.sort(reverse=True)
print(score[0])
score.sort()
print(score[0])
print(score.index(100))
print(sum(score) / len(score))