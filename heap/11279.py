#heapq 사용
import sys
from heapq import heappush, heappop

#heapq: 최소 힙 구현한 라이브러리

heap = []
nums = []

N = int(input())
for i in range(N):
    nums = [input() for _ in range(N)]

for num in nums:
    if(num>0):
        heappush(heap, (-num, num))
    else:
        if len(heap)==0:
            print(0)
        else:
            print(heappop(heap))
