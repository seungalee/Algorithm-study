import sys

sys.stdin = open('input.txt', 'r')

T = int(sys.stdin.readline())
answers = []

for i in range(T):
    M, N, K = map(int, sys.stdin.readline().rstrip().split())
    graph = [[0]*M for _ in range(N)]

    
    dx = [1, -1, 0, 0]
    dy = [0,0,1, -1]
    visit = []

    for j in range(K):
        x, y = map(int, sys.stdin.readline().rstrip().split())
        graph[y][x] = 1
        if j==0:    
            visit.append((y,x))
            graph[y][x]=0
    answer_num=0
    while True:
        result = []
        while visit:
            node = visit.pop(0)
            if node not in result:
                result.append(node)
                for k in range(4):
                    newx = node[0]+dx[k]
                    newy = node[1]+dy[k]
                    if 0<=newy<M and 0<=newx<N:
                        if graph[newx][newy]==1:
                            visit.append((newx,newy))
                            graph[newx][newy]=0
        answer_num+=1
        is_more = False
        break_toggle = False
        for a in range(M):
            for b in range(N):
                if graph[b][a]==1:
                    is_more = True
                    visit.append((b,a))
                    graph[b][a]=0
                    break_toggle=True
                    break
            if break_toggle==True:
                break
        if is_more==False:
            break
    answers.append(answer_num)

for answer in answers:
    print(answer)

                
                    
        
        
