import sys
input = sys.stdin.readline

K = int(input())
lists = []
for i in range(K):
    tmp = int(input())
    if(tmp == 0):
        lists.pop()
    else:
        lists.append(tmp)

print(sum(lists))