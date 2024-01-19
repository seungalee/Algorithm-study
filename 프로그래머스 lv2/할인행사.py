def solution(want, number, discount):
    answer = 0
    want_arr = []
    for i in range(len(want)):
        for j in range(number[i]):
            want_arr.append(want[i])
    for date in range(len(discount)-9):
        want_arr_temp = want_arr[:]
        arr = discount[date:date+10]
        answer_bool = True
        for thing in want_arr:
            if thing not in arr:
                answer_bool = False
            else:
                want_arr_temp.remove(thing)
                arr.remove(thing)
        if answer_bool==True and want_arr_temp==[]:
            answer+=1
    return answer