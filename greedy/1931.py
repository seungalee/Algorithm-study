import sys

n = int(sys.stdin.readline())
answer = 0
times = []

for i in range(n):
    #int로 변환하지 않아 오류 발생
    times.append(list(map(int, sys.stdin.readline().split())))

#회의가 끝나는 시간, 시작하는 시간 기준으로 sort해준다(처음에는 끝나는 시간으로만 sort해 오류 발생)
times.sort(key=lambda x:(x[1], x[0]))
last_time = 0

#회의가 시작하는 시간이 last_time보다 크거나 같으면 해당 회의 추가
#(끝나는 시간 기준으로 sort했으므로 끝나는 시간은 무조건 더 크거나 같음)
for time in times:
    if time[0]>=last_time:
        answer+=1
        last_time = time[1]

print(answer)
