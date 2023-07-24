##序列是Python中遍历的数据结构。序列中的每个元素都分配一个数字——它的位置，或者索引，第一个索引是0，第二个索引是1，如此推。
##Python 有 6 个序列的内置类型，但最常见的是列表和元组。
##序列都可以进行的操作包括索引、切片、添加、乘、检查成员。
##另外，Python已经内置了确定序列的长度以及确定最大和最小元素的方法。
##列表是最常用的Python数据类型，它可以作为方括号内的逗号分隔值出现。
##列表中的数据项不需要具有相同的类型
list1=['physics','chemistry',1997,2000]
list2=[1,2,3,4,5]
list3=['a','b','c','d']
print("list1[0]:",list1[0])
print("list2[1:5]:",list2[1:5])
##添加列表中的元素
list=[]
list.append('Google')
list.append('Runoob')
print(list)
##删除列表中的元素
list=[1,2,3,4,5,6,7]
del list[2]
print('删除结果为',list)




##Python 表达式	结果	描述
##L[2]	'Taobao'	读取列表中第三个元素
##L[-2]	'Runoob'	读取列表中倒数第二个元素
##L[1:]	['Runoob', 'Taobao']	从第二个元素开始截取列表