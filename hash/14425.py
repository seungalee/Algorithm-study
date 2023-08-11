import sys

NandM = list(map(int,sys.stdin.readline().split()))

N = NandM[0]
M = NandM[1]
dic = {}
i=0
j=0
answer = 0

while i<N:
    str = sys.stdin.readline().rstrip()
    dic[str] = True
    i+=1

while j<M:
    findingStr = sys.stdin.readline().rstrip()
    if findingStr in dic:
        answer+=1
    j+=1

print(answer)