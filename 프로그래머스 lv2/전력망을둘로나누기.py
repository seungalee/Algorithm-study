import sys

def solution(n, wires):
    answer = sys.maxsize
    dic= {}
    for i in range(n):
        dic[i+1] = []
    for wire in wires:
        dic[wire[0]].append(wire[1])
        dic[wire[1]].append(wire[0])

    for wire in wires:
        dic[wire[0]].remove(wire[1])
        dic[wire[1]].remove(wire[0])
        result = []
        visit = []
        visit.append(wire[0])
        while visit:
            node = visit.pop()
            if node not in result:
                result.append(node)
                visit.extend(dic[node])
        answer = min(answer, abs(len(result)-(n-len(result))))
        dic[wire[0]].append(wire[1])
        dic[wire[1]].append(wire[0])
    return answer