"""
5 6
1
5 1 1
1 2 2
1 3 3
2 3 4
2 4 5
3 4 6
"""
import sys
from collections import defaultdict
import heapq
input = sys.stdin.readline
V, E = map(int, input().split())
START = int(input())
INF = 1e9
set_ = [defaultdict(lambda  : INF) for i in range(V+1)]#0인덱스는 안쓸거임 헷갈려서..
distance = [INF for i in range(V+1)]
for i in range(E):
    s,t,w = map(int, input().split())
    set_[s][t]=w

            
distance[START]=0

def test(start):
    default_v = distance[start]
    minimum = INF
    next_ = -1
    heap=[]
    for idx in set_[start]:
        value = default_v + set_[start][idx]
        if(distance[idx]>value):
            distance[idx]=value
            heapq.heappush(heap, (value, idx))
    return heapq.heappop(heap) if len(heap)>0 else -1


next_=(0,START)
while(1):
    next_ = test(next_[1])    
    if(next_ == -1):
        break

distance = list(map(lambda x: "INF" if x==1e9 else x, distance[1:]))
for i in distance:
    print(i)