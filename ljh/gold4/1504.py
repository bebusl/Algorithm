from collections import defaultdict

def inputLineToNumber():
    return map(int, input().split())

INF = 1e9

N ,E = inputLineToNumber()

linkedList = [{} for i in range(N+1) ]
is_visited_one = [False for i in range(N+1)]
is_visited_two = [False for i in range(N+1)]
is_visited= set()
## initialize
distance = [INF for i in range(N+1) ]
distance[1] = 0

for idx in range(E):
    s , e , w = inputLineToNumber()
    ## start, end, weight
    linkedList[s][e] = w
    linkedList[e][s] = w

v1,v2  = inputLineToNumber()
"""
    linkedList : (destination, weight)
"""

## idx와 min값을 반환함
def findMin():
    a = sorted(distance)
    for i in a:
        idx  = distance.index(i)
        if(not idx in is_visited):
            return (idx, i)

while(len(is_visited)!=N):
    idx, minvalue = findMin() # 이제 확인 할 곳
    print("현재 탐색 중 : ",idx)


    is_visited.add(idx)
    for key,value in linkedList[idx].items():
        if(key == v1):
            is_visited_two[idx]= True
        elif(key == v2):
            is_visited_two[idx] = True
        print(minvalue+value)
        if( minvalue+value < distance[key]):
            distance[key] = minvalue+value
    print("UPDATED DISTANCE : ",distance)
    print("-------------------")

