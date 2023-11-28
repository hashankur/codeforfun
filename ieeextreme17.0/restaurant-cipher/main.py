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
import collections

def remove_special_characters(counter):
  new_counter = collections.Counter()
  for element, count in counter.items():
    if element.isalpha():
      new_counter[element] = count
  return new_counter

a = get_number()

for i in range(a):
    
    b = get_word()
    
    results = collections.Counter(b)
    print(remove_special_characters(results).most_common(1)[0][0].upper())
    # print(results)