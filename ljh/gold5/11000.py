import sys
import heapq
input = sys.stdin.readline

N = int(input())
queue = []
rooms = []

for i in range(N):
    start,end = map(int,input().split())
    queue.append((start,end))
queue.sort() #시작시간이 빠른 것부터 배치해야 하니깡
# rooms에는 end, start로 끝남!
heapq.heappush(rooms,(queue[0][1],queue[0][0]))
for i in range(1,N):
    cur = queue[i] #
    room = rooms[0] # 끝나는 시간이 제일 빠른거!
    if(cur[0]>=room[0]): # 제일 빠른거랑 같은 날 들을 수 있다. 시간만 갱신해서 다시 넣어줌.
        heapq.heappop(rooms)
        heapq.heappush(rooms, (cur[1],cur[0]))
    else:# 제일 빠른거에 추가해서 못듣네? 그럼 새로운 날짜에 강의 들어야지.
        heapq.heappush(rooms,(cur[1],cur[0]))



print(len(rooms))
    
    # while(rooms):
    #     room = heapq.heappop(rooms)
    #     if(cur[0]>=room[0]):
    #         tmp.append((cur[1],room[1]))
    #         isOn= True
    #         break
    #     tmp.append(room)
    # if(not isOn):
    #     heapq.heappush(rooms, (cur[1],cur[0]))
    # for i in tmp:
    #     heapq.heappush(rooms, i)
    

# for t in range(N):
#     s,e = map(int,input().split())
#     classes = (-1*(e-s),s,e)
#     heapq.heappush(queue,classes)

# for t in range(N):
#     cur = heapq.heappop(queue)
#     isIn=False
#     for k in range(len(result)):
#         for v in result[k]:
#             if (v[2]<=cur[1] or cur[2]<=v[1]):
#                 isIn=True
#         if(isIn):
#             result[k].append(cur)
#             break
#     if(not isIn):
#         result.append([cur])
# #시간 초과!

# print(len(result))