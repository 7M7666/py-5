#第六章程序练习题
#6.1随机密码生成
from random import *
import string
def password(n):
    a=string.digits+string.ascii_letters
    b = [choice(a) for i in range(n)]
    return ''.join(b)
passwords=[password(8) for i in range(10)]
print(passwords)
#6.2\6.3重复元素判定
def a(n):
    return len(n)!=len(set(n))
print(a("123321"))
#6.4文本字符分析
def n():
    q=input()
    w={}
    for i in  q:
        w[i]=w.get(i,0)+1
    iw=list(w.items())
    iw.sort(key=lambda x:x[1],reverse=True)
    return iw
s=n()
print(s)
#6.5生日悖论
from random import *
def q(n):
    a=0
    for i in range(n):
        s=[randint(1,365) for _ in range(23)]
        if len(s)!=len(set(s)):
          a+=1
    return a/n
print(q(10000))       


    