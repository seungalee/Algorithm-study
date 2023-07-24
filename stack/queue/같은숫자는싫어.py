def solution(arr):
    answer = []
    for i in arr:
        if answer:
            curr = answer.pop()
            if curr!=i:
                answer.append(curr)
                answer.append(i)
            else:
                answer.append(curr)
        else: 
            answer.append(i)
    return answer