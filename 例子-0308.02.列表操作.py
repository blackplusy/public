#coding=utf-8
l=[1,2,3]
l=[1,'o8ma',2,'ladeng']
l=[1,2,[3,4]]


#列表的访问
#直接访问

l=[1,2,3,4,5]
print(l)

#遍历访问
for i in l:
    print(i)

if 3 in l:
    print('3 is here!')

#列表的索引和切片
l1=[2,3,5,7,9]

print(l1[3])

print(l1[-2])

#print(l1[8])

print(l1[2:4])

print(l1[1:])

print(l1[:-3])

#列表的拼接
l1=[1,2,3]
l2=[4,5]
print(l1+l2)


#列表的更新
l=[1,2,3,4,5]
print(l[2])
l[2]='heygor'
print(l)
l[-1]='ladeng'
print(l)




#列表的删除
l=[1,2,3,4,5]
print(l)
del l[-2]
print(l)
del l[2]
print(l)







