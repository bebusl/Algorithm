import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
queue = deque([i for i in range(1,N+1)])

while(len(queue)>1):
    queue.popleft()
    tmp = queue.popleft()
    queue.append(tmp)
print(queue.pop())

