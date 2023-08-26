def solution(sizes):
    answer = 0
    len1 = 0
    len2 = 0
    for size in sizes:
        if size[0]>=size[1]:
            if size[0]>=len1:
                len1 = size[0]
            if size[1]>=len2:
                len2 = size[1]
        else:
            if size[1]>=len1:
                len1 = size[1]
            if size[0]>=len2:
                len2 = size[0]
        answer = len1*len2
    return answer