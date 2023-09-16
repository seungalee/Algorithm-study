import sys
from collections import deque
from copy import deepcopy

##내가 헷갈리는 것!! deep copy, 배열 복사(특히 2차원)

N = int(sys.stdin.readline())

def bfs(graph, visited, x, y):
    
    visit = deque()
    visit.append((x, y))
    visited[y][x]=1
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while visit:
        node = visit.popleft()
        for i in range(4):
            newx = node[0]+dx[i]
            newy = node[1]+dy[i]
            if 0<=newx<N and 0<=newy<N:
                if graph[newy][newx]==graph[node[1]][node[0]] and visited[newy][newx]==0:
                    visit.append((newx, newy))
                    visited[newy][newx]=1
graph_norm = []
graph_risg = []
num_norm = 0
num_risg = 0
visited_norm = [[0]*N for _ in range(N)]
visited_risg = [[0]*N for _ in range(N)]

for i in range(N):
    appendline = list(sys.stdin.readline().rstrip())
    appendline2 = appendline[:]
    graph_norm.append(appendline)
    graph_risg.append(appendline2)
    for j in range(N):
        if graph_norm[i][j]=="R":
            graph_risg[i][j]="G"
    

for a in range(N):
    for b in range(N):
        if visited_norm[b][a]==0:
            bfs(graph_norm, visited_norm, a, b)
            num_norm+=1
            

for a in range(N):
    for b in range(N):
        if visited_risg[b][a]==0:
            bfs(graph_risg, visited_risg, a, b)
            num_risg+=1
            
print(num_norm, end=" ")
print(num_risg)
    