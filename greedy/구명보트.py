def solution(people, limit):
    answer = 0
    people.sort()
    i=0
    j = len(people)-1
    while people:
        now_person = people[i]
        if j==0:
            people.remove(now_person)
            answer+=1
            j = len(people)-1
        elif now_person+people[j]<=limit:
            people.remove(people[j])
            people.remove(now_person)
            answer+=1
            j = len(people)-1
        else:
            j-=1
        
        
    return answer

print(solution([70,50,80, 50],100))

