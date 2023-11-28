# a simple parser for python. use get_number() and get_word() to read
def parser():
    while 1:
        data = list(input().split('\n'))
        for number in data:
            if len(number) > 0:
                yield(number)   

input_parser = parser()

def get_word():
    global input_parser
    return next(input_parser)

def get_number():
    data = get_word()
    try:
        return int(data)
    except ValueError:
        return float(data)

# numpy and scipy are available for use
import numpy
import scipy

a = get_number()
b = []
arr = []
res = []
res2 = []
dump = []

# for i in range(get_number()):
#     x, y, z = get_word().split()
#     a.append(x)
#     b.append(z)
    
for i in range(a):
    arr = get_word().split()
    dump.append(arr)

for i in range(a):
    if dump[i][1] == "->":
        res.append(dump[i][0])
        res2.append(dump[i][2])

for i in range(a):
    if dump[i][1] == "??":
        if (dump[i][0]) not in res:
            res.append(dump[i][0])
        # res.append(dump[i][2])
    
# print(res)
# print(res2)

# print(res2.index("dev"))

for i in range(len(res2)):
    if res2[i] in res:
        res.pop(res.index(res2[i]))
        
        
result = sorted(res)
last = ""

for i in range(len(res)):
    if last != result[i]:
        print(result[i])
    last = result[i]
