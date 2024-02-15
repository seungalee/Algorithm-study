import sys

n = int(sys.stdin.readline().rstrip())

triangle = [[0]*n for _ in range(n)]

for i in range(n):
    line = list(map(int, sys.stdin.readline().rstrip().split()))
    for j in range(i+1):
        triangle[i][j] = line[j]

for i in range(1, n):
    for j in range(i+1):
        if j==0:
            triangle[i][j] += triangle[i-1][j]
        elif j==i:
            triangle[i][j] += triangle[i-1][j-1]
        else:
            triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
print(max(triangle[n-1]))