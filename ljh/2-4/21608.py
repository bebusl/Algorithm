from collections import defaultdict
import sys
input = sys.stdin.readline

N = int(input())
Map = [[-1 for i in range(N)] for i in range(N)]
check = []
def printMap():
    for i in range(N):
        print(''.join(str(Map[i])))
col = [0,-1,1,0]
row = [-1,0,0,1]#상,좌,우,하

students = [list(map(int,input().split())) for i in range(N*N)]

real_students= defaultdict(list,{})
for i in students:
    real_students[i[0]]=i[1:]

for _ in students:
    #한 학생
    maxEmpty = 0
    maxLike = 0
    emptySpace = (-1,-1)
    likelist = []
    student, stu_a,stu_b,stu_c,stu_d = _
    for r in range(N-1,-1,-1):
        for c in range(N-1,-1,-1):
            if(Map[r][c] != -1):
                continue
            tmpEmpty=0
            tmpLike =0
            for k in range(4):
                tmpRow = r+row[k]
                tmpCol = c+col[k]
                if(0<=tmpRow<N and 0<=tmpCol<N):
                    cur_value = Map[tmpRow][tmpCol]
                    if(cur_value == -1):#주변에 빈공간
                        tmpEmpty+=1
                    if(cur_value in [stu_a,stu_b,stu_c,stu_d]):#주변에 좋아하는 애 있을 때
                        tmpLike +=1

            #네방향 세기 완료
            if(tmpLike > maxLike):
                maxEmpty=tmpEmpty
                maxLike = tmpLike
                likelist = [(r,c)]
                emptySpace = (r,c)
            elif(tmpLike == maxLike):
                likelist.append((r,c))
                if(maxEmpty <= tmpEmpty):
                    maxEmpty = tmpEmpty
                    emptySpace=(r,c)
    if(len(likelist)==1):
        likelist =likelist[0]
        Map[likelist[0]][likelist[1]]=student
    else:
        Map[emptySpace[0]][emptySpace[1]] =student
    ##printMap();
    ##print("===========================")

#주변에 좋아하는 학생 수가 0이면 학생의 만족도는 0, 1이면 1, 2이면 10, 3이면 100, 4이면 1000이다.
result=0

#이제 호감도를 셉시다!
for r in range(N):
    for c in range(N):
        cur = Map[r][c]
        tmpLike =0
        for k in range(4):
            tmpRow = r+row[k]
            tmpCol = c+col[k]
            if(0<=tmpRow<N and 0<=tmpCol<N):
                cur_value = Map[tmpRow][tmpCol]
                if(cur_value in real_students[cur]):#주변에 좋아하는 애 있을 때
                    tmpLike +=1
        if(tmpLike==0):
            continue
        result+= 10**(tmpLike-1)
# print()
# print("RESULT",result)

print(result)
