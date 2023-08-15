import sys

yesorno = []
input = sys.stdin.readlines()

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

for line in input:
    line = line.rstrip()
    if line == ".":
        break
    returned = YesorNo(line)
    yesorno.append(returned)

for boolean in yesorno:
    if boolean == True:
        print("yes")
    elif boolean == False:
        print("no")