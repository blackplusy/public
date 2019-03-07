#coding=utf-8
#设置字符集
#中文 GBK2312
#1.直接输出
print('hello world!')
print(1000)
#2.变量输出
a=100
print(a)
a='simida'
print(a)
a=100
b=200
print(a+b)
#3.函数输出
#abs()   绝对值
print(abs(-10))
#格式化输出
# %s  	格式化输出字符串内容
# %d 	格式化输出数字类型内容
name='heygor'
print('your name is %s' % name )
age=100
print('your age is %d' % age)
name='python'
b=1
print('%s is no.%d'%(name,b))