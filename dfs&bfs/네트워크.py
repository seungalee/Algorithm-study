from collections import deque

def bfs(node, computers, n):
    x, y = node
    computers[x][y] = 0
    computers[y][x] = 0
    queue = deque()
    queue.append((x, y))
    while queue:
        a, b = queue.popleft()
        for i in range(n):
            if computers[a][i] == 1:
                queue.append((a, i))
                computers[a][i] = 0
            if computers[i][b] == 1:
                queue.append((i, b))
                computers[i][b] = 0
    

def solution(n, computers):
    answer = 0
    for j in range(n):
        for k in range(n):
            if computers[j][k] == 1:
                bfs((j, k), computers, n)
                answer+=1
    return answer