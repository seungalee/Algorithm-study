from collections import deque
# 처음에 dfs, bfs 여부를 구분하지 못했고, visited를 만들어 어디를 방문했는지 표시를 무조건 하려 했다

# answer 개수를 반환받는 부분이 헷갈렸다: nonlocal 변수를 이용하거나
# index가 끝까지 간 경우에 정답 맞는 경우에만 1 return하지 말고 정답인 경우, 아닌 경우 모두 고려해 준다
def dfs(index, total, numbers, target, answer):
    if index == len(numbers):
        if total==target:
            return 1
        else:
            return 0

    if index < len(numbers):
        return dfs(index+1, total+numbers[index], numbers, target, answer) + dfs(index+1, total-numbers[index], numbers, target, answer)
    
def solution(numbers, target):
    answer = 0
    answer = dfs(0, 0, numbers, target, 0)
    return answer