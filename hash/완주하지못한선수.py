def solution(participant, completion):
    answer = ''
    dic = {}
    for person in participant:
        if dic.get(person) == None:
            dic[person] = 1
        else:
            dic[person]+=1
    for person in completion:
        dic[person]-=1
    for key in dic:
        if dic[key] != 0:
            answer = key
    return answer