import sys
sys.stdin = open('input.txt', 'r')

n = int(sys.stdin.readline())
in_arr = []
out_arr = []
answer = 0

for i in range(n):
    in_arr.append(sys.stdin.readline().rstrip())

for i in range(n):
    out_arr.append(sys.stdin.readline().rstrip())

#out array를 순서대로 지나가며 in array와 일치한다면 추월 X, 일치하지 않는다면 추월한 것이므로 answer에 +1 해주었다, in array와 out array가 일치할 때까지 in array에서 삭제하였다, in array가 비면 종료
#in array에서 차량을 삭제해가며 추월 차량을 센다는 접근법은 좋았으나 이 방식으로 하면 out array에서 in array에서는 이미 삭제된 차량을 찾아야 하는 경우가 존재한다

out_start = out_arr.index(in_arr[0])
for i in range(out_start):
    in_arr.remove(out_arr[i])
answer += out_start
pointer_o = out_start
pointer_i = 0

in_arr_copy = in_arr[:]

while in_arr_copy:
    if in_arr_copy[0] == out_arr[pointer_o]:
        in_arr_copy.pop(0)
        pointer_o+=1
    else:
        in_arr_copy.remove(out_arr[0])
        answer+=1
if out_start == n-1:
    answer+=1
print(answer)