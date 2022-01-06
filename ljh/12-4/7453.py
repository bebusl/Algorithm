import sys
from collections import defaultdict

input = sys.stdin.readline# 빠른 입력

n = int(input())
A=[]
B=[]
C=[]
D=[]
cnt=0

first=defaultdict(int)

for i in range(n):
    a,b,c,d= map(int,input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

for i in range(n):
    for j in range(n):#a랑 비교할거임!
        first[A[i]+B[j]]+=1

for i in range(n):
    for j in range(n):
        value = -(C[i] + D[j])
        if value in first:
            cnt += first[value]

print(cnt)


# redux hook도 한번 써봐야징~~