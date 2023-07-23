from heapq import heapify, heappop, heappush


def solution(jobs):
    heapify(jobs)
    lenofJobs = len(jobs)
    time = 0
    
    nowDisk = heappop(jobs)
    time += nowDisk[1]
    totaltime = nowDisk[0]+nowDisk[1]
    
    while len(jobs)>0:
        readyDisk = []
        while True:
            nowDisk = heappop(jobs)
            if nowDisk[0] <= time:
                readyDisk.append(nowDisk)
            else:
                heappush(jobs, nowDisk)
                break
            if len(jobs)==0:
                break
        #여기서 에러발생: 2차원 배열의 특정 행에서 최소값 어떻게 찾지?
        readyDiskWorkTime = []
        for i in readyDisk:
            readyDiskWorkTime.append(i[1])
        nextjobIndex = readyDiskWorkTime.index(min(readyDiskWorkTime))
        time += readyDisk[nextjobIndex][1]
        totaltime += (time-readyDisk[nextjobIndex][0])
        del readyDisk[nextjobIndex]
        for i in readyDisk:
            heappush(jobs, i)
    answer = totaltime/lenofJobs
    return answer

jobs = [[0, 3], [1, 9], [2, 6]]
solution(jobs)