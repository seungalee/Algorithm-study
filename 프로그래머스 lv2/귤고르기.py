def solution(k, tangerine):
    answer = 0
    dic = {}
    for tan in tangerine:
        if tan in dic:
            dic[tan] +=1
        else:
            dic[tan] =1
    nums = list(dic.values())
    nums.sort()
    num = 0
    while True:
        num += nums.pop()
        answer+=1
        if k <= num:
            break
    return answer