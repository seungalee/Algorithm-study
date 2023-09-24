# #예상: 짝수부분 실패
# def solution(n):
#     answer = 0
#     div_num=0
#     two_div_num=0
#     three_div_num=0
#     if n%2==0:
#         while n%2==0:
#             n=n/2
#             div_num+=1
#             two_div_num+=1
#         if n%3==0:
#             while n%3==0:
#                 n=n/3
#                 three_div_num+=1
#             if ((n//2)+1) >= 2*two_div_num+3*three_div_num:
#                 answer=1
        
#         else:
#             if div_num <= n:
#                 answer = 1
#     else:
#         for i in range(n):
#             if n%(i+1)==0:
#                 print(i+1)
#                 answer+=1
#     return answer

#정답 코드

def solution(n):
    answer = 0
    for i in range(n):
        num=0
        for j in range(i+1, n+1):
            num+=j
            if num == n:
                answer+=1
                break
            elif num > n:
                break
    return answer