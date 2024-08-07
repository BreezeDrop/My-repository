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