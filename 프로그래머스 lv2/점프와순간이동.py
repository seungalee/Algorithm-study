#정확성 검사 다 맞았는데 효율성 검사 다 틀림
#bfs로 푸는 건줄 알았는데 아니었다.. 
#1. 이진수에서 1의 갯수 세기/ 2. 그리디

#1
def solution(n):
    n_bin = bin(n)
    ans = n_bin[2:].count('1')
    return ans

#2
def solution(n):
    ans = 0
    while True:
        if n==1:
            ans+=1
            break
        if n==0:
            break
        if n %2 ==1:
            ans+=1
            n = (n-1)//2
        else:
            n = n//2
    return ans
