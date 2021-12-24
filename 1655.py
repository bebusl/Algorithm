import sys
import heapq

N = int(input())
min_heap = []
max_heap = []

for i in range(N):
    value = int(sys.stdin.readline())
    if len(max_heap) != len(min_heap):  # 홀
        heapq.heappush(min_heap, value)
    else:  # 0, 짝
        heapq.heappush(max_heap, -value)

    if max_heap and min_heap and -min_heap[0] > max_heap[0]:
        tmp = heapq.heappop(max_heap)
        tmp2 = -heapq.heappop(min_heap)
        heapq.heappush(min_heap, -tmp)
        heapq.heappush(max_heap, tmp2)

    print(max_heap, "|", min_heap)
    print(-max_heap[0])

