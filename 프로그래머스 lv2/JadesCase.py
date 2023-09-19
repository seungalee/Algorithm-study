def solution(s):
    answer = ""
    newStr = ""
    for i in range(len(s)):
        if i==0:
            newStr += s[i].upper()
        elif i!=0 and s[i-1]==" ":
            newStr += s[i].upper()
        else:
            newStr += s[i].lower()
    answer = newStr
    return answer

#아래는 다른 사람 풀이

# def solution(s):
#     answer = ''
#     for i in s.lower().split(' '):
#         if answer == '':
#             answer += i.capitalize()
#         else:
#             answer += ' '+i.capitalize()
#     return answer

