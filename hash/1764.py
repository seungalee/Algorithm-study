import sys

SawNHeard = list(map(int, sys.stdin.readline().split()))
SawNum = SawNHeard[0]
HeardNum = SawNHeard[1]

SawPp = []
HeardPp = []

i=0
j=0

while i<SawNum:
    person = sys.stdin.readline().rstrip()
    SawPp.append(person)
    i+=1

while j<HeardNum:
    person = sys.stdin.readline().rstrip()
    HeardPp.append(person)
    j+=1

SawPpSet = set(SawPp)
HeardPpSet = set(HeardPp)

SawHeardPpSet = SawPpSet & HeardPpSet

SawHeardPp = list(SawHeardPpSet)
SawHeardPp.sort()

print(len(SawHeardPp))
for i in range(len(SawHeardPp)):
    print(SawHeardPp[i])

