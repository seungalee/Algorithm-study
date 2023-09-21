def solution(n):
    answer = 0
    n_bin = bin(n)
    one_num = n_bin.count("1")
    while True:
        n+=1
        new_n_bin = bin(n)
        new_one_num = new_n_bin.count("1")
        if one_num == new_one_num:
            break
    answer = n
    return answer