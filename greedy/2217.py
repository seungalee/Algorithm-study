import sys

n = int(sys.stdin.readline())
max_w = 0
rope_arr = []
for i in range(n):
    rope_arr.append(int(sys.stdin.readline()))

rope_arr.sort()

for i in range(n):
    max_w = max(max_w, rope_arr[i]*(n-i))

print(max_w)