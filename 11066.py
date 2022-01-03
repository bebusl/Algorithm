from itertools import accumulate
import math


'''
2
4
40 30 30 50
15
1 21 3 4 5 35 5 4 3 5 98 21 14 17 32

'''
T = int(input())

for t in range(T):
     K = int(input())
     arr = [0] + list(map(int, input().split()))
     sum_arr = list(accumulate(arr))
     dp = [[0] * (K + 1) for i in range(K + 1)]
     for d in range(1, K):
          for tx in range(1, K - d + 1):
               ty = tx + d
               dp[tx][ty] = math.inf

               for mid in range(tx, ty):
                    dp[tx][ty] = min(dp[tx][ty], dp[tx][mid] + dp[mid + 1][ty] + sum_arr[ty] - sum_arr[tx - 1])

     print()
     print("Test Case #%d" % (t + 1))
     print("sum_arr", sum_arr)
     print("DP Table")
     for x in range(K + 1):
          for y in range(K + 1):
               print("%3d" % dp[x][y], end=' ')
          print()

     print(dp[1][K])

