def solution(nums):
    answer = 0
    #배열을 돌며 종류 몇개인지 알아내기
    ponkeNum = 0
    ponkeType = [0]*200000
    for num in nums:
        ponkeType[num-1] = 1
    
    for i in range(len(ponkeType)):
        if ponkeType[i]==1:
            ponkeNum+=1
    
    if ponkeNum>=len(nums)/2:
        answer = len(nums)/2
    else:
        answer = ponkeNum
    return answer

##인터넷 본 더 쉬운 풀이: set 함수 활용하기! 중복을 제거해준다