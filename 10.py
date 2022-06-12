str1 = 'www.hufe.edu.cn'
str2 = ''
str2 = str1[:3]
print(str2)
str2 = str1[-3:]
print(str2)
str2 = str1
print(str2)
str2 = str1[6:]
print(str2)
str2 = str1[2]
print(str2)
print(len(str1))
str2 = str1.replace(".", "-")
print(str2)
str2 = str1.split(".")
for str in str2:
    print(str)