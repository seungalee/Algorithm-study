def solution(s):
    answer = -1
    is_last = False
    while True:
        continue_toggle = False
        news = s
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                lists = list(s)
                del lists[i]
                del lists[i]
                news = "".join(lists)
                continue_toggle = True
        s = news
        if s=="" or continue_toggle == False:
            break

    if s=="":
        answer = 1
    else:
        answer=0
            

    return answer