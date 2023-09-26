import math
def solution(n):
    two_num = 0
    answer =1
    while True:
        if n==two_num or n==two_num+1:
            break
        n-=1
        two_num +=1
        answer += math.comb(n, two_num)
    answer = answer % 1234567
    return answer