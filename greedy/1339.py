import sys
#처음에 틀린 이유: 모든 줄에서의 자릿수 합이 가장 높은 것 순으로 했어야 하는데 고려하지 않고 그냥 먼저 등장한 순서대로 크기를 정해버림

n = int(sys.stdin.readline())
org_str = []
dic = {}
answer = 0

for i in range(n):
    line = sys.stdin.readline().rstrip()
    org_str.append(line)
    #모든 문자열에서의 자릿수 총합을 먼저 구해준다
    for j in range(len(line)):
        if line[j] not in dic:
            dic[line[j]] = 10 ** (len(line) - j-1)
        else:
            dic[line[j]] += 10 ** (len(line) - j-1)
    
#자릿수 총합이 높은 순대로 dic을 정렬
dic_sorted = sorted(dic.items(), key=lambda x:x[1], reverse=True)

###아래의 과정을 거치지 않고 그냥 자릿수 총합 높은 수대로 9부터 곱해나가 모두 더해도 됨
###왜? 어떤 알파벳이 어떤 수 가지는지는 중요하지 않다
# num = 9
# for values in dic_sorted:
#     answer += num * values[1]
#     num -= 1

#자릿수 총합 순서에 따라 9부터 높은 수 할당
num = 9
for items in dic_sorted:
    dic[items[0]] = num
    num-=1

#그에 따라 수 계산
for strs in org_str:
    for j in range(len(strs)):
        answer += dic[strs[j]] * (10 **(len(strs)-j-1))

print(answer)