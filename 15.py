num = int(input("输入年龄："))
if (num < 0 or num > 150):
    print("这不是人！")
elif (num > 18):
    print("成年")
elif (num < 18):
    print("未成年")