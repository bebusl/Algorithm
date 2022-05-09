import sys
input = sys.stdin.readline

#map 받기
N,M = map(int, input().split())

map_info = [list(map(int,list(input().strip("\n")))) for i in range(N)]
visited = [[0 for col in range(M)]for row in range(N)]
stack = []
cnt = 0

dx = [1,0,-1,0]
dy = [0,1,0,-1] #동 남 서 북

def print_map():
    for i in range(N):
        print(map_info[i])
def print_visited():
    for i in range(N):
        print(visited[i])
    

def dfs(row,col):
    for i in range(4):
        new_r = row+dy[i]
        new_c = col+dx[i]
        if(0<=new_r<N and 0<=new_c<M and not map_info[new_r][new_c] and not visited[new_r][new_c]):
            visited[new_r][new_c]=1
            stack.append((new_r,new_c))
            return dfs(new_r,new_c)
    if(len(stack)):
        tmp = stack.pop()
        new_r = tmp[0]
        new_c=tmp[1]
        return dfs(new_r,new_c)
    return
    
print_map()
for row in range(N):
    for col in range(M) : 
        if(map_info[row][col]==1):
            visited[row][col]=-1
            continue
        if(visited[row][col]==0):
            cnt+=1
            visited[row][col]=1
            dfs(row,col)
    
print("CNT :" ,cnt)
print("visited")
print_visited()
        
        
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
    
    """