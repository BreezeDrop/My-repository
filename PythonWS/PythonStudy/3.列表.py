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