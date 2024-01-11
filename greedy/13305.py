#시간복잡도 문제 해결 완료
import sys

road_arr = []
oil_arr = []
answer = 0

n = int(sys.stdin.readline())

road_arr = list(map(int, sys.stdin.readline().split()))
oil_arr = list(map(int, sys.stdin.readline().split()))

#반복문을 한번만 수행: 배열을 앞에서부터 돌며 
# 해당 시점에서의 최저 기름값*해당 도로의 길이를 더해 나간다
min_oil = 1000000001
for j in range(n-1):
    min_oil = min(min_oil, oil_arr[j])
    answer += min_oil*road_arr[j]

print(answer)
