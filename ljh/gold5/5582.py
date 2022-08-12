from sys import stdin
input = stdin.readline

def solution():
    A = input().strip("\n")
    B = input().strip("\n")

    result = 0
    solution = [[0 for i in range(len(B)+1)]for j in range(len(A)+1)]

    for i in range(1,len(A)+1):
        for j in range(1, len(B)+1):
            # 이건 공통부분 문자열 => 연속돼야함! 그러므로 같을 떄만 값 업데이트 해주면 됨.
            if(A[i-1]==B[j-1]):
                solution[i][j]=solution[i-1][j-1]+1
                result = max(result, solution[i][j])

    print(result)

solution()