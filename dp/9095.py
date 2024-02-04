import sys

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    dp_table = [0]*12
    dp_table[1] = 1
    dp_table[2] = 2
    dp_table[3] = 4
    for i in range(4, n+1):
        dp_table[i] = dp_table[i-1]+dp_table[i-2]+dp_table[i-3]
    print(dp_table[n])