import sys
#힌트 보고 해결
#https://www.acmicpc.net/board/view/8301

n, c = map(int, sys.stdin.readline().rstrip().split())
houses = []
for _ in range(n):
    houses.append(int(sys.stdin.readline().rstrip()))

houses.sort()

start = 1
end = houses[-1]//(c-1)
answer = 0

while start <= end:
    middle = (start + end) // 2
    count = 1
    last_house = houses[0]
    for i in range(1, len(houses)):
        if houses[i] - last_house >= middle:
            count+=1
            last_house = houses[i]
    if count >= c:
        start = middle + 1
    else:
        end = middle - 1

print(end)
    