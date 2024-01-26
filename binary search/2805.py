#python3 시간초과, pypy3 통과
#인터넷 참고
#문제 1. 이분탐색의 개념을 어떻게 적용할지 고민; 나무의 길이로
# 꼭 해당값을 찾는 게 이분 탐색이 아님! 시작점과 끝점 설정 개념을 주로 생각하자
#문제 2. 시간초과 해결하기: 재귀 X, 반복문 O, pypy3로 제출
import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
trees = list(map(int, sys.stdin.readline().rstrip().split()))

start = 1
#pypy3로 하면 sort후 [-1]로 end 찾아도 상관없음
end = max(trees)

#https://develop247.tistory.com/361 종료조건 관련 참조
while start <= end:
    middle = (start + end) // 2
    tree_len = 0
    for tree in trees:
        if tree - middle > 0:
            tree_len += (tree - middle)
    if tree_len >= m:
        start = middle + 1
    else:
        end = middle - 1

print(end)

