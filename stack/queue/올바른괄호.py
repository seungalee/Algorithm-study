# 아이디어: '('를 만나면 stack에 1 push, ')'를 만나면 1 pop. 다 입력받은 후 stack이 0이 아니라면 잘못된 것.

def solution(s):
    answer = True
    
    stack = []
    for i in s:
        if i=="(":
            stack.append(1)
        elif i==")":
            try:
                stack.pop()
            except IndexError:
                return False

    if stack==[]:
        return True
    else:
        return False