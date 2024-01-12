def solution(s):
    answer = 0
    for i in range(len(s)):
        stack = []
        for j in range(len(s)):
            letter = s[(i+j)%len(s)]
            if letter == "[":
                stack.append("[")
            elif letter == "{":
                stack.append("{")
            elif letter == "(":
                stack.append("(")
            elif letter == "]":
                if stack!=[]:
                    popped = stack.pop()
                    if popped != "[":
                        stack.append(popped)
                        stack.append("]")
                else:
                    stack.append("]")
                    #첫 글자가 ), ], }면 무조건 틀린 문자열이므로 break해주는 것도 가능(시간 단축됨), 이때 answer-1을 해줘야 아래에서 빈 문자열이라 1을 더해줘도 올바른 답이 나온다
                    #answer-=1
                    #break
                
            elif letter == "}":
                if stack!=[]:
                    popped = stack.pop()
                    if popped != "{":
                        stack.append(popped)
                        stack.append("}")
                else:
                    stack.append("]")
                
            elif letter == ")":
                if stack!=[]:
                    popped = stack.pop()
                    if popped != "(":
                        stack.append(popped)
                        stack.append(")")
                else:
                    stack.append("]")
                
        if stack == []:
            answer+=1
    return answer