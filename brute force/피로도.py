from itertools import permutations
#인터넷 참고: permutatio 통한 순열 활용

def solution(k, dungeons):
    answer = -1
    for case in permutations(dungeons):
        nowk = k
        cnt = 0
        for dungeon in case:
            if nowk>=dungeon[0]:
                nowk-=dungeon[1]
                cnt+=1
            else:
                break
        answer = max(answer, cnt)
    return answer