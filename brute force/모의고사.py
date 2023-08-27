def solution(answers):
    answer = []
    oneNum = 0
    twoNum = 0
    threeNum = 0
    oneAns = []
    twoAns = []
    threeAns = []

    for i in range(len(answers)):
        if i%10==0:
            oneAns.append(1)
            threeAns.append(3)
        elif i%10==1:
            oneAns.append(2)
            threeAns.append(3)
        elif i%10==2:
            oneAns.append(3)
            threeAns.append(1)
        elif i%10==3:
            oneAns.append(4)
            threeAns.append(1)
        elif i%10==4:
            oneAns.append(5)
            threeAns.append(2)
        elif i%10==5:
            oneAns.append(1)
            threeAns.append(2)
        elif i%10==6:
            oneAns.append(2)
            threeAns.append(4)
        elif i%10==7:
            oneAns.append(3)
            threeAns.append(4)
        elif i%10==8:
            oneAns.append(4)
            threeAns.append(5)
        else:
            oneAns.append(5)
            threeAns.append(5)
        if i%2==0:
            twoAns.append(2)
        else:
            if i%8==1:
                twoAns.append(1)
            elif i%8==3:
                twoAns.append(3)
            elif i%8==5:
                twoAns.append(4)
            elif i%8==7:
                twoAns.append(5)
    
    for j in range(len(answers)):
        if oneAns[j]==answers[j]:
            oneNum+=1
        if twoAns[j]==answers[j]:
            twoNum+=1
        if threeAns[j]==answers[j]:
            threeNum+=1
    nums = [oneNum, twoNum, threeNum]
    for k in range(len(nums)):
        if nums[k] == max(nums):
            answer.append(k+1)
    return answer