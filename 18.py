password = input("输入密码: ")
error = "密码强度过低"
raiseerr = False
if len(password) < 7:
    error += "，长度不足8位"
    raiseerr = True
if password.islower():
    error += "，未包含英文大写"
    raiseerr = True
if password.isupper():
    error += "，未包含英文小写"
    raiseerr = True
if password.isdigit():
    error += "，未包含英文字母"
    raiseerr = True
if password.isalpha():
    error += "，未包含数字"
    raiseerr = True

if raiseerr:
    print(error)
else:
    print("密码OK")