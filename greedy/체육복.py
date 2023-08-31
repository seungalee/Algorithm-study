def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    nowlost = lost.copy()
    #lost, reserve에 동시에 있는 사람 삭제
    for person in lost:
        if person in reserve:
            nowlost.remove(person)
            reserve.remove(person)
    #reserve에 대해서 반복문 돌며 nowlost에서 삭제 가능
    for pers in reserve:
        if pers-1 in nowlost:
            nowlost.remove(pers-1)
        elif pers+1 in nowlost:
            nowlost.remove(pers+1)
    answer = n - len(nowlost)
    return answer

print(solution(5,[2,4],[3,5]))