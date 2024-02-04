import sys

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    dp_table = [[0]*2 for _ in range(41)]
    dp_table[0] = (1, 0)
    dp_table[1] = (0, 1)
    for i in range(2, n+1):
        dp_table[i][0] = dp_table[i-1][0] + dp_table[i-2][0]
        dp_table[i][1] = dp_table[i-1][1] + dp_table[i-2][1]
    print(dp_table[n][0], end=" ")
    print(dp_table[n][1])