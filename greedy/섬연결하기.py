costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
n = 4

def solution(n, costs):
    answer = 0
    graph = [[0]*n for _ in range(n)]
    visit = [0]*n
    print(visit)
    costs.sort(key=lambda x:x[2])
    i=0
    while 0 in visit:
        if visit[costs[i][0]]== 0 or visit[costs[i][1]] ==0:
            visit[costs[i][0]] = 1
            visit[costs[i][1]] = 1
            answer += costs[i][2]
            i+=1
        else:
            i+=1
            continue
    
    return answer


print(solution(n, costs))