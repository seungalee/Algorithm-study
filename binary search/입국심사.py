def solution(n, times):
    answer = 0
    start = 1
    end = 10 ** 18
    while start <= end:
        middle = (start+end)//2
        people = 0
        for time in times:
            people += (middle//time)
        if people >= n:
            end = middle - 1
        else:
            start = middle + 1
    answer = start
    return answer