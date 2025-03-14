import sys
import collections

num, p = map(int, sys.stdin.readline().split())

stack = collections.deque()
stack.append(num)
idx = 0
while True:
    popnum = stack[-1]
    newnum = 0
    for letter in str(popnum):
        newnum += int(letter)**p
    
    if newnum in stack:
        idx = stack.index(newnum)
        break
    else:
        stack.append(newnum)

print(idx)
