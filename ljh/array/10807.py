input()
prob = list(map(int, input().split()))
target = int(input())
cnt = 0
for i in prob:
    if target==i:
        cnt+=1
print(cnt)
