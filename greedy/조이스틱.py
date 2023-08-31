def solution(name):
    answer = 0
    name_list = []
    for letter in name:
        name_list.append(ord(letter)-65)
    if name_list[1] == 0:
        answer+=name_list[0]+1
        name_list.pop(0)
        while name_list[0]==0:
            name_list.pop(0)
        for i in range(len(name_list)):
            answer+=min(name_list[len(name_list)-i-1], 26-name_list[len(name_list)-i-1])+1
    else:
        while name_list[len(name_list)-1]==0:
            name_list.pop()
        for i in range(len(name_list)):
            answer+=min(name_list[i], 26-name_list[i])+1
    answer-=1
    return answer

solution("JEROEN")