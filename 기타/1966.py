import sys
import collections

t = int(sys.stdin.readline())

for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    num_queue = collections.deque(list(map(int, sys.stdin.readline().split())))
    count = 0

    sorted_num_arr = sorted(num_queue)

