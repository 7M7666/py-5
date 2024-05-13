#random库
#随机生成100内的十个整数
from random import *
for i in range(10):
    print(randint(0,100))
#随机选取0到100内的奇数
a=randrange(1,100,2)
print("奇数是{}".format(a))
#从字符串“abcdefghjidwdn”随机选取4个字符
s="asdfghjkl"
a=choice(s)
print(a)
#随机选取列表【】中的一个字符串
s=["sdsa","sjnda","sjd"]
a=choice(s)
print(a)