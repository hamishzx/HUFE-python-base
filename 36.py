scores = {"Zhang San": 45, "Li Si": 78, "Wang Wu": 40, "Zhou Liu": 96, "Zhao Qi": 65, "Sun Ba": 90, "Zheng Jiu": 78, "Wu Shi": 99, "Dong Shiyi": 60}
max = 0
min = 100
avrg = 0
namelst = []
for grade in scores.values():
    if grade > max:
        max = grade
    if grade < min:
        min = grade
    avrg += grade
avrg /= len(scores)
print("最高分是{0}，最低分是{1}，平均分是{2}".format(max, min, avrg))
for name, score in scores.items():
    if score == max:
        namelst.append(name)
print("{0}获得最高分".format(namelst))
