#斐波那契
def f(n):
    fei = [0, 1]
    [fei.append(fei[-1] + fei[-2]) for i in range(n-2)]
    return fei
s = f(8)
print(s[7])
