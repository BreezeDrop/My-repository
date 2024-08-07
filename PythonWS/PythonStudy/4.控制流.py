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

# region break\continue\else



# endregion
