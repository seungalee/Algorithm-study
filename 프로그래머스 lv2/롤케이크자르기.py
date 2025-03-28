def solution(topping):
    answer = 0
    topping_count = len(topping)

    first_set = set()  # 왼쪽에 있는 토핑들
    second_count = {}  # 오른쪽에 있는 토핑들의 개수 (딕셔너리로 저장)
    
    # 오른쪽 집합에 초기 값 설정
    for t in topping:
        if t in second_count:
            second_count[t] += 1
        else:
            second_count[t] = 1
    
    for i in range(topping_count - 1):
        # 첫 번째 집합에 현재 토핑 추가
        first_set.add(topping[i])
        second_count[topping[i]] -= 1
        
        # 오른쪽 집합에서 토핑이 하나 없어지면 제거
        if second_count[topping[i]] == 0:
            del second_count[topping[i]]
        
        # 두 집합의 길이가 같으면 answer 증가
        if len(first_set) == len(second_count):
            answer += 1

    return answer