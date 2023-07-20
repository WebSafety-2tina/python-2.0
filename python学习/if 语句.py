nl = input("你好请问您的年龄是：")
age = int(nl)
if age > 18:
    print("你好，满18可以喝酒")
elif age <= 18:
    print("你好，未满18不可以喝酒")
else:
    print("想蒙混过关不行")
