##字典是另一种可变容器模型，且可存储任意类型对象。
##字典的每个键值 key:value 对用冒号 : 分割，
##每个键值对之间用逗号 , 分割，整个字典包括在花括号 {} 中
#d = {key1 : value1, key2 : value2 }
##注意：dict 作为 Python 的关键字和内置函数，变量名不建议命名为 dict。

tinydict={'a':1,'b':2,'b':3}
print(tinydict['b'])
##>>>3
##键一般是唯一的，如果重复最后的一个键值对会替换前面的，值不需要唯一
zhangchulan={'Name':'zcl','age':'19','class':2}
print("名字为",zhangchulan['Name'])
print("年龄为",zhangchulan['age'])
print("班级为",zhangchulan['class'])
##修改字典
zhangchulan2={'name':'wanghaitao','age':19,'class':'first'}
zhangchulan2['age']=20
zhangchulan2['谁']='wo'
print("添加结果为:",zhangchulan2['age'])
print("新增结果为:",zhangchulan2['谁'])
##删除字典元素
zhangchulan3={'name':'wanghaitao','age':19,'class':'first'}
del zhangchulan3['class']
print('删除字典元素为:',zhangchulan3)
##删除字典所有条目
zhangchulan4={'name':'wanghaitao','age':19,'class':'first'}
zhangchulan.clear()
print('删除所有条目',zhangchulan4)
##删除整个字典
zhangchulan5={'name':'wanghaitao','age':19,'class':'first'}
del zhangchulan5
print('删除整个字典',zhangchulan5)
##字典的特性
##字典值可以没有限制地取任何 python 对象，既可以是标准的对象，也可以是用户定义的，但键不行。
##两个重要的点需要记住：
##1）不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住
tinydict = {'Name': 'Runoob', 'Age': 7, 'Name': 'Manni'} 
print("tinydict['Name']: ", tinydict['Name'])
##输出结果为
## >>>tinydict['Name']:  Manni
##2）键必须不可变，所以可以用数字，字符串或元组充当，所以用列表就不行，
tinydict = {['Name']: 'Zara', 'Age': 7} 
print("tinydict['Name']: ", tinydict['Name'])
##输出结果为
##>>>Traceback (most recent call last):
##  File "test.py", line 3, in <module>
##    tinydict = {['Name']: 'Zara', 'Age': 7} 
##TypeError: unhashable type: 'list'
