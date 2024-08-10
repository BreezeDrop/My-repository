# region 默认值参数

def fib(n):    # write Fibonacci series up to n
    """Print a Fibonacci series up to n.""" # 函数文档
    """This is a test"""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

# Now call the function we just defined:
fib(2000)

fib.__doc__

fib

f = fib
f(100)

print(fib(0)) # 没有定义return返回none

def fib2(n):  # return Fibonacci series up to n
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)    # see below
        a, b = b, a+b
    return result

f100 = fib2(100)    # call it
f100                # write the result

# 为参数指定默认值
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'): # in的用法
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response') # raise 手动触发异常
        print(reminder)

ask_ok('Do you really want to quit?')  # 只给出必选实参
ask_ok('OK to overwrite the file?', 2) # 给出一个可选实参
ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!') # 给出所有实参

i = 6
def f(arg=i):
    print(arg)

i = 7 # 函数定义不会随着全局变量而改变
f()

# 默认值只计算一次，默认值为列表、字典、类实例时，会变化
def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))

def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))

# endregion

# region 关键值参数

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

# 可选调用方式
parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword

# 无效调用方式
parrot()                     # required argument missing
parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument
parrot(110, voltage=220)     # duplicate value for the same argument
parrot(actor='John Cleese')  # unknown keyword argument
# 关键字参数的顺序不重要

# *name为元组，**name为字典，*name必须在**name之前
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

# endregion

# region
# / * 在函数参数中的作用，/仅位置参数，*关键字参数
def standard_arg(arg):
    print(arg)

def pos_only_arg(arg, /):
    print(arg)

def kwd_only_arg(*, arg):
    print(arg)

def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)

standard_arg(2)
standard_arg(2)

pos_only_arg(1)
pos_only_arg(arg=1)

kwd_only_arg(3)
kwd_only_arg(arg=3)

combined_example(1, 2, 3)
combined_example(1, 2, kwd_only=3)

def foo(name, **kwds):
    return 'name' in kwds
foo(1, **{'name': 2})

def foo(name, /, **kwds):
    return 'name' in kwds
foo(1, **{'name': 2})

# 任意实参列表
def concat(*args, sep="/"):
    return sep.join(args)

concat("earth", "mars", "venus")
concat("earth", "mars", "venus", sep=".")

# 解包实参列表
list(range(3, 6)) 
args = [3, 6]
list(range(args))
list(range(*args)) # *解包实参列表

def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")

d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d) # **解包字典

# Lambda表达式