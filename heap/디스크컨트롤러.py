from heapq import heapify, heappop, heappush


def solution(jobs):
    heapify(jobs)
    time = 0
    readyDisk = []
    nowDisk = heappop(jobs)
    time += nowDisk[1]
    totaltime = nowDisk[0]+nowDisk[1]
    
    while len(jobs)>0:
        while True:
            nowDisk = heappop(jobs)
            if nowDisk[0] <= time:
                readyDisk.append(nowDisk)
            else:
                heappush(jobs, nowDisk)
                break
            if len(jobs)==0:
                break
        nextjobIndex = readyDisk.index(min(readyDisk[1]))
        time = readyDisk[nextjobIndex][1]
        totaltime += (time-readyDisk[nextjobIndex][0])
        answer = totaltime/(len(jobs))
        return answer

jobs = [[0, 3], [1, 9], [2, 6]]
solution(jobs)