import sys

N = int(sys.stdin.readline())
NArr = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
MArr = list(map(int, sys.stdin.readline().split()))

dic = {}

for i in range(N):
    if dic.get(NArr[i]) == None:
        dic[NArr[i]] = 1
    else:
        dic[NArr[i]]+=1

for i in range(M):
    if dic.get(MArr[i]) == None:
        print("0", end=" ")
    else:
        print(dic[MArr[i]], end=" ")

