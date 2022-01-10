import sys
from math import  sqrt
from time import time
input = sys.stdin.readline
start = time()
N, K = map(int, input().split())
prefer = list(map(int, input().split()))
prefer_bunsan = []
min_ = float('inf')

for i in range(0,N-K+1):
    #m = sum(prefer[i:i+K]) #m을 j값따라 또 다르게 해줘야하는디..!
    for j in range(K,N-i+1):
        m= sum(prefer[i:i+j])/j #평균을 제대로 안 구해줘서 계속 틀렸었음.! 위에 처럼.
        bunsan = 0
        for k in range(i,i+j):
            bunsan += (prefer[k]-m)**2
        bunsan = bunsan/j
        if (bunsan>=0 and min_>bunsan):
            min_ = bunsan

print(sqrt(min_))


# 주의해야 할 점
# 1. k개 이상임! 