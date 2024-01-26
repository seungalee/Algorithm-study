import sys

k, n = map(int, sys.stdin.readline().rstrip().split())
lines = []
for _ in range(k):
    lines.append(int(sys.stdin.readline().rstrip()))

start = 1
end = 2 ** 31 - 1

while start<=end:
    middle = (start+end)//2
    line_num = 0
    for line in lines:
        line_num += line//middle
    if line_num < n:
        end = middle - 1
    else:
        start = middle + 1

print(end)