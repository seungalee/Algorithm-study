def solution(people, limit):
    answer = 0
    people.sort()
    while people:
        i=0
        tog_person = 0
        now_person = people[i]
        people.remove(now_person)
        pp_len = len(people)
        for j in range(pp_len):
            if now_person+people[pp_len - j-1]<=limit:
                tog_person = people[pp_len -j-1]
                people.remove(tog_person)
                answer+=1
                break
        if tog_person ==0:
            answer+=1
        i+=1
    return answer

