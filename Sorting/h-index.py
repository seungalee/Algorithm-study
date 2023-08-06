citations = [3, 0, 6, 1, 5, 7, 8, 2, 9]

def solution(citations):
    answer = 0
    #인용수 배열을 정렬
    #[0, 1, 2, 3, 5, 6, 7, 8, 9]
    #[9, 8, 7, 6, 5, 3, 2, 1, 0]
    #index+1(인용된 논문 갯수)> citation[index](인용횟수)인 최소의 index 찾기?
    index = 0
    citations.sort(reverse=True)
    for i in range(len(citations)):
        if i+1 > citations[i]:
            index = i
            break
        else:
            continue
    answer = index
    return answer

print(solution(citations))