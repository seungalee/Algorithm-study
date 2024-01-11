import sys

n = int(sys.stdin.readline())

n_arr = list(str(n))
n_arr.sort(reverse=True)

total = 0
for num in n_arr:
    total+=int(num)

if total%3 != 0:
    print(-1)
elif n_arr[-1]!="0":
    print(-1)
else:
    #join 이용해 반복문 사용하지 않고 list 문자열로 변환하여 출력 가능
    #print("".join(n_arr))
    for num in n_arr:
        print(num, end="")
    