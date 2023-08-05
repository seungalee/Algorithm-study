import sys
sys.stdin = open('input.txt', 'r')

leastNum = 0
numPp = int(sys.stdin.readline())

timeList = list(map(int, sys.stdin.readline().split()))

timeList.sort()

for index in range(len(timeList)):
    leastNum += timeList[index]*(len(timeList)-index)

print(leastNum)
