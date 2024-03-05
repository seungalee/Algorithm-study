import sys
from collections import Counter
sys.stdin = open('input.txt', 'r')


n = int(sys.stdin.readline().rstrip())
nums = []

for _ in range(n):
    nums.append(int(sys.stdin.readline().rstrip()))

nums.sort()
total = 0
for num in nums:
    total+=num

print(int("{:.0f}".format(float(total/len(nums)))))

cen = len(nums)//2

print(nums[cen])

common = 0
common_list = Counter(nums).most_common()
if n>1:
    if common_list[0][1] > common_list[1][1]:
        common = common_list[0][0]
    else:
        common = common_list[1][0]
else:
    common = common_list[0][0]
print(common)

print(nums[-1]-nums[0])
