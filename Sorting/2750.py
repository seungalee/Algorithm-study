import sys

sys.stdin = open('input.txt', 'r')

arr = []
numOfLines = int(sys.stdin.readline())
i=0
for x in range(numOfLines):
    x = int(sys.stdin.readline())
    arr.append(x)

arr.sort()

for y in arr:
    print(y)