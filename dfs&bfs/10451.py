import sys
sys.setrecursionlimit(2000)

def visit(num):
    visited[num] = 1
    if visited[nums[num]] != 1:
        visit(nums[num])

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    nums = [0] + list(map(int, sys.stdin.readline().split()))
    visited = [0]*(n+1)
    count = 0

    for i in range(1, n+1):
        if visited[i]!=1:
            visit(i)
            count+=1
            
    print(count)