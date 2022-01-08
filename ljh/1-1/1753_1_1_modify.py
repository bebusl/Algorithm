
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
S = []
for i in range(E):
    s,t,w = map(int, input().split())
    im = set_[s][t]
    set_[s][t]=w if  im>=w else im
# map을 만들었습니다.
distance[START]=0

def test(start):
    default_v = distance[start]
    heap=[]
    heapq.heappush(heap, (default_v, start))

    while heap:
        cur_dis, cur_des = heapq.heappop(heap)
        
        if distance[cur_des] < cur_dis:
            continue
        for new_destination ,new_distance in set_[cur_des].items():
            dis = cur_dis + new_distance
            if dis < distance[new_destination]:
                distance[new_destination] = dis
                heapq.heappush(heap,(dis,new_destination)) 



test(START)

distance = list(map(lambda x: "INF" if x==1e9 else x, distance[1:]))
for i in distance:
    print(i)