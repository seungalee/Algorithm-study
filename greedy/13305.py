#N에 대한 제약조건 일부만 만족, 시간복잡도 해결해야 함
import sys

road_arr = []
oil_arr = []
answer = 0

n = int(sys.stdin.readline())

road_arr = list(map(int, sys.stdin.readline().split()))
oil_arr = list(map(int, sys.stdin.readline().split()))


oil_index = n-1
last_road = n-2

while oil_index!=0:
    oil_min = min(oil_arr[0:last_road+1])
    oil_index = oil_arr[0:last_road+1].index(oil_min)
    for j in range(oil_index, last_road+1):
        answer += oil_min * road_arr[j]
    last_road = oil_index - 1

print(answer)
