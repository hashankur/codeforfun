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
        return float(data)
    except ValueError:
        return int(data)

# numpy and scipy are available for use
import numpy
import scipy

def shiftalgo(plaintext,n):
    ans = ""
    # iterate over the given text
    for i in range(len(plaintext)):
        ch = plaintext[i]
        
        if ch==" ":
            ans+=" "
        elif (not ch.isalpha()):
            ans += ch
        elif (ch.isupper()):
            ans += chr((ord(ch) + n-65) % 26 + 65)
        else:
            ans += chr((ord(ch) + n-97) % 26 + 97)
    
    return ans

loops = get_word()

# print(loops)

for loop in range(int(loops)):
    n = get_word()
    plaintext = get_word()
    
    has_the = False
    
    for word in plaintext.split():
        if "the" == word:
            has_the = True
    
    if has_the:
        print(shiftalgo(plaintext,-abs(int(n))))
    else:
        print(shiftalgo(plaintext,int(n)))




# plaintext = input()
# n = 14
