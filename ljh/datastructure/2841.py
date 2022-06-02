import sys
input = sys.stdin.readline

N,P = map(int,input().split())

guitar = [None,[],[],[],[],[],[]]
cnt = 0
for i in range(N):
    row, pret = map(int,input().split())
    cur_row = guitar[row]
    
    if(len(cur_row)==0 or pret>max(cur_row)):
        cur_row.append(pret)
        cnt+=1
    else:
        for idx,j in enumerate(cur_row):
            print(j,idx)
            if(j>=pret):
                cur_row= cur_row[idx:]
                cur_row.append(pret)
                cnt+=2
                break
    guitar[row]=cur_row

print(cnt)