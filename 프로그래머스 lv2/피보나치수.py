def solution(n):
    answer = 0
    num1 = 0
    num2 = 1
    for i in range(n-1):
        num2 = num1+num2
        num1 = num2-num1
    answer = num2 % 1234567
    return answer