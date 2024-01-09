import sys

n, k = map(int, sys.stdin.readline().split())
coin_arr = []
count = 0
for i in range(n):
    coin_arr.append(int(sys.stdin.readline()))

for i in range(n):
    count += k // coin_arr[n-i-1]
    k %= coin_arr[n-i-1]
    #아래 조건은 굳이 없어도 됨
    if k == 0:
        break

print(count)