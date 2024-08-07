# 申明字符编码
# -*- coding:encoding -*-


# region 代码折叠

# endregion

# region math & string

17/3 # float division
17//3 # floor division 
5 ** 2 # power

'doesn\'t' # 转义
print('doesn\'t') # print不加引号

#r转义
print('C:\some\name')
print(r'C:\some\name')

print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""") # 三引号换行

# 拼接
'py''thon'
text = ('Put several strings within parentheses '
        'to have them joined together.')
text

# 索引
word = 'Python'
word[0]  # character in position 0
word[5]  # character in position 5

# 切片
word[0:2]  # characters from position 0 (included) to 2 (excluded)

# 字符串不能修改
word[0] = 'J'

# 字符串长度
s = 'supercalifragilisticexpialidocious'
len(s)

# endregion

# region list


squares = [1, 4, 9, 16, 25]
squares
squares + [36, 49, 64, 81, 100]

# 列表内容可以更改
cubes = [1, 8, 27, 65, 125]  # something's wrong here
4 ** 3  # the cube of 4 is 64, not 65!
cubes[3] = 64  # replace the wrong value
cubes

# 嵌套列表
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
x
x[0][1]

# Fibonacci series:
# the sum of two elements defines the next

a,b = 0,1
while a < 10:
    print(a)
    a,b=b,a+b

a,b = 0,1
while a < 1000:
    print(a,end=',')
    a,b=b,a+b


# endregion

# region control flaw

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

a = list[range(5,10)]
a
# endregion