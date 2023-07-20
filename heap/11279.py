#최대 힙 배열
heap = []

#입력받은 수 삽입
def InsertNum(number):
    heap.append(number)
    i=len(heap)-1
    while i>1:
        if heap[i]>heap[i//2]:
            heap[i], heap[i//2] = heap[i//2], heap[i]
        else: 
            break
    
def RemoveMax():
    i=len(heap)-1
    del heap[0]
    if i>0:
        heap[0], heap[-1] = heap[-1], heap[0]
        if heap[0]>heap[]