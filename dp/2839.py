import sys

N = int(sys.stdin.readline())
arr = [[0]*1701 for _ in range(1701)]

answerTrue = False
for i in range(1700):
    breakToggle = False
    for j in range(i):
        arr[i+1][j] = max(arr[i+1][j], arr[i][j]+3)
        if arr[i+1][j] == N:
            breakToggle = True
            answerTrue = True
            break
        arr[i+1][j+1] = max(arr[i+1][j+1], arr[i][j]+5)
        if arr[i+1][j+1] == N:
            breakToggle = True
            answerTrue = True
            break
    if breakToggle == True:
        break
            
if answerTrue == True:
    print(i)
else:
    print(-1)