#coding=utf-8
tup=(1,)
print(tup)
print(type(tup))



tup=(1,2,3,4)
for i in tup:
    print(i)



tup=(1,2,3,4)
del tup
#print(tup)


#元组的索引和切片
tup=(1,2,3,4)
print(tup[0])
print(tup[-3])
print(tup[2:])
print(tup[:-2])
print(tup[2:3])


#元组的补充
a=(2,3,1,1,1,1)
print(len(a))
print(max(a))
print(min(a))
print(a.index(1))
print(a.count(1))
