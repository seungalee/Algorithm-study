import sys

n = int(sys.stdin.readline())
locals = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline())

start = 1
#처음에 end 잘못 설정해 틀림
end = max(locals)
answer = 0

while start <= end:
    middle = (start + end) // 2
    money = 0
    for local in locals:
        if local <= middle:
            money += local
        else:
            money += middle
    if money <= m:
        start = middle + 1
    else:
        end = middle - 1
answer = end
print(answer)