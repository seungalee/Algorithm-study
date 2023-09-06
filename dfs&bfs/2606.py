import sys
#dfs로 해결

n = int(sys.stdin.readline())
num = int(sys.stdin.readline())
graph = {}

for i in range(n):
    graph[i+1] = []

for j in range(num):
    num1, num2 = map(int, sys.stdin.readline().rstrip().split())
    graph[num1].append(num2)
    graph[num2].append(num1)


visited = []
res = []
visited.append(1)

while visited:
    node = visited.pop()
    if node not in res:
        res.append(node)
        visited.extend(graph[node])

print(len(res)-1)