def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)-1):
        #정렬을 사용했으므로 앞뒤로 startswith로 비교할 필요 없다, 한번만 해도 ok
        if phone_book[i+1].startswith(phone_book[i]):
            answer = False
            break
    return answer