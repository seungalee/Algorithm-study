import heapq
from heapq import heappop, heappush, heapify

def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    while scoville[0] < K:
        firstmin = heappop(scoville)
        secondmin = heappop(scoville)
        newscov = firstmin + 2*secondmin
        heappush(scoville, newscov)
        answer = answer + 1

        if len(scoville) ==1 and scoville[0]<K:
            return -1
    return answer
