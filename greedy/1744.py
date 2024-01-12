import sys

n = int(sys.stdin.readline())
pos_nums = []
neg_nums = []
answer = 0

for i in range(n):
    num = int(sys.stdin.readline())
    if num > 0:
        pos_nums.append(num)
    else:
        neg_nums.append(num)
    
pos_nums.sort()

#반례: num1이나 num2가 1이라면 곱하는 것보다 더하는 게 이득
#곱할 때는 특수한 경우인 1, 0, 음수를 잘 생각해 보자
while len(pos_nums) > 1:
    num1=pos_nums.pop()
    num2=pos_nums.pop()
    if num1==1 or num2==1:
        pos_nums.append(num2)
        pos_nums.append(num1)
        break
    answer+=num1*num2
while pos_nums:
    last_num = pos_nums.pop()
    answer+=last_num

neg_nums.sort(reverse=True)

while len(neg_nums) > 1:
    num1=neg_nums.pop()
    num2=neg_nums.pop()
    answer+=(num1*num2)
if neg_nums:
    now_num = neg_nums.pop()
    answer+=now_num

print(answer)