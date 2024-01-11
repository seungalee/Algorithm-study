import sys

a, b = map(int, sys.stdin.readline().split())

answer = 1

while True:
    if b%10==1:
        b = (b-1)//10
        answer+=1
    elif b%2==0:
        b = b//2
        answer+=1
    else:
        answer = -1
        break
    if b==a:
        break
    if b==0:
        answer=-1
        break

print(answer)