#정확성 검사 다 맞았는데 효율성 검사 다 틀림

from collections import deque

def solution(n):
    ans = 0
    ans+=1
    arr = [0]*(n+1)
    visit = deque()
    visit.append(1)
    arr[1] = 1
    while visit:
        breakToggle = False
        node = visit.popleft()
        if node == n:
            ans = arr[node]
            break
        new_node = node*2
        if new_node == n:
            ans = arr[node]
            break
        while new_node+1<=n:
            if arr[new_node+1]==0:
                if new_node +1 == n:
                    ans = arr[node]+1
                    breakToggle = True
                    break
                visit.append(new_node+1)
                arr[new_node+1]=arr[node]+1
            new_node*=2
            if new_node == n:
                ans = arr[node]
                breakToggle = True
                break
        if breakToggle == True:
            break

    return ans