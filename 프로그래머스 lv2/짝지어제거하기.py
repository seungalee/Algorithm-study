#인터넷 보고 참고해 적은 효율성 정답 코드
#문자열 말고 스택 이용하니 효율성 훨씬 빨라짐. 단순 반복문 말고 큐나 스택의 활용도 생각해 보자

def solution(s):
    answer = -1
    s_stack = []
    for letter in s:
        if s_stack == []:
            s_stack.append(letter)
        else:
            if s_stack[-1]==letter:
                s_stack.pop()
            else:
                s_stack.append(letter)
                
        
    if s_stack==[]:
        answer = 1
    else:
        answer = 0
        
            
            

    return answer