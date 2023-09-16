import sys
from collections import deque
#메모리 초과, 인덱스 초과, 시간 초과 등 다양한 오류....
#메모리 초과 해결하기 위해 graph 사용해 횟수 표시하자
#시간 초과 해결하기 위해 deque 사용, 마찬가지로 graph 사용
#인덱스 초과 해결하기 위해 집어넣을 값이 100000 이하인지 확인하는 과정 거치기 - 왜 100000인가?
#100000 이하인지 확인하는 과정을 먼저 거쳐 인덱스 오류 안나도록 한다

N, K = map(int, sys.stdin.readline().split())

graph = [0 for _ in range(200000)]
visitNums = deque()
visitNums.append(N)
graph[N]=1

answer = 0

while True:
    node = visitNums.popleft()
    if node == K: 
        answer = graph[node]
        break
    if 0<=node+1<=100000 and graph[node+1]==0:
        visitNums.append(node+1)
        graph[node+1] = graph[node]+1
    if  0<=node-1<=100000 and graph[node-1]==0:
        visitNums.append(node-1)
        graph[node-1] = graph[node]+1
    if  0<=node*2<=100000 and graph[node*2]==0:
        visitNums.append(node*2)
        graph[node*2] = graph[node]+1

print(answer-1)