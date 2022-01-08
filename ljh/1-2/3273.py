import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
x = int(input())
cnt =0
nums.sort()
left,right  = 0 ,n-1

while left!=right:
    tmp = nums[left] + nums[right]
    if tmp == x:
        cnt+=1#이제 더 이상 이라인 확인할 필요가 없넹.
        left+=1
    elif tmp>x:
        right-=1
    else:
        left+=1


print(cnt)