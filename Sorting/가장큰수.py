def solution(numbers):
    answer = ''
    strs = []
    for number in numbers:
        number = str(number)
        strs.append(number)
    #str으로 변환 후 자릿수를 맞춰 비교해 주기 위해 *3
    strs.sort(key=lambda num: num*3, reverse=True)
    #int로 변환해주는 이유: 000을 방지하기 위해
    answer = str(int(''.join(strs)))

    return answer