##break跳出整个循环 
for letter in 'Python':  # 第一个实例
    if letter == 'h':
        break
    print('当前字母 :', letter)

var = 10  # 第二个实例
while var > 0:
    print('当前变量值 :', var)
    var = var - 1
    if var == 5:  # 当变量 var 等于 5 时退出循环
        break

print("Good bye!")
