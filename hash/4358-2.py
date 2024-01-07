#Counter 이용하는 코드
import sys
import collections

all = list(map(lambda s: s.rstrip(), sys.stdin.readlines()))
all_num = len(all)
counter = collections.Counter(all)
sorted_dic = sorted(counter.items())

for item in sorted_dic:
    print("%s %.4f" % (item[0], item[1]/all_num*100))


