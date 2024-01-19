import sys
from collections import deque

n = int(sys.stdin.readline())

graph = []

for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

max_num = max(map(max, graph))
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    graph_copy[x][y]=0
    while queue:
        a, b = queue.popleft()
        for m in range(4):
            nx = a + dx[m]
            ny = b + dy[m]
            if 0<=nx<n and 0<=ny<n and graph_copy[nx][ny]>0:
                graph_copy[nx][ny]=0
                queue.append((nx, ny))

answer = 0
rain = 0

while rain <= max_num:
    graph_copy = [arr[:] for arr in graph]
    for i in range(n):
        for j in range(n):
            graph_copy[i][j]-=rain
    temp_answer = 0
    for i in range(n):
        for j in range(n):
            if graph_copy[i][j]>0:
                bfs(i, j)
                temp_answer+=1
    answer = max(temp_answer, answer)
    rain+=1

print(answer)