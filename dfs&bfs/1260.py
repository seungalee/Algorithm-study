import sys
dic = {}

n,m,v = map(int,sys.stdin.readline().rstrip().split())


for j in range(n):
    dic[j+1] = []

for i in range(m):
    num1, num2 = map(int,sys.stdin.readline().rstrip().split())
    dic[num1].append(num2)
    dic[num2].append(num1)

for key in dic.keys():
    dic[key].sort(reverse=True)

visit = []
res = []
visit.append(v)

while visit:
    node = visit.pop()
    if node not in res:
        res.append(node)
        visit.extend(dic[node])

for dfsnum in res:
    print(dfsnum, end=" ")
print("")
for key in dic.keys():
    dic[key].sort()

visit = []
res = []
visit.append(v)

while visit:
    node = visit.pop(0)
    if node not in res:
        res.append(node)
        visit.extend(dic[node])

for bfsnum in res:
    print(bfsnum, end=" ")