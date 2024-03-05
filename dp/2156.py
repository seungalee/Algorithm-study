import sys

n = int(sys.stdin.readline().rstrip())
cups = []
#시작점 1로 하기 위해 의미없는 값 삽입
cups.append(0)

for _ in range(n):
    cups.append(int(sys.stdin.readline().rstrip()))

#안마심, 마심, 두번 연속 마심
dp = [[0]*3 for _ in range(10001)]
dp[1][1] = cups[1]
if n>=2:
    dp[2][0] = cups[1]
    dp[2][1] = cups[2]
    dp[2][2] = cups[1]+cups[2]
if n>=3:
    dp[3][0] = cups[1] + cups[2]
    dp[3][1] = cups[1] + cups[3]
    dp[3][2] = cups[2] + cups[3]

for i in range(4, n+1):
    dp[i][0] = max(max(dp[i-1], dp[i-2]))
    dp[i][1] = max(dp[i-2]) + cups[i]
    dp[i][2] = dp[i-1][1] + cups[i]
print(max(dp[n]))