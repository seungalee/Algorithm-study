import sys

testCaseNum = int(sys.stdin.readline())
dic = {}

for i in range(testCaseNum):
    ClothesNum = int(sys.stdin.readline())
    for j in range(ClothesNum):
        name, type = sys.stdin.readline().rstrip().split()
        if type in dic:
            dic[type].append(name)
        else:
            dic[type] = [name]
    #총 수 + nC2*a*b+nC3*a*b*c+...+a*b*c*d....
    