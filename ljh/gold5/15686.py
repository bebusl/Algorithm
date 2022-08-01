from cmath import inf
import sys
from itertools import combinations

input = sys.stdin.readline

N,M=map(int,input().split())

home = []
store = []

for r in range(N):
    tmp = list(map(int,input().split()))
    for c in range(N):
        if(tmp[c] == 1):
            home.append((r,c))
        elif(tmp[c]==2):
            store.append((r,c))
#store와 distance의 인덱스가 같음.
#distance = [[] for i in store]

# for k in range(len(store)):
#     cur_store = store[k]
#     for t in home:#(r,c)역할.
#         len1= cur_store[0]-t[0]
#         len2 = cur_store[1]-t[1]
#         if(len1<0):
#             len1 = -len1
#         if(len2<0):
#             len2=-len2
#         distance[k].append(len1+len2)

# print("HOME",home)
# print("STORE",store)
# print("DISTANCE",distance)


#print(list(permutations(home, M)))

combi = list(combinations(store, M))
# print("COMBI",combi)
min_result = inf
for _ in combi:
    # print("__",_)
    home_min = [inf for i in home]

    for t in _ :
        #print(store.index(t)) #store에서 이번 조합의 인덱스.
        #t가 현재꺼
        hIdx =0
        for h in home:
            len1= t[0]-h[0]
            len2 = t[1]-h[1]
            if(len1<0):
                len1 = -len1
            if(len2<0):
                len2=-len2
            if(home_min[hIdx]>len1+len2):
                home_min[hIdx]=len1+len2
            hIdx+=1
    if(min_result>sum(home_min)):
        min_result = sum(home_min)
    # print("MIN_HOME",home_min)
    # print("SUM",(sum(home_min)))
    # print("RESULT_MIN",min_result)

    # print("============")
# print("FINAL",min_result)
print(min_result)
