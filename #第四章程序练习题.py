#第四章程序练习题
"""
#4.1猜数游戏
from random import *
a=randint(0,100)
b=eval(input("请输入你猜的数"))
c=1
while a!=b:
    if b>a:
        print("你输入的数太大了！")
        c+=1
    else:
        print("你输入的数太小了！")
        c+=1
    b=eval(input("请输入你猜的数"))
print("你终于猜对了！这个数是{},你一共猜了{}次".format(a,c))
"""
"""
#4.2统计不同字符个数
s=input("请输入文本")
letter=0
digits=0
space=0
others=0
for i in s:
    if i.isalpha():
        letter+=1
    elif i.isspace():
        space+=1
    elif i.isdigit():
        digits+=1
    else:others+=1
print("字母次数是{},空格次数是{},数字次数是{},其他次数是{}".format(letter,space,digits,others))
"""
"""
#4.3最大公约数计算
from math import *
a,b=eval(input()),eval(input())
c=gcd(a,b)
print("这两个数的最大公约数是{}".format(c))
#辗转相除法a和b的最大公约数是a和b的余数和b的最大公约数
c=a%b
while c!=0:
    c=a%b
    a=b
    b=c
print("他们的最大公约数是{}".format(a))
"""
#4.6羊门车问题
from random import *
cnt=0
for i in range(10000):
  a=randint(1,3)
  b=randint(1,3)
  if a==b:
      cnt+=1
print("不换猜对车的概率是{:.2f}".format(cnt/10000))
cnt=0
for i in range(10000):
    a=randint(1,3)
    b=randint(1,3)
    if a==b:
      cnt+=1
    else:
        while True:
            q=randint(1,3)
            if q!=a and q!=b:
                break
        b=choice([a,q])
        if a==b:
            cnt+=1
           
print("换猜对车的概率是{:.2f}".format(cnt/10000))
    
  
    