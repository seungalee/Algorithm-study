import sys
import itertools
from collections import deque

sys.stdin = open('input.txt', 'r')

N, M = map(int, sys.stdin.readline().split())

safety_num = 0
graph_org = []
for _ in range(N):
    graph_org.append(list(map(int, sys.stdin.readline().split())))


def bfs(graph, x, y):
    visit = deque()
    visit.append((x,y))
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    while visit:
        node = visit.popleft()
        for i in range(4):
            newx = node[0]+dx[i]
            newy = node[1]+dy[i]
            if 0<=newx<M and 0<=newy<N:
                if graph[newy][newx] == 0:
                    graph[newy][newx]=2
                    visit.append((newx, newy))

arr_NandM = []
for i in range(N):
    for j in range(M):
        arr_NandM.append((i, j))

walls_list = list(itertools.combinations(arr_NandM, 3))
    
for walls in walls_list:
    breakToggle=False
    graph_copy = [arr[:] for arr in graph_org]
    for wall in walls:
        if graph_copy[wall[0]][wall[1]]==0:
            graph_copy[wall[0]][wall[1]] = 1
        else:
            breakToggle = True
            break
    if breakToggle==True:
        continue
    for i in range(N):
        for j in range(M):
            if graph_copy[i][j] == 2:
                bfs(graph_copy, j, i)
    nownum = 0
    for i in range(N):
        for j in range(M):
            if graph_copy[i][j]==0:
                nownum+=1
    safety_num = max(safety_num, nownum)

print(safety_num)