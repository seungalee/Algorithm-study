def solution(n, left, right):
    answer = []
    for i in range(left, right+1):
        column = (i // n) + 1
        row = i % n + 1
        if row <= column:
            answer.append(column)
        else:
            answer.append(row)
    
    return answer