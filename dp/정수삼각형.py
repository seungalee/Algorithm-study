def solution(triangle):
    answer = 0
    arr = [[0]*500 for _ in range(500)]
    arr[0][0] = triangle[0][0]
    for i in range(len(triangle)-1):
        for j in range(len(triangle[i])):
            arr[i+1][j] = max(triangle[i+1][j]+arr[i][j], arr[i+1][j])
            arr[i+1][j+1] = max(triangle[i+1][j+1]+arr[i][j], arr[i+1][j+1])
    for i in range(len(triangle)):
        answer = max(answer, arr[len(triangle)-1][i])
    return answer

