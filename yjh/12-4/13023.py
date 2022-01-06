def dfs(arr, check, cur, cnt):
    global success

    if cnt == 4:
        success = True
        return

    check[cur] = True
    for sub in arr[cur]:
        if not check[sub]:
            check[sub] = True
            dfs(arr, check, sub, cnt + 1)

    check[cur] = False


N, M = map(int, input().split())

arr = [[] for i in range(N)]

for i in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

success = False
for i in range(M):
    check = [False for i in range(N)]
    dfs(arr, check, i, 0)
    if success:
        break

print(1 if success else 0)