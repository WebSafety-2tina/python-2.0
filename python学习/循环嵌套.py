i =int(input("请输入一个数字:"))
while (i < 100):
    j = 2
    while (j <= (i / j)):
        if not (i % j):
            break
        j = j + 1
    if (j > i / j):print (i, " 是素数")
    i=i+1
print("Good bye!")