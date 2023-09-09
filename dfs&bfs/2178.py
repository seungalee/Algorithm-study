import sys

sys.stdin = open('input.txt', 'r')

N, M = map(int, sys.stdin.readline().rstrip().split())

graph = []

for _ in range(N):
    arr = (list(sys.stdin.readline().rstrip()))
    graph.append(list(map(int, arr)))

visit = []
result = []
visit.append((0,0))
graph[0][0] = 1

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
while visit:
    node = visit.pop(0)
    if node not in result:
        result.append(node)
        canmove = False
        for i in range(4):
            newa = node[0]+dx[i]
            newb = node[1]+dy[i]
            if 0<=newa<N and 0<=newb<M:
                if graph[newa][newb]==1:
                    visit.append((newa,newb))
                    graph[newa][newb] = graph[node[0]][node[1]]+1
                    canmove = True
        if canmove == False: 
            result.remove(node)
            

print(graph[N-1][M-1])