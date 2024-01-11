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
    for j in range(1, n):
        people_cut = sorted(people[0:j], key=lambda x:x[1])
        if people_cut[0][1] >= people[j][1]:
            answer+=1
    print(answer)