from collections import deque
# def findMinInHigh(value, priority):
#     min_value = max(priority)
#     for i in priority:
#         if(i>value and min_value> i):
#             min_value = i
#     return min_value
# def solution(priorities, location):
#     value = priorities[location]
#     priority = list(set(priorities))
#     priority.reverse()
#
#     min_value = findMinInHigh(value, priority)
#
#     if(min_value == value):
#         idx = 0
#         for i, v in enumerate(priorities):
#             if(v==value):
#                 idx+=1
#             if(i == location):
#                 break
#
#         return idx
#
#     front = priorities[::-1].index(min_value)
#     front = len(priorities)-1 - front
#
#     t = filter(lambda x: True if x>value else False, priorities)
#     print("더 큰 수 count", len(list(t)), front)
#     idx = 0
#     check = False
#     for i,v in enumerate(priorities[front:]):
#         if(v == value):
#             print("여기서 업데이트", i)
#             idx += 1
#         if(location == front+i):
#             print("여기서 종료", i, location)
#
#             check = True
#             break
#     if(not check):
#         for i,v in enumerate(priorities[:front]):
#             if(v == value):
#                 idx+=1
#                 print("여기서 업데이트2", i)
#
#             if(location == i):
#                 print("여기서 종료2", i, location)
#
#                 break
#
#
#     return len(list(t))+idx

# def solution(priorities, location):
#     set_of_priorities = sorted(list(set(priorities)),reverse=True)
#     last_index_of_priorities = len(priorities)-1
#     value = priorities[location]
#     if(set_of_priorities[0] == value):
#         idx = 0
#         for i,v in enumerate(priorities):
#             if(v == value):
#                 idx+=1
#             if(i==location):
#                 break
#         return idx
#
#     front = last_index_of_priorities - priorities[::-1].index(set_of_priorities[0]) # 일단 최댓값의 인덱스 부터
#     tmp = front
#     for idx in range(1,set_of_priorities.index(value)):
#         for i,v in enumerate(priorities[front:]):
#             if(v==set_of_priorities[idx]):
#                 tmp+=1
#         for i,v in enumerate(priorities[:front]):
#             if(v==set_of_priorities[idx]):
#                 tmp=i
#
#         if(v == set_of_priorities[idx]):
#             tmp+=i
#         front=tmp
#     answer = len(list(filter(lambda x: True if x>value else False, priorities)))
#     idx = 0
#     for i,v in enumerate(priorities[front:]):
#         if(v==value):
#             idx+=1
#         if(location == front+i):
#             return answer+idx
#     for i,v in enumerate(priorities[:front]):
#         if(v==value):
#             idx+=1
#         if(location == i):
#             return answer+idx
#     return answer

def solution(priorities, location):
    queue = deque([(i,v) for i,v in enumerate(priorities)])
    value = priorities[location]
    order = sorted(priorities, reverse=True)
    idx = 0
    cnt = 0
    while(queue and idx<=len(order)):
        cur_value = queue.popleft()
        if(cur_value[0]==location and order[idx] == value):
            cnt+=1
            break
        if(cur_value[1] == order[idx]):
            cnt+=1
            idx+=1
        else:
            queue.append(cur_value)
        
    return cnt




print(solution([2, 1, 3, 2]	,2))
# print(solution([1, 1, 9, 1, 1, 1],0))
# print(solution([1, 1, 2, 3, 2, 1],0))