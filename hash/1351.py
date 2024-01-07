import sys

n, p, q = map(int, sys.stdin.readline().split())

dic = {}
dic[0] = 1

def getA(i):
    if i in dic: 
        return dic[i]
    else:
        # if i//p in dic:
        #     a1 = dic[i//p]
        # else:
        #     a1 = getA(i//p)

        # if i//q in dic:
        #     a2 = dic[i//q]
        # else:
        #     a2 = getA(i//q)
        dic[i] = getA(i//p) + getA(i//q)
        return dic[i]
      

answer = getA(n)

print(answer)

'''
a256 = a128 + a64 = 89
a128 = a64 + a32 = 56
a64 = a32 + a16 = 35
a32 = a16 + a8 = 21
a16 = a8 + a4 = 13
a8 = a4 + a2 = 8
a4 = a2 + a1 = 5
a2 = a1 + a0 = 3
a1 = 2 

'''

