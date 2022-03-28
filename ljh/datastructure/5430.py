import sys
from collections import deque
input = sys.stdin.readline

TC = int(input())

for i in range(TC):
    p = input().strip('\n').replace("RR","")
    L = 0
    R = 0
    isReversed = False
    n = int(input())
    if(n>0):
        tmp=deque(list(input().strip("\n").strip("[]").split(",")))
    else:
        input()
        tmp =deque()
    for k in p:
        if(k=='R'):
            isReversed = not isReversed
        elif(isReversed):
            R +=1
        else:
            L +=1

    # reverse를 여러번하면 
    # 연속된 R R은 결국 제자리로 되돌리므로 아예 p에서 삭제
    # 뒤집지 않고 삭제=>popleft, 뒤집은 후 삭제=>pop, 뒤집어야하는가=>isReversed
    # R이 나오기 전까지 isReversed가 false면 tmp의 왼쪽에서 L개를 삭제하면 되므로 L에 1씩 더해줌
    # isReversed가 true면 tmp의 오른쪽에서 R개를 삭제하면 되므로 R에 1씩 더해줌
    # R이 나오면 isReversed 값을 toggle 해준다.
    # 이렇게 하면 가장 비용이 많이드는 reverse함수를 최대 한 번만 실행하면 된다.(나머지 pop은 시간복잡도가 O(1)이므로 아주 가벼운 작업!)


    if(len(tmp)>=R and len(tmp)-R>=L):
        for j in range(R):
            tmp.pop()
        for j in range(L):
            tmp.popleft()
        if(isReversed):
            tmp.reverse()
    else:
        tmp='error'

    if(tmp=='error'):
        print('error')
    else:
        print(str(list(tmp)).replace(" ",'').replace("'",''))