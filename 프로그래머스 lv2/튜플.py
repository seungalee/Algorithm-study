def solution(s):
    answer = []
    
    arr = s.split("},{")
    s_arr = []
    for string in arr:
        s_arr.append(list(map(int, string.strip("{}").split(","))))
    
    #key=len으로 설정하면 길이순 정렬
    s_arr.sort(key=len)
    
    for sets in s_arr:
        for num in sets:
            if num not in answer:
                answer.append(num)
    return answer