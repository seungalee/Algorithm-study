import sys
from heapq import heappush, heappop


heap = []

N = int(input())
for i in range(N):
    num = int(sys.stdin.readline())
    if(num>0):
        heappush(heap, (-num, num))
    else:
        if len(heap)==0:
            print(0)
        else:
            maxnum = heappop(heap)
            print(maxnum[1])