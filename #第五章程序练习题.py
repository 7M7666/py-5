#第五章程序练习题
#5.2奇数
def isodd(n):
    return n%2 in [1]
print(isodd(2))
#5.3 isnum
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
    try:
        int(s)
        return True
    except ValueError:
        pass
    try:
        complex(s)
        return True
    except ValueError:
        pass
    return False
#5.4 multi
def multi(*n):
    a=1
    for i in n:
        a*=i
    return a
print(multi(5,6,7,8))
#5.5 isprime
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
#5.6
from datetime import datetime
# 假设的生日
birthday = datetime(1990, 1, 1)
# 10种不同的日期格式
formats = [
    "%Y-%m-%d",      # 年-月-日格式
    "%m/%d/%Y",      # 月/日/年格式
    "%d/%m/%Y",      # 日/月/年格式
    "%Y%m%d",        # 年月日格式
    "%m-%d",         # 月日格式
    "%d-%m",         # 日月格式
    "%A, %B %d, %Y", # 星期几, 月份 日, 年
    "%B %d, %Y",     # 月份 日, 年
    "%A, %B %d, %Y", # 完整英文日期
    "%a, %b %d, %Y"  # 简写英文日期
]
formatteddates = [birthday.strftime(format) for format in formats]
print(formatteddates)
#5.7汉诺塔
def hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move 盘子1 from {source} to {target}")
    else:
        hanoi(n-1, source, auxiliary, target)#让上面的盘子全去辅助盘子
        print(f"Move 盘子{n} from {source} to {target}")#最大的盘子移到target
        hanoi(n-1, auxiliary, target, source)#辅助盘子去target
hanoi(3, 'A', 'C', 'B')





