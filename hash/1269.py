import sys

anum, bnum = map(int, sys.stdin.readline().split())
in_a_and_b = 0
answer = 0
aarr = sys.stdin.readline().split()

adic = {}

#a 집합의 수들을 입력받아 adic에 넣는다
for num in aarr:
    if num not in adic:
        adic[num] = "true"

barr = sys.stdin.readline().split()

#b 집합의 수가 a 집합과 중복된다면 in_a_and_b를 1 증가시킨다
for num in barr:
    if num in adic:
        in_a_and_b+=1

#a 집합 원소 수 - 중복되는 수, b 집합 원소 수 - 중복되는 수를 답에 더해준다
answer += (anum - in_a_and_b)
answer += (bnum - in_a_and_b)

print(answer)
