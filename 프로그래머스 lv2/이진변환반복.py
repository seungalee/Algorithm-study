def solution(s):
    answer = []
    convert_num = 0
    zero_num = 0
    
    while True:
        now_zero_num=0
        list_s = list(s)
        for num in s:
            if num=='0':
                zero_num+=1
                now_zero_num+=1
        new_num = ""
        for i in range(len(list_s)-now_zero_num):
            new_num += "1"
        convert_num+=1
        s = str(format(len(new_num), 'b'))
        if s=="1":
            break
    answer.append(convert_num)
    answer.append(zero_num)
                
    return answer