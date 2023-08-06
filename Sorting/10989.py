import sys
sys.stdin = open('input.txt', 'r')

#2750, 2751번과 같은 방식으로 풀면 메모리 초과 발생
#sort를 이용할 수 없어 자연수의 크기제한만한 배열을 만듦
#해당 배열에 입력된 수의 횟수를 저장

lineNum = int(sys.stdin.readline())

arr = [0]*10001

for x in range(lineNum):
    num = int(sys.stdin.readline())
    arr[num] += 1

for x in range(len(arr)):
    i=1
    while i<=arr[x]:
        print(x)
        i+=1

