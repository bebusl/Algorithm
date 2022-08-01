import sys
input = sys.stdin.readline

n = int(input())
nums= []

for i in range(n):
    nums.extend(list(map(int, input().split())))

white = 0
blue = 0

def solution(row,col,step):
    global white,blue
    cnt = row*n+col
    tmp = 0

    for i in range(step):
        if(all(nums[cnt+i*n:cnt+i*n+step])):
            if(tmp==-1):
                tmp = 0
                break
            tmp = 1
        elif(not any(nums[cnt+i*n:cnt+i*n+step])):
            if(tmp==1):
                tmp = 0
                break
            tmp = -1
        else:
            tmp=0
            break;
    if(tmp==1):
        blue+=1
        return
    elif(tmp==-1):
        white +=1
        return
    elif(tmp==0):
        step = step//2
        solution(row,col,step)
        solution(row,col+step,step)
        solution(row+step,col,step)
        solution(row+step,col+step,step)

solution(0,0,n);
print(white)
print(blue)

## 이렇게 범위 설정하는 문제에서 범위때매,,, 많이 틀린다.
## 범위를 반복해서 사용해야 할 경우 꼭 변수에 넣어서 오타내는 일 없도록 하기,.!