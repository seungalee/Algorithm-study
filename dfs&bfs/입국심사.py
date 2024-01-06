import sys

sys.stdin = open('input.txt', 'r')

n = int(sys.stdin.readline())
array = []

for i in range(n):
    arr = list(sys.stdin.readline().rstrip())
    array.append(list(map(int, arr)))

visit = []

group_num = 0
each_group_num = []

while True:
    breaker = False
    for anum in range(n):
        for bnum in range(n):
            if array[anum][bnum]!=0:
                    breaker=True
                    break
        if breaker == True:
            break
    if anum==n-1 and bnum==n-1:
        if array[anum][bnum]==0:
            break
    visit.append((anum, bnum))
    result = []
    while visit:
        node = visit.pop(0)
        a, b = node[0], node[1]
        if node not in result:
            result.append(node)
            array[a][b]=0
            if a!=0 and array[a-1][b]==1:
                if (a-1, b) not in visit and (a-1, b) not in result:
                    visit.append((a-1,b))
            if a!=n-1 and array[a+1][b]==1:
                if (a+1, b) not in visit and (a+1, b) not in result:
                    visit.append((a+1,b))
            if b!=0 and array[a][b-1]==1 and (a, b-1) not in result:
                if (a, b-1) not in visit:
                    visit.append((a,b-1))
            if b!=n-1 and array[a][b+1]==1:
                if (a, b+1) not in visit and (a, b+1) not in result:
                    visit.append((a,b+1))
    group_num+=1
    each_group_num.append(len(result))

print(group_num)
each_group_num.sort()
for num in each_group_num:
    print(num)