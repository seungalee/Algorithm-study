progress = [93, 30, 55]
speeds = [1, 30, 5]


def solution(progresses, speeds):
    answer = []

    while True:
        funcNum=0
        nowFuncProg = progresses.pop(0)
        nowFuncSpeed = speeds.pop(0)
        funcNum+=1
        #첫번째 작업 끝나는 일수 계산, 그 뒤 작업에 다 더해준다
        nowFuncDate = (100-nowFuncProg)//nowFuncSpeed
        if (100-nowFuncProg)%nowFuncSpeed!=0:
            nowFuncDate+=1

        for i in range(len(progresses)):
            progresses[i-1] = progresses[i-1]+speeds[i-1]*nowFuncDate
        
        #100이 넘은 것들 pop
        if progresses[0]:
            while progresses[0]>=100:
                progresses.pop(0)
                funcNum+=1
                if progresses == []:
                    break
        
        answer.append(funcNum)
        if progresses==[]:
            break

    return answer

solution(progress, speeds)
