scores = {"Zhang San": [45,60,80], "Li Si": [78,80,90], "Wang Wu": [40,59,60]}
averScores = {key:sum(scores[key])/len(scores.values()) for key in scores}
print("平均分字典: {}".format(averScores))
failMath = []
failPython = []
failEnglish = []
for name,grades in scores.items():
    for i in range(3):
        if grades[i] < 60:
            if i == 0:
                failMath.append(name)
            elif i == 1:
                failPython.append(name)
            elif i == 2:
                failEnglish.append(name)
print("数学不及格: {}".format(",".join(failMath) if len(failMath) > 0 else "无"))
print("Python不及格: {}".format(",".join(failPython) if len(failPython) > 0 else "无"))
print("英语不及格: {}".format(",".join(failEnglish) if len(failEnglish) > 0 else "无"))
print("按照数学分数由低到高排序，输出信息")
scoresSorted = sorted(scores.items(),key=lambda x:x[1][0]) 
for name, grade in scoresSorted:
    print(name,grade)