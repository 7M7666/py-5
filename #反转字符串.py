#反转字符串
def a(n):
    if n=="":
        return n
    else:
        return a(n[1:])+n[0]
s=a("qwertyuiop")
print(s)