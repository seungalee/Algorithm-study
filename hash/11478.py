import sys
S = sys.stdin.readline().rstrip()
num = 0
dic = {}

for i in range(len(S)):
    for j in range(len(S)):
        part = S[j:j+i+1]
        if part not in dic:
            dic[part] = True

num = len(dic.keys())
print(num)