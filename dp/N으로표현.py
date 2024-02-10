def solution(N, number):
    #실패 이유: dp 저장을 숫자말고 횟수로 한다는 생각을 못함
    answer = -1
    #dp 배열
    dp_arr = [set([int(str(N)*i)]) for i in range(1, 9)]
    
    #연산 횟수마다 계산
    for i in range(8):
        for j in range(i):
            for num1 in dp_arr[j]:
                for num2 in dp_arr[i-j-1]:
                    dp_arr[i].add(num1+num2)
                    dp_arr[i].add(num1-num2)
                    dp_arr[i].add(num1*num2)
                    if num2 != 0:
                        dp_arr[i].add(num1//num2)
        if number in dp_arr[i]:
            answer = i+1
            break
    return answer