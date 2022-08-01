import sys
input = sys.stdin.readline

N, K = map(int,input().split())
lee = []
for i in range(1,N+1):
    lee.append(i)

cnt = N
idx = K-1
result = []

while(lee):
    idx %=len(lee)
    popping=lee.pop(idx)
    idx += K-1
    result.append(popping)

print("<",end='')
print(", ".join(map(str,result)),end='')
print(">")

# 원형 리스트 말하는 것 같은데
# idx%(리스트의 크기) 해서 삭제되도록 함.
# 인덱스는 0부터 세므로, K번째 걸 삭제하려면 K-1인덱스에 있는 값을 삭제해야 함.