import sys

n, m = map(int, sys.stdin.readline().split())
set_price = []
one_price = []
answers = []
for i in range(m):
    set, one = map(int, sys.stdin.readline().split())
    set_price.append(set)
    one_price.append(one)

set_price.sort()
one_price.sort()

answers.append(n*one_price[0])
set_and_one = set_price[0]*(n//6) + one_price[0]*(n%6)
answers.append(set_and_one)
answers.append(set_price[0]*(n//6+1))

print(min(answers))
