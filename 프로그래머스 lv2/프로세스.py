import collections

#헷갈리는 부분: queue가 계속 변하는데 어떻게 location을 기억할 것이냐
#큐가 빈 에러가 있는데 이를 어떻게 해결하는가

def solution(priorities, location):
    answer = 0
    max_num = max(priorities)
    queue = collections.deque()
    for i in range(len(priorities)):
        if i == location:
            queue.append([True, priorities[i]])
        else:
            queue.append([False, priorities[i]])
    while True:
        now_elm = queue.popleft()
        now_bool = now_elm[0]
        now_num = now_elm[1]
        if now_num < max_num:
            queue.append([now_bool, now_num])
        else:
            answer+=1
            if now_bool == True:
                break
            else:
                max_num = max(queue, key = lambda x: x[1])[1]
        
    return answer