#반례 https://www.acmicpc.net/board/view/123323 보고 해결
#
import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().rstrip().split()))
maxs = []
for i in range(1, n):
    #더한 값이 음수인 경우 연결을 끊고 더하기 전까지의 값 max에 저장
    if nums[i-1]+nums[i] < 0:
        maxs.append(nums[i-1])
    else:
        #i번째 항이 양수인 경우
        if nums[i] >= 0:
            #더한 값이 i번째 항 단독보다 큰 경우 더한다
            if nums[i-1]+nums[i] >= nums[i]:
                nums[i] += nums[i-1]
            #i번째 항 단독이 큰 경우 i 단독으로만 저장
        #i번째 항이 음수인 경우, 일단 i-1 + i는 양수이므로 i-1까지 끊은 값도 저장해 놓고 이은 값도 저장한다
        else:
            maxs.append(nums[i-1])
            nums[i] += nums[i-1]

maxs.append(nums[n-1])
print(max(maxs))