n = int(input())

stack = []
pp = []
latest = 0
flag = True
for i in range(n):
    cur = int(input())
    if(latest < cur):
        stack.extend(j for j in range(latest+1,cur+1))
        pp.extend(['+' for t in range(cur-latest)])
        latest = cur
    top = stack[-1]
    if(top == cur):
        stack.pop()
        pp.append('-')
    else:
        flag = False
        print("NO")
        break
    
if(flag):
    for t in pp:
        print(t)


"""스택의 특성상 스택 최상단에 있는 것과 현재 입력값이 다를 시 순서가 꼬이므로 어떤 방법을 사용하더라도 원하는대로 나오게 하는 것은 불가능함"""
