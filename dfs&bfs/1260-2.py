import sys
from collections import deque
sys.stdin = open('input.txt', 'r')

n, m, v = map(int, sys.stdin.readline().split())

graph = {}

for i in range(m):
    num1, num2 = map(int, sys.stdin.readline().split())
    if num1 in graph:
        graph[num1].append(num2)
    else:
        graph[num1] = [num2]
    if num2 in graph:
        graph[num2].append(num1)
    else:
        graph[num2] = [num1]

for key in graph.keys():
    graph[key].sort(reverse = True)

dfs_visited = [False]*(n+1)
dfs_print = []

def dfs(visited, node, graph):
    visited[node] = True
    dfs_print.append(node)
    if node in graph:
        for child in graph[node]:
            if not visited[child]:
                dfs(visited, child, graph)

for key in graph.keys():
    graph[key].sort()

bfs_visited = [False]*(n+1)

bfs = deque()
bfs.append(v)
bfs_print = []
while bfs:
    node = bfs.popleft()
    if not bfs_visited[node]:
        bfs_visited[node] = True
        bfs_print.append(node)
        if node in graph:
            for child in graph[node]:
                bfs.append(child)

dfs(dfs_visited, v, graph)
for j in dfs_print:
    print(j, end=" ")

print("")
for i in bfs_print:
    print(i, end=" ")