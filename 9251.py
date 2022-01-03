# A = 'ACAYKP'
# B = 'CAPCAK'
A = input()
B = input()

a_len = len(A)
b_len = len(B)

dp = [[0 for c in range(b_len + 1)] for c in range(a_len + 1)]

for i in range(1, a_len + 1):
    for j in range(1, b_len + 1):
        if A[i - 1] == B[j - 1]:
            dp[i][j] += dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print("DP Table")
for i in range(-1, a_len + 1):
    for j in range(-1, b_len + 1):
        if j == -1:
            if i <= 0:
                print(end='  ')
            else:
                print(A[i - 1], end=' ')
        elif i == -1:
            if j <= 0:
                print(end='  ')
            else:
                print(B[j - 1], end=' ')
        else:
            print(dp[i][j], end=' ')
    print()

answer = dp[a_len][b_len]
print(answer)