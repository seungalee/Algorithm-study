def solution(s):
    slist = list(map(int, s.split()))
    slist.sort()
    answer = str(slist[0]) + " " + str(slist[len(slist)-1])
    return answer