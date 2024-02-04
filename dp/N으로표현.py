def solution(N, number):
    #실패 코드
    answer = 0
    #dp 배열
    dp_arr = [9]*32001
    dp_arr[1] = 2
    start_nums = []
    start_nums.append((N, 1))
    start_nums.append((10*N + N, 2))
    start_nums.append((100*N + 10*N + N, 3))
    start_nums.append((1000*N + 100*N + 10*N + N, 4))
    start_nums.append((10000*N +1000*N + 100*N + 10*N + N, 5))
    a = N*N
    if a >=2:
        while a <= 32000:
            start_nums.append(a)
            a = a*N

    for j in range(7):
        for k in range(4):
            if start_nums[k][0] + N*j <= 32000:
                dp_arr[start_nums[k][0] + N*j] = start_nums[k][1] + j
    
    #점화식 이용?
    for i in range(2, number+1):
        #+ N/N
        dp_arr[i] = min(dp_arr[i], dp_arr[i-1]+2)
        #+ N
        if i >= N:
            dp_arr[i] = min(dp_arr[i-N]+1, dp_arr[i])
        #+ NN/N
        if i>=11:
            dp_arr[i] = min(dp_arr[i-11]+3, dp_arr[i])
        if i*N <= 32000:
            dp_arr[i] = min(dp_arr[i*N]+1, dp_arr[i])
        
    if dp_arr[i] <= 8:
        answer = dp_arr[i]
    else:
        answer = -1
    return answer