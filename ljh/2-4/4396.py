from random import randrange
import sys
input = sys.stdin.readline
#빠른 읽기

n = int(input())
jido = []
checked = []
result = [['.' for i in range(n)] for i in range(n)]

isBomb = False
where_bomb = (-1,-1)
"""
n => 지도 크기
jido => 폭탄표시되어 있는 원본 지도
checked => 클릭된 곳 표시한 지도
result => 결과물 저장할 n*n 배열
isBomb => 폭탄있는 곳을 눌렀는지 체크하는 flag
where_bomb => 폭탄있는 곳 눌린 위치(발견된 곳 이전에 폭탄있었던 위치를 result에 표시해주기 위함.)
"""

for i in range(n):
    jido.append(input().strip("\n"))

for i in range(n):
    checked.append(input().strip("\n"))

# ===================== 데이터 입력부


row = [-1,0,1,-1,1,-1,0,1]
col =[1,1,1,0,0,-1,-1,-1]
# 상,하,좌,우,대각선 총 8자리 탐색하기 위한 값 저장.

for i in range(n):
    for j in range(n):
        # 1. 폭탄이 발견된 상태고, 지도에 폭탄이 표시되어 있다 => result에 폭탄 표시
        if(isBomb and jido[i][j]=='*'):
            result[i][j]='*'
        # 2. 폭탄 발견 여부 상관X(1번에서 폭탄발견되었으면 result에 이미 폭탄 표시해둔 상태)
        #    아직 열어보지 않은 곳이다 => result에 .만 표기
        if(checked[i][j]=='.'):
            continue
        # 3. 눌렀는데 폭탄이 있는 곳이다. => 해당 자리 result에 폭탄 표시. isBomb플래그 True로 지정해주고, 현재 위치를 저장.
        elif(jido[i][j]=='*' and checked[i][j]=='x' ):
            result[i][j]='*'
            isBomb=True
            where_bomb=(i,j)
        # 4. 그 외에 눌렸는데 폭탄이 아닌곳. 주변 8개 지역에 폭탄이 몇 개 있는지 세야 함.
        else:
            tmp = 0
            for k in range(8):
                if(0<=i+row[k]<n and 0<=j+col[k]<n and jido[i+row[k]][j+col[k]]=='*'):
                    tmp= tmp+1
            result[i][j]=str(tmp)

# 2-exception. 폭탄 발견 위치 이전에 폭탄표시가 있는 구역을 놓쳤을 수 있으므로, 폭탄 발견 위치 전까지 한 번 더 지도를 탐색해 모든 폭탄 위치를 result에 표시
if(isBomb):
    for i in range(where_bomb[0]+1):
        for j in range(n):
            if((i,j)==where_bomb):
                break
            if(jido[i][j]=='*'):
                result[i][j]='*'


##결과 출력.
for i in range(n):
    print(''.join(result[i]))


"""
TestCase
n = 4
jido :
...*
*...
....
...*
checked :
....
....
....
...x
"""