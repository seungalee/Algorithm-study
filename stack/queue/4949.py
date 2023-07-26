input = input()
input = input.replace("\n", "")
sentences = input.split('.')


yesorno = []

def YesorNo(sentence):
    parenthesis = []
    for letter in sentence:
        if letter == "(":
            parenthesis.append("(")
        elif letter == ")":
            try:
                popped = parenthesis.pop()
            except IndexError:
                return False
            if popped != "(":
                return False
        elif letter == "[":
            parenthesis.append("[")
        elif letter == "]":
            try:
                popped = parenthesis.pop()
            except IndexError:
                return False
            if popped != "[":
                return False
        elif letter==".":
            break
    if len(parenthesis)==0:
        return True
    else:
        return False



for sentence in sentences:
    if sentence == "":
        break
    i = YesorNo(sentence)
    yesorno.append(i)

for result in yesorno:
    if result == True:
        print("yes")
    elif result == False:
        print("no")