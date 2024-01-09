import sys

line = sys.stdin.readline().rstrip()
#-를 기준으로 나눈다
line_minus = line.split("-")
answer = 0

for i in range(len(line_minus)):
    #+를 기준으로 나눈다
    nums = line_minus[i].split("+")
    #첫 숫자들은 더해 준다
    if i==0:
        for num in nums:
            answer+=int(num)
    #- 뒤의 숫자들은 빼준다
    else:
        for num in nums:
            answer-=int(num)

print(answer)