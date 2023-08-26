def solution(brown, yellow):
    answer = []
    # a*b = brown + yellow
    # (a-2)*(b-2) = yellow
    # 2a+2b-4 = brown
    aplusb = brown//2 + 2
    for a in range(aplusb):
        b = aplusb - a
        if a*b==yellow+brown:
            break
    answer.append(a)
    answer.append(b)
    answer.sort(reverse=True)

    return answer