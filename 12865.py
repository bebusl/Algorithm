N, K = map(int, input().split())

dp = [[0 for j in range(K + 1)] for i in range(N + 1)]
arr = []
for i in range(1, N+1):
    W, V = map(int, input().split())
    arr.append([W, V])
    for j in range(K + 1):
        if W <= j:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - W] + V)
        else:
            dp[i][j] = dp[i - 1][j]

print("Article Table")
for i in range(N):
    print('%d -> W: %d, V: %2d' % (i, arr[i][0], arr[i][1]))

print()
print("DP Table")
for i in range(-1, N + 1):
    for j in range(-1, K + 1):
        if i == -1 and j == -1:
            print('  ', end=' ')
        elif i == -1:
            print('%2d' % j, end=' ')
        elif j == -1:
            print('%2d' % i, end=' ')
        else:
            print('%2d' % dp[i][j], end=' ')
    print()

print(dp[N][K])

print('1. 해당 차례의 물건을 담는 경우')
print('dp[i][j] = dp[i - 1][j - 현재 물품 무게] + 현재 물품 가치 -> 누적 최대 가치 + 현재 물품 가치')
print('2. 해당 차례의 물건을 담지 않는 경우')
print('dp[i][j] = dp[i - 1] -> 전 물품 최대 가치')