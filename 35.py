from re import I


myDict = {"辣条": 9.9, "快乐肥宅水": 99, "盲盒": 199, "毛拖": 299}
for item in myDict:
    print("{0}.........{1}".format(item, myDict[item]))
for item, price in myDict.items():
    if price > 100:
        print(item)