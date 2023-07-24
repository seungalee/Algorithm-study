def solution(arr):
    answer = []
    for i in arr:
        if answer:
            curr = answer[-1]
            if curr!=i:
                answer.append(i)
        else: 
            answer.append(i)
    return answer
