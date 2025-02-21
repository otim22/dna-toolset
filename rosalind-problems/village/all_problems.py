# Question 1
# import this
from collections import Counter

# Question 2
# ====== Variables an some Arithmetic
a = 3
b = 5 
print(f'{a}^2 + {b}^2 = {a**2 + b**2}')

# Loops
startPos = 4309
endPos = 8902
result = 0

for x in range(startPos, endPos + 1):
    if x % 2 != 0:
        result += x
# method 2
# result = sum(
#     [x for x in range(startPos, endPos + 1) if x % 2 != 0]
# )

# Working with files
outputFile = []

with open('village/input.txt', 'r') as f:
    outputFile = [line for pos, line in enumerate(
        f.readlines()) if pos % 2 != 0]

with open('village/output.txt', 'w') as f:
    f.write(''.join([line for line in outputFile]))
    

# Dictionaries
txtStr = "We tried list and we tried dicts also we tried Zen"

# Method 1
# wordCountDict = {}
# for word in txtStr.split(' '):
#     if word in wordCountDict:
#         wordCountDict[word] += 1
#     else:
#         wordCountDict[word] = 1

# Method 2
wordCountDict = Counter(txtStr.split(' '))

for key, value in wordCountDict.items():
    print(key, value)
