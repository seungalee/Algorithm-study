import sys

n = int(sys.stdin.readline().rstrip())

rgb_arr = []

for _ in range(n):
    rgb_arr.append(list(map(int, sys.stdin.readline().rstrip().split())))

for i in range(1, n):
    rgb_arr[i][0] = min(rgb_arr[i-1][1], rgb_arr[i-1][2]) + rgb_arr[i][0]
    rgb_arr[i][1] = min(rgb_arr[i-1][0], rgb_arr[i-1][2]) + rgb_arr[i][1]
    rgb_arr[i][2] = min(rgb_arr[i-1][0], rgb_arr[i-1][1]) + rgb_arr[i][2]

print(min(rgb_arr[n-1]))