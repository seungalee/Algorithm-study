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
