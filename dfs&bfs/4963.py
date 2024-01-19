import sys
#dfs 이용
sys.setrecursionlimit(10**7)
move = [[0, 1], [1, 0], [0, -1], [-1, 0], [1, 1], [-1, -1], [1, -1], [-1, 1]]

#굳이 graph 따로 전달 안하고 node만 전달해도 상관없음
def dfs(node, graph):
    x, y = node
    if graph[x][y] == 1:
        graph[x][y] = 0
        for j in range(len(move)):
            dx = x + move[j][0]
            dy = y + move[j][1]
            if dx>=0 and dx<h and dy>=0 and dy<w:
                dfs((dx, dy), graph)
        return True
    return False


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
            if dfs((j, i), graph)== True:
                answer+=1
                #True, False 여부로 따지지 말고 graph 값이 1이면 dfs 함수 호출하고 answer +1 해주는 방법으로 해결 가능
    print(answer)


