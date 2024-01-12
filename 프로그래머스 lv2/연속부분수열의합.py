#처음에는 연속해야 한다는 사실을 잊고 combination으로 해결하고자 해 틀림
#그 다음으로는 삼중 반복문으로 인한 시간 초과로 틀림
#반복문을 이중으로 줄여 반복문을 도는 과정에서 더해가며 맞춤

def solution(elements):
    answer = 0
    ext_arr = elements + elements
    add_arr = []
    for i in range(len(elements)):
        temp = 0
        for j in range(len(elements)):
            #element를 늘리지 않고 len(elements)로 나눈 나머지로 계산해 처리 가능
            temp += ext_arr[i+j]
            add_arr.append(temp)
    arr = set(add_arr)
    answer = len(arr)
    return answer