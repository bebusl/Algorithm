import sys
input = sys.stdin.readline

def to_array():
    return list(map(int, input().split()))

M, N = to_array()
A = to_array()
B = to_array()

A_IDX = 0
B_IDX = 0

result = []

while(True):
    if(A_IDX==M):
        result.extend(B[B_IDX:])
        break
    if(B_IDX==N):
        result.extend(A[A_IDX:])
        break
    if(A[A_IDX] < B[B_IDX]):
        result.append(A[A_IDX])
        A_IDX+=1
    elif(A[A_IDX]>B[B_IDX]):
        result.append(B[B_IDX])
        B_IDX+=1
    else:
        result.extend([A[A_IDX],B[B_IDX]])
        A_IDX+=1
        B_IDX+=1

print(' '.join(list(map(str,result))))