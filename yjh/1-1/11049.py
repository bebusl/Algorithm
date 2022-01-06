import math

'''
3
5 3
3 2
2 6

4
5 3
3 2
2 6
6 2
'''


def solution(s, e):
    if s == e:  # 같은 경우
        return 0

    if dp[s][e]:  # 이미 있는 경우
        return dp[s][e]

    if e == s + 1:  # 1 차이 나는 경우
        dp[s][e] = arr[s][0] * arr[s][1] * arr[e][1]
        return dp[s][e]

    for i in range(s, e):  # 0 ~ n-1
        ret = solution(s, i) + solution(i + 1, e) + arr[s][0] * arr[i][1] * arr[e][1]
        if not dp[s][e] or ret < dp[s][e]:
            dp[s][e] = ret

    return dp[s][e]


N = int(input())

arr = []
for i in range(N):
    arr.append(list(map(int, input().split() + [i])))

size = len(arr)
dp = [[0] * size for i in range(size)]

print(solution(0, size - 1))

print("DP Table")
for x in range(-1, size):
    for y in range(-1, size):
        if x == -1 and y == -1:
            print('   ', end=' ')
        elif x == -1:
            print("%3d" % y, end=' ')
        elif y == -1:
            print("%3d" % x, end=' ')
        else:
           print("%3d" % dp[x][y], end=' ')
    print()