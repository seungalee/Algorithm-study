progress = [93, 30, 55]
speeds = [1, 30, 5]


def solution(progresses, speeds):
    answer = []
    time = 0
    count = 0

    while len(progresses)>0:
        if progresses[0]+time*speeds[0]>=100:
            progresses.pop(0)
            speeds.pop(0)
            count+=1
        else:
            if count!=0:
                answer.append(count)
                count = 0
            else:
                time+=1
    #그냥 종료하면 마지막 count가 배열에 들어가지 않으므로 반복문을 빠져나와 한번 더 append
    answer.append(count)
    return answer

print(solution(progress, speeds))

