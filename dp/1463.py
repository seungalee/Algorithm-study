# 인터넷 풀이 참고, DP를 기록할 방법에 대해 고민...
# https://bio-info.tistory.com/159

import sys

N = int(sys.stdin.readline())
num=0
arr=[0]*(N+1)
for i in range(2, N+1):
    arr[i] = arr[i-1]+1
    if i%3==0:
        arr[i] = min(arr[i//3]+1, arr[i])
    if i%2==0:
        arr[i] = min(arr[i//2]+1, arr[i])

print(arr[N])
    