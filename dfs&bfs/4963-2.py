import sys
from collections import deque
#bfs 이용
#dfs보다 시간 약간 빠름
sys.stdin = open('input.txt', 'r')

sys.setrecursionlimit(10**7)
move = [[0, 1], [1, 0], [0, -1], [-1, 0], [1, 1], [-1, -1], [1, -1], [-1, 1]]

def bfs(node, graph):
    x, y = node
    if graph[x][y] == 1:
        graph[x][y] = 0
        q = deque()
        q.append((x, y))
        while q:
            a, b = q.popleft()
            for j in range(len(move)):
                dx = a + move[j][0]
                dy = b + move[j][1]
                if dx>=0 and dx<h and dy>=0 and dy<w and graph[dx][dy]==1:
                    graph[dx][dy]=0
                    q.append((dx, dy))



while True:
    w, h = map(int, sys.stdin.readline().split())
    if w==0 and h==0:
        break
    graph = []
    for _ in range(h):
        graph.append(list(map(int, sys.stdin.readline().split())))

    answer = 0
    for i in range(w):
        for j in range(h):
            if graph[j][i]==1:
                bfs((j, i), graph)
                answer+=1
                #True, False 아니고 graph 호출 후 세는 방법으로
    print(answer)


