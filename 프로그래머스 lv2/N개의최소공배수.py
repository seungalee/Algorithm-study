def solution(arr):
    answer = 0
    arr.sort()
    num = arr[-1]
    while True:
        break_toggle= True
        num +=arr[-1]
        for i in arr:
            if num%i!=0:
                break_toggle = False
                break
        if break_toggle == True:
            break
    answer = num
    return answer