# region if、for、range

x = int(input("Please enter an integer: "))
if x < 0:
    x = 0
    print("Negetive changed to zero")
elif x == 0:
    print("Zero")
elif x == 1:
    print("Single") # 可以有多个elif
else:
    print("More")

words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w,len(w))

for i in range(5):
    print(i,end=',')

range(5,10)
list(range(5,10)) # list()函数对range转换成列表
list(range(1,10,3))
a = ['Mary','had','a','little','lamb']
for i in range(len(a)):
    print(i, a[i])

sum(range(4))

# endregion

# region break\continue\else\pass

for n in range(2, 10):
    for x in range(2,n):
        if n % x == 0:
            print(n,'equals',x,'*',n//x)
            break
        else: # else从属于if
            # loop fell through without finding a factor
            print(n,'is a prime number')


10 // 7 # 整除

# try的用法
try:
    # 可能会引发异常的代码
except ExceptionType:
    # 发生异常时执行的代码
else:
    # 如果没有发生异常，执行的代码（可选）
finally:
    # 无论是否发生异常，都会执行的代码（可选）

try:
    # 尝试将用户输入转换为整数
    num = int(input("请输入一个整数："))
    print(f"你输入的整数是: {num}")
except ValueError:
    # 当用户输入非整数时，捕获并处理 ValueError 异常
    print("这不是一个有效的整数！")
else:
    # 如果没有发生异常，执行以下代码
    print("感谢你输入了一个整数。")
finally:
    # 无论是否发生异常，都会执行的代码
    print("程序执行完毕。")

for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found an odd number", num)

# pass 不执行任何动作
class MyEmptyClass: # 最小的类
    pass
# endregion
