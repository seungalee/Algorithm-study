import sys

n = int(sys.stdin.readline())

dp = [0]*101
nums = {}
dp[1] = 9
for i in range(1, 10):
    nums[i] = 1
nums[0] = 0

#0의 수, 9의 수가 관건: *2할 수 없으니까....
#이전의 0 수, 9 수를 이용해 다음 0, 9를 구할 방법 없을까?
#그냥 sort해서 계산하는 방법?

for j in range(2, n+1):
    dp[j] = (dp[j-1]-nums[0]-nums[9])*2 + (nums[0]+nums[9])
    temp = [0]*10
    temp[0] = nums[1]
    temp[9] = nums[8]
    for k in range(1, 9):
        temp[k] = nums[k-1] + nums[k+1]
    for k in range(10):
        nums[k] = temp[k]

print(dp[n]%1000000000)