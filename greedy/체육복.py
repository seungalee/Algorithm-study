def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    nowlost = lost.copy()
    for person in lost:
        if person in reserve:
            nowlost.remove(person)
            reserve.remove(person)

    nownowlost = nowlost.copy()
    for pers in nowlost:
        if pers-1 in reserve:
            nownowlost.remove(pers)
            reserve.remove(pers-1)
        elif pers+1 in reserve:
            nownowlost.remove(pers)
            reserve.remove(pers+1)
            
    answer = n - len(nownowlost)
    return answer

print(solution(5,[2,4],[1,3,5]))