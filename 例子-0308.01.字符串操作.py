#coding=utf-8
s='www.baidu.com'
print(s[0])
print(s[2])
print(s[-4])



#字符串的切片
print(s[1:3])
print(s[3:])
print(s[:-4])
print(s[4:-4])

#字符串的拼接
a='hello   '
b='world'
print(a+b)

a='100'
b='999'
print(a+b)

#遍历
s='baidu.com'
for i in s:
    print(i)

#去空格 strip
#   lstrip    去掉左边空格
#   rstrip    去掉右边空格

a='   simida   '
print(a)
print(a.strip())
print(a.lstrip())
print(a.rstrip())

#计算长度
#len()
a='python '
print(len(a))

#引号操作
print('**********************')
print('heygor')
print("simida")
#print('i'm your papa')
print("i'm your papa")
print('i"m your mm')

#三引号
#注释，引号中内容不会影响代码执行
#换行输出

'''
我是东北的
'''


#print('转账请嗯1')
#print('退卡请嗯2')
print('''
转账请嗯1
退卡请嗯2

''')











