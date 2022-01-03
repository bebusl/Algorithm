def dfs(row, col, d):
    global arr, M, N, dir_row, dir_col

    arr[row][col] = 2

    print("----------------------------")
    for i in range(N):
        for j in range(M):
            print(arr[i][j], end=' ')
        print()

    clean = False
    cur_d = d
    for i in range(4):
        cur_d = change_index[cur_d]
        cur_row = row + dir_row[cur_d]
        cur_col = col + dir_col[cur_d]
        if 0 <= cur_row < N and 0 <= cur_col < M and arr[cur_row][cur_col] == 0:
            dfs(cur_row, cur_col, cur_d)
            clean = True
            break

    if not clean:
        cur_row = row + -dir_row[d]
        cur_col = col + -dir_col[d]
        if 0 <= cur_row < N and 0 <= cur_col < M and arr[cur_row][cur_col] == 2:
            dfs(cur_row, cur_col, d)


N, M = map(int, input().split())
start_row, start_col, start_d = map(int, input().split())

change_index = [3, 0, 1, 2]
dir_row = [-1, 0, 1, 0]
dir_col = [0, 1, 0, -1]

arr = []

for i in range(N):
    arr.append(list(map(int, input().split())))

dfs(start_row, start_col, start_d)

answer = 0
for i in range(N):
    answer += arr[i].count(2)

print(answer)