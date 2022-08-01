import sys
input = sys.stdin.readline

# 목표 nlogn

N, C = map(int, input().split())
point=[]
distances = []
for i in range(N):
    tmp = int(input())
    point.append(tmp)

point.sort()
min_distance =1 
max_distance = point[-1]-point[0]
max_target = max_distance // (C-1)
result = -1


def isFound(target):
    if(target==0):
        return -1
    check = C-1
    prev = point[0]
    for i in range(1,N):
        cur = point[i]
        if(cur-prev>=target):
            prev =cur
            check-= 1
    if(check>0):
        return False
    else:
        return True
target= max_target
while(target>0):
    if(isFound(target)):
        result = target
    else:
        target -=1

print(result)
    

