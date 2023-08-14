import sys
testCaseNum = int(sys.stdin.readline())

for i in range(testCaseNum):
    dic = {}
    num=1
    ClothesNum = int(sys.stdin.readline())
    for j in range(ClothesNum):
        name, type = sys.stdin.readline().rstrip().split()
        if type in dic:
            dic[type].append(name)
        else:
            dic[type] = [name]
    #총 수 + nC2*a*b+nC3*a*b*c+...+a*b*c*d....
    ###(a 종류수 +1(착용X 경우))*(b 종류수+1)... -1(모두 안착용하는 경우)
    for cloth, clothArr in dic.items():
        num*=(len(clothArr)+1)
    num-=1
    print(num)