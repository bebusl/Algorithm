from sys import stdin

fastInput = stdin.readline


def input_():
    return fastInput().strip("\n")

def print_map(target):
    for j in range(len(target)):
        print(target[j])

N, M = map(int, input_().split())
print(N, M)
visited = [[0 for i in range(M)]for j in range(N)]
dfs = [list(map(int,input_())) for j in range(N)]

direction = [(-1,0),(1,0),(0,-1),(0,1)]
# 상 하 좌 우
result = 0

def check(row,col):
    # 범위 넘어가고 이미 방문한 곳/뚫려있는 곳은 체크하지 않아야 할 곳!
    if(row < 0 or row>=N or col <0 or col >=M ):
        return False
    if(visited[row][col]==0 and dfs[row][col]==0):
        visited[row][col] = 1
        for i in range(4):
            cur = direction[i]
            check(row+cur[0],col+cur[1])
        return True
    return False


for row in range(N):
    for col in range(M):
        if(check(row,col)==True):
            result+=1

print(result)





# example1
"""
15 14
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111

output 8
"""