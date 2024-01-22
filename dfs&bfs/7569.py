import sys
from collections import deque

m, n, h = map(int, sys.stdin.readline().split())

tomatos = []

for k in range(h):
    tomato_box = []
    for j in range(n):
        line = list(map(int, sys.stdin.readline().split()))
        tomato_box.append(line)
    tomatos.append(tomato_box)

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
answer = 0
queue = deque()

def bfs(graph):
    answer_temp = 0
    while queue:
        a, b, c = queue.popleft()
        for num in range(6):
            nx = a + dx[num]
            ny = b + dy[num]
            nz = c + dz[num]
            if 0<=nx<m and 0<=ny<n and 0<=nz<h and graph[nz][ny][nx]==0:
                graph[nz][ny][nx] = graph[c][b][a]+1
                queue.append((nx, ny, nz))
                answer_temp = max(answer_temp, graph[nz][ny][nx])
    return answer_temp

#탐색 순서를 k->j->i로 바꾸면 아주 약간 시간 효율 상승
for i in range(m):
    for j in range(n):
        for k in range(h):
            if tomatos[k][j][i] == 1:
                queue.append((i, j, k))

answer = bfs(tomatos)

#만약 0이라면(이미 모두 다 익어 있었다면) 그대로 출력, 아니라면 1 빼줌(초기값 1부터 카운트 시작했으므로)
if answer != 0:
    answer -= 1

#만약 안 익은 토마토가 있다면 -1 출력
for i in range(m):
    for j in range(n):
        for k in range(h):
            if tomatos[k][j][i] == 0:
                answer = -1
            

print(answer)