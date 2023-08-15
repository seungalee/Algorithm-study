def solution(clothes):
    answer = 1
    dic = {}
    for cloth in clothes:
        cname, ctype= cloth
        if ctype in dic.keys():
            dic[ctype].append(cname)
        else:
            dic[ctype] = [cname]
    
    for keys in dic.keys():
        answer*=(len(dic[keys])+1)
    answer-=1

    return answer