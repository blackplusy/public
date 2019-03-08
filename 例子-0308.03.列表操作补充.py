#coding=utf-8
#pop()弹出列表中的元素
#append()向列表中增加元素

l=[1,2,3,4]
print(l)
l.append(5)
print(l)
l.append(6)
l.append(7)
print(l)
l.pop()
print(l)
l.pop()
print(l)


#获取索引

l=[1,2,3,4,5,3,4,5]
print(l)
print(l.index(5))

l=['kobe','james','rose']
print(l.index('rose'))


#enumerate
for index,value in enumerate(l):
    print('索引是: '+str(index)+'值是：'+value)
    #print(type(index))    


#$tupe              判断数据类型
#数据类型转换       int() 转换为数字类型   str() 转换为字符类型   list() 转换为列表类型

print('******************')
l=[1,3,5,2,4,6]
print(l)
l.reverse()   #列表中元素倒序排列
print(l)
l=[1,3,5,2,4,6]
print(l)
l.sort()      #列表中元素进行排序
print(l)

l=[1,3,5,2,4,6]
print(l)
l.sort(reverse=True)
print(l)
