from collections import deque

def solution(maps):
    r = len(maps)
    c = len(maps[0])
    is_visited = [ [False for i in range(c)] for j in range(r)]
    answer = 0
    # 시작점 (0,0), 끝점 (r-1,c-1) 여기에 도착하면 depth return 하면 됨

    dirs = [(0,1),(0,-1),(1,0),(-1,0)]
    # 오, 왼, 하, 상

    queue = deque()
    queue.append((0,0,1))

    while( len(queue) ):
        cur_r, cur_c, cur_depth = queue.popleft()

        if((cur_r,cur_c) == (r-1,c-1)):
            return cur_depth
        if( is_visited[cur_r][cur_c] ):
            continue

        is_visited[cur_r][cur_c] = True
        for dir in dirs:
            new_r = cur_r+dir[0]
            new_c = cur_c+dir[1]
            if(0<=new_r<r and 0<=new_c<c and maps[new_r][new_c]):
                queue.append((new_r, new_c, cur_depth+1))


    return -1

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]),11)
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]),-1)