from collections import deque
def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)]
    distance = [0]*(n+1)
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
    queue = deque()
    queue.append(1)
    while queue:
        now = queue.popleft()
        for node in graph[now]:
            if distance[node]==0 and node!=1:
                distance[node] = distance[now]+1
                queue.append(node)
    max_dist = max(distance)
    for node_dist in distance:
        if node_dist == max_dist:
            answer+=1
    return answer