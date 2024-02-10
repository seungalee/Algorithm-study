import sys
sys.stdin = open('input.txt', 'r')

n = int(sys.stdin.readline().rstrip())
nums = list(map(int, sys.stdin.readline().rstrip().split()))

count = 0
