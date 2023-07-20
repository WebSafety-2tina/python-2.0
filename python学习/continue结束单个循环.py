# continue 结束循环语句中的单个循环  continue 语句是一个删除的效果，他的存在是为了删除满足循环条件下的某些不需要的成分
for letter in 'Python':  # 第一个实例
    if letter == 'h':
        continue
    print('当前字母 :', letter)

var = 10  # 第二个实例
while var > 0:
    var = var - 1
    if var == 5:
        continue
    print('当前变量值 :', var)
print("Good bye!")
