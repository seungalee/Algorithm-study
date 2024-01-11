import sys
from queue import PriorityQueue

n = int(sys.stdin.readline())
card_arr = PriorityQueue()
answer = 0

for i in range(n):
    card_arr.put(int(sys.stdin.readline()))

#처음 실패 이유: 카드 리스트를 계속 갱신해야 한다는 점을 망각함(합친 카드 더미를 다음 계산에서 최소인지 고려해야한다)
#계속 배열을 정렬하려 시도해 시간초과
#
#->우선순위 큐(힙) 사용해라!

while n>1:
    min1 = card_arr.get()
    min2 = card_arr.get()
    answer+= (min1+min2)
    card_arr.put(min1+min2)
    n-=1

print(answer)

