import sys
sys.stdin = open('input.txt', 'r')

t = int(sys.stdin.readline())

for i in range(t):
    n = int(sys.stdin.readline())
    people = []
    answer = 1
    for j in range(n):
        people.append(list(map(int, sys.stdin.readline().split())))
    
    people.sort(key=lambda x:x[0])
    #x[1] 기준 최소를 찾기 위해 반복문을 돌거나 다시 sort하지 말고 min에 저장한다
    min = people[0]
    for j in range(1, n):
        if people[j][1] < min[1]:
            answer+=1 
            min = people[j]
        
    print(answer)