## 列表是可变的，长度大小可变，可随意增删改查元素
##存储空间略大于元组，性能稍弱于元组，不能作为字典的键 
##元组是不可变的，长度大小固定

##创建一个元组 访问一个元组
tup1=('physics','chemistry',1997,2000)
tup2=(1,2,3,4,5,6,7)
print('tup1[2]',tup1[2])
print('tup2[4]',tup2[4])
##修改一个元组时
##元组中的元素值是不允许修改的，但我们可以对元组进行连接组合
tup1=('physics','chemistry',1997,2000)
tup2=(1,2,3,4,5,6,7)
tup3=tup1+tup2
print(tup3)
##删除元组
tup=('physics','chemistry',1997,2000)
tup2=(1,2,3,4,5,6,7)
del tup2
print(tup,tup2)