import sys
input = sys.stdin.readline

goal = '666'
N = int(input())
number = 666
cnt = 0
while(True):
    if('666' in str(number)):
        cnt+=1
    if(cnt==N):
        break
    number+=1

print(number)