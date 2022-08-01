import sys
import heapq as PriorityQueue
input = sys.stdin.readline

TC = 0
TC = int(input())
present = []
for p in range(TC):
    test = list(map(int,input().split()))
    if(test[0] == 0 ): # 애기들 만난 경우
        if( len(present)>0):
            print(-PriorityQueue.heappop(present))
        else:
            print(-1)
    else:
        for j in range(test[0]):
            PriorityQueue.heappush(present,-test[j+1])