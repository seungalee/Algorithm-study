import math

def solution(n,a,b):
    answer = 0
    if a>b:
        a, b = b, a
    standard = 0
    
    while True:
        n= n//2
        if a <= standard+n and b > standard+n:
            break
        elif a <= standard+n and b <= standard+n:
            continue
        else: 
            standard += n
    answer = math.log2(n) +1
    return answer