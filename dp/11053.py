import sys

n = int(sys.stdin.readline().rstrip())
nums = list(map(int, sys.stdin.readline().rstrip().split()))

count = 0
#dp[i]에 저장되는 값: A[i]를 포함하는 가장 긴 증가하는 부분 수열
dp = [1]*(n)

for i in range(1, n):
    for j in range(i+1):
        if nums[i] > nums[j]:
            dp[i] = max(dp[i], dp[j]+1)
count = max(dp)
print(count)