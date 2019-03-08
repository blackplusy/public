#coding=utf-8
dic={'name':'gaga','QQ':110}
dic2={'age':19}

print(dic)
print(dic['name'])
print(dic['QQ'])

dic={'name':'gaga','QQ':110}
print(dic)
dic['name']='simida'
print(dic)
dic['QQ']=500
print(dic)

dic={'name':'gaga','QQ':110}
print(dic)
del dic['name']
print(dic)
del dic
#print(dic)


dic={'name':'gaga','QQ':110}
dic.clear()
print(dic)


#keys
dic={'name':'gaga','QQ':110}
print(dic.keys())
for i in dic.keys():
    print(i)

#values
dic={'name':'gaga','QQ':110}
print(dic.values())
for i in dic.values():
    print(i)


#items
dic={'name':'gaga','QQ':110}
print(dic.items())
for i,j in dic.items():
    print(str(i)+':'+str(j))


