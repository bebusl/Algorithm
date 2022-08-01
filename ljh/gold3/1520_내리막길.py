DIR = [[1,0],[0,1],[-1,0],[0,-1]]#상, 우, 하, 좌

map_ = []
r,c = map(int, input().split())

for j in range(r):
    map_.append([int(i) for i in input().split()])#반드시 int로 바꿔 저장!

checked = [[-1 for j in range(c)] for i in range(r)]
checked[r-1][c-1]=1

def search(cur):
    global checked
    row = cur["Row"]
    col = cur["Col"]
    if(checked[row][col]!=-1):
        return checked[row][col] # 이게 dp이용. 이미 있는건 dp에 저장되어 있는 값을 반환한다.
    else:
        checked[row][col]=0
        for i in DIR:
            if(not 0<=col+i[1]<c or not 0<=row+i[0]<r ) :#줄 뺌
                continue
            if(map_[row][col]>map_[row+i[0]][col+i[1]]):
                checked[row][col]+=search({"Row":row+i[0],"Col":col+i[1]})
        return checked[row][col]
    

search({"Row":0, "Col":0})
print(checked[0][0])

