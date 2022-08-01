import sys
from collections import deque
input = sys.stdin.readline

TC = int(input())
for i in range(TC):
    N, M  = map(int,input().split())
    numbers = list(map(int,input().split()))
    queue = deque()
    cnt=0

    for i in range(N):
        queue.append((numbers[i],i))
    numbers.sort()
    idx =0
    while(True):
        cur = queue.popleft()
        if(cur[0] == numbers[-1]):
            numbers.pop(-1)
            idx+=1

            if(cur[1]==M):
                print(idx)
                break
        else:
            queue.append(cur)




        