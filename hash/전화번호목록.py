def solution(phone_book):
    answer = True
    for i in range(len(phone_book)):
        for j in range(len(phone_book)-i-1):
            if len(phone_book[i])<=len(phone_book[i+j+1]):
                if phone_book[i+j+1].startswith(phone_book[i]):
                    answer=False
                    break
            else: continue
    return answer