import sys

n = int(sys.stdin.readline().rstrip())
stairs = []

for _ in range(n):
    stairs.append(int(sys.stdin.readline().rstrip()))

dp = [[0]*2 for _ in range(301)]
dp[0][0] = stairs[0]
if(n>=2):
    dp[1][0] = stairs[1]
    dp[1][1] = stairs[0] + stairs[1]

for i in range(2, n):
    dp[i][0] = max(dp[i-2])+stairs[i]
    dp[i][1] = dp[i-1][0]+stairs[i]

print(max(dp[n-1]))