def solution(people, limit):
    answer = 0
    people.sort()
    i=0
    j = len(people)-1
    #remove와 같은 함수 사용 최소화, index 포인터를 변화시키는 것으로 해결
    #종료조건 주의; 등호 주의하자
    while i<=j:
        now_person = people[i]
        if now_person+people[j]<=limit:
            j-=1
            i+=1
            answer+=1
        else:
            j-=1
            answer+=1
        
    return answer

print(solution([70,50,80, 50],100))

