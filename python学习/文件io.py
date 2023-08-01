##最简单的输出方法是用print语句，你可以给它传递零个或多个用逗号隔开的表达式。此函数把你传递的表达式转换成一个字符串表达式，并将结果写到标准输出如下：
print("Python 是一个非常棒的语言，不是吗？")
##Python提供了两个内置函数从标准输入读入一行文本，默认的标准输入是键盘。如下：
#raw_input
#input
#raw_input函数
#raw_input([prompt]) 函数从标准输入读取一个行，并返回一个字符串（去掉结尾的换行符）：
str=input("请输入：")
print("你输入的内容是: ",str)
##input函数
##input([prompt]) 函数和 raw_input([prompt]) 函数基本类似，但是 input 可以接收一个Python表达式作为输入，并将运算结果返回。
str=input("请输入：")
print("你输入的内容是: ",str)