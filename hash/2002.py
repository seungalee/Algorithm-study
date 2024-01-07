import sys

n = int(sys.stdin.readline())
in_arr = []
out_arr = []
answer = 0

for i in range(n):
    in_arr.append(sys.stdin.readline().rstrip())

for i in range(n):
    out_arr.append(sys.stdin.readline().rstrip())

in_arr_copy = in_arr[:]

#in array를 삭제해나가며 계산한다는 점은 같다
#차이점은 out_array를 모두 돌며 in array와 일치하지 않는다면 해당 차량을 in array에서 pop 해주고, 추월했다고 간주하고 out array의 다음 차량으로 넘어간다는 것이다

for pointer_o in range(n):
    if in_arr_copy[0] == out_arr[pointer_o]:
        in_arr_copy.pop(0)
        pointer_o+=1
    else:
        in_arr_copy.remove(out_arr[pointer_o])
        answer+=1

print(answer)