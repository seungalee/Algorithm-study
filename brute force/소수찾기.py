from itertools import permutations

def solution(numbers):
    answer = 0
    numList = []
    canNumList = []
    for num in numbers:
        numList.append(num)
    #numList = list(numbers)도 가능

    #가능한 모든 수의 경우 만드는 방법-순열 사용
    for i in range(len(numList)):
        for case in permutations(numList, i+1):
            caseNum = int(''.join(case))
            canNumList.append(caseNum)
    canNumSet = set(canNumList)
    

    for canNum in canNumSet:
        if canNum==0 or canNum==1:
            continue
        notAns = False
        ##^1/2까지만 확인하면 ok
        for i in range(2, int(canNum**0.5)+1):
            if canNum%i==0:
                notAns=True
                break
        if notAns==False:
            answer+=1

    return answer