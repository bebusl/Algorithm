import sys
input = sys.stdin.readline# 빠른 입력

A_= []
B_= []
cnt = 0

T = int(input())
a_len = int(input())
A = list(map(int, input().split()))
b_len = int(input())
B = list(map(int, input().split()))


for i in range(0,a_len):
    A_.append(A[i])
    for j in range(i+1,a_len):
        A_.append(A_[-1]+A[j])

for i in range(0, b_len):
    B_.append(B[i])
    if(T-B_[-1] in A_):
        cnt+=A_.count(T-B_[-1])
    for j in range(i+1,b_len):
        B_.append(B_[-1]+B[j])
        if(T-B_[-1] in A_):
             cnt+=A_.count(T-B_[-1])

print(cnt)

##defaultdict => initialValue의 기본값으로 초기화시켜줌.
# 즉 A = defaultdict(int)해두면
# A[newKey]+=5 하는 순간 원래 dict는 에러나지만, defaultdict의 경우 A[newKey]=0로 초기화해주기 때문에 문제가 발생하지 않음.
"""
from collections import defaultdict
n = int(input())
aNo = int(input())
a = list(map(int, input().split()))
bNo = int(input())
b = list(map(int, input().split()))

aSum = defaultdict(int)
answer = 0

for i in range(aNo):
    for j in range(aNo):
        if i<=j:
            aSum[sum(a[i:j+1])]+=1

for i in range(bNo):
    for j in range(bNo):
        if i<=j:
            answer+=aSum[n-sum(b[i:j+1])]

print(answer)
"""