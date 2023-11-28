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
import string

nums = get_word().split()

words = []
lines = []
count = 0
count2 = 0

for i in range(int(nums[0])):
    temp = get_word().split()
    words.append(temp)
    words[i].insert(0, " ")
    
for i in range(int(nums[1])):
    temp = get_word().split().pop(-1)
    lines.append(temp)
    

    
    # print(lines[i])

# for j in range(len(lines)):
#     try:
#         for i in range(len(lines)):
#             if lines[i].lower() in words[i] and lines[i+1].lower() in words[i]:
#                 # print(lines[0], lines[1])
#                 if (words[i][0] == ' '):
#                     words[i][0] = string.ascii_uppercase[count]
#                     count+=1
#                 print(words[i][0]*2, end="")
#                 lines.pop(0)
#                 lines.pop(1)
                
#             else:
#                 print("XX", end="")
#             # print(i, j)
#             count2+=1
#     except IndexError:
#         break

# for i in range(0, len(lines)+1, 2):
#     # print(lines[i])
#     for j in range(len(words)):
#         try:
#             if lines[i].lower() in words[j] and lines[i+1].lower() in words[j]:
#                 # print(lines[i], lines[i+1])
#                 if (words[j][0] == ' '):
#                     words[j][0] = string.ascii_uppercase[count]
#                     count+=1
#                     print(j)
    
#                 print(words[j][0]*2, end="")
#                 lines.pop(0)
#                 lines.pop(1)
#         except IndexError:
#             break
# j = 0
# if lines[0].lower() in words[j] and lines[1].lower() in words[j]:
#     if (words[j][0] == ' '):
#         words[j][0] = string.ascii_uppercase[count]
#         count+=1
#         # print(j)
#     print(words[j][0]*2, end="")
#     lines.pop(0)
#     lines.pop(1)
j = 0
def exists(word):
    global j
    for i in range(len(words)):
        if word in words[i]:
            j = i
            # print(j)
            return True
 
    return False

try:
    for i in range(0, len(lines)-3):
        t1 = lines.pop(0).lower()
        t2 = lines.pop(0).lower()
        
        # print(i)
        if exists(t1) and exists(t2):
    
            
            if (words[j][0] == ' '):
                words[j][0] = string.ascii_uppercase[count]
                count+=1
                # print(j)
        
            print(words[j][0]*2, end="")
            continue
        print("XX", end="")
except:
    print("")

    
# print(arr[0][-1])
# print()
# print(exists("four"))
# print(words)
# print(lines)