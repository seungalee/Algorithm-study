import sys
#재귀를 이용한 이분 탐색

n = int(sys.stdin.readline())
n_arr = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline())
m_arr = list(map(int, sys.stdin.readline().rstrip().split()))

n_arr.sort()

def binary_search(left, find, right):
    middle = (left+right)//2
    if find < n_arr[left] or find > n_arr[right]:
        return 0
    if n_arr[middle]==find:
        return 1
    else:
        if n_arr[middle]<find:
            #재귀적 호출할 때 return 붙여주는 걸 잊지 말자
            return binary_search(middle+1, find, right)
        else:
            return binary_search(left, find, middle-1)

for num in m_arr:
    answer = binary_search(0, num, len(n_arr)-1)
    print(answer)