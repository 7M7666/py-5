#第三章程序练习题
#3.1
#假设我的体重是60kg
a=60
for i in range(10):
    a+=0.5
print("3.1:在地球上的体重是{}\n在月球上的体重是{}".format(a,a*0.165))    
#3.2
a=1
#持续学习365天：
for i in range(365):
    if i>3:
        a=(1+0.01)*a
print("3.2:连续学习365天是{:.2f}".format(a))
#3.3
#持续学习10天：
a=1 
for i in range(365):
    if i%11==0:
        continue
    else:
        if 4<=(i%10)<=7:
            a+=a*0.01
        else:
            a+=a*0.01 if i>7 else 0
print("3.2:连续学习10天是{:.2f}".format(a))
#3.4
# 回文判断数
def b(n):
    return str(n)==str(n)[::-1]
a=12321
print(b(a))


        
              