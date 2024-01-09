import sys

answer = 0
n = int(sys.stdin.readline())

a_arr = list(map(int, sys.stdin.readline().split()))
b_arr = list(map(int, sys.stdin.readline().split()))

a_arr.sort()
#b_arr.sort(reverse=True)

for i in range(n):
    answer += a_arr[i] * max(b_arr)
    b_arr.remove(max(b_arr))
    #answer+=a_arr[i]*b_arr[i]

print(answer)