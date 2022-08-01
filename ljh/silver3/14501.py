import sys
input = sys.stdin.readline

N = int(input())
job =[False]
for i in range(N):
    a,b = map(int,input().split())
    job.append((a,b))

# job[0] =>  [0]은 소요 시간 [1] 은 버는 돈

max = 0
def findMax(tmp):
    if(tmp>max):
        return tmp
    return max

# N+1에는 일하기 불가능
# 1. 일단 일 할 수 있는지 파악(오늘날짜 + 소요날짜((0,1,2)즉 P - 1 하면됨.) > N+1 )
# 1-1. 일 할 수 있음( tmp += job[point][1]을 더해줍니다) & next update
# 1-2. 일 할 수 없음 break

for start_point in range(1,N+1):
    cur =start_point
    tmp = 0
    while(cur<=N):
        print("cur : ",cur)
        if(cur + job[cur][0] -1 < N+1):
            tmp+=job[cur][1]
            cur = cur+job[cur][0]
            continue
        break
    max = findMax(tmp)
    print("tmp : ",tmp)
    print("==================")

print("RESULT : ",max)
