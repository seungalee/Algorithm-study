import sys
from collections import deque
#시간 2768ms

M, N = map(int, sys.stdin.readline().split())

graph = [[0]*M for _ in range(N)]

for i in range(N):
    arr = list(map(int, sys.stdin.readline().split()))
    for j in range(M):
        graph[i][j] = arr[j]


visit = deque()
for i in range(N):
    for j in range(M):
        if graph[i][j]==1:
            visit.append((j, i, 0))

answer = 0
dx = [1, -1, 0 ,0]
dy = [0, 0, 1, -1]
while visit:
    node = visit.popleft()
    for a in range(4):
        newx = node[0]+dx[a]
        newy = node[1]+dy[a]
        answer = node[2]
        if 0<=newx<=M-1 and 0<=newy<=N-1:
            if graph[newy][newx]==0:
                visit.append((newx, newy, answer+1))
                graph[newy][newx]=-1

breakToggle = False
for i in range(N):
    for j in range(M):
        if graph[i][j]==0:
            answer = -1
            breakToggle = True
            break
    if breakToggle ==True:
        break

print(answer)
    